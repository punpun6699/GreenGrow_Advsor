import sys, subprocess, sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow , QMessageBox
from GreenAdvisor_UI import data_ui
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import QtGui,QtCore

def load_data_into_table(table_view):
    # Connect to the SQLite database
    conn = sqlite3.connect('/Users/panpom/PycharmProjects/GreenGrow_Advisor/Database/Main_data.db')  # Database path
    cursor = conn.cursor()

    # Fetch data from the Main_data table
    cursor.execute("SELECT * FROM Main_data")
    rows = cursor.fetchall()

    # Set up the model for the QTableView
    model = QStandardItemModel()
    model.setHorizontalHeaderLabels(["plant_ID", "Name", "Type", "Age"])  # Set column headers

    # Populate the model with data from the database
    for row in rows:
        items = [QStandardItem(str(value)) for value in row]
        model.appendRow(items)

    # Set the model for the QTableView
    table_view.setModel(model)

    # Close the database connection
    conn.close()

def get_selected_plant_id(table_view):
    """
    Get the plant_ID from the selected row in the QTableView.
    """
    selection_model = table_view.selectionModel()
    selected_indexes = selection_model.selectedRows()

    if selected_indexes:
        # Get the plant_ID from the first selected row (index 0 corresponds to 'plant_ID' column)
        plant_id = selected_indexes[0].sibling(selected_indexes[0].row(), 0).data()
        print(f"Selected plant_ID: {plant_id}")
        return plant_id
    else:
        print("No row selected.")
        return None

def openPlantdata():

    """
    Open the plant_data.py script and pass the selected plant_ID as a command-line argument.
    """
    # Get the selected plant_ID
    plant_id = get_selected_plant_id(ui.tableView)
    if plant_id:
        try:
            # Run the new Python script with plant_ID as an argument
            result = subprocess.run(
                ["python", "/Users/panpom/PycharmProjects/GreenGrow_Advisor/GreenAdvisor_app/PopUP_app/data_popup_app/plant_data.py", plant_id],
                capture_output=True,
                text=True
            )
            print("Script Output:", result.stdout)
            print("Script Errors:", result.stderr)
        except Exception as e:
            print(f"Error running plant_data.py: {e}")
    else:
        print("No plant_ID selected to send.")

def Open_Add_data_ui():
    """
    เรียกใช้โปรแกรม plant_data.py โดยใช้เส้นทางในโฟลเดอร์ปัจจุบัน
    """
    try:
        result = subprocess.run(
            ["python", "/Users/panpom/PycharmProjects/GreenGrow_Advisor/GreenAdvisor_app/PopUP_app/data_popup_app/add_data.py"],
            capture_output=True,
            text=True
        )
        print("Script Output from openPlantdata:", result.stdout)
        print("Script Errors from openPlantdata:", result.stderr)
    except Exception as e:
        print(f"Error running openPlantdata(): \n{e}")

def reload():
    load_data_into_table(ui.tableView)
def delete_selected_data():
    """
    Delete the selected row's data from the database.
    """
    # Get the selected plant_ID
    plant_id = get_selected_plant_id(ui.tableView)
    if not plant_id:
        QMessageBox.warning(None, "No Selection", "กรุณาเลือกข้อมูลที่ต้องการลบก่อน!")
        return

        # Confirm deletion with a QMessageBox
    confirm = QMessageBox.question(
        None,  # Parent widget, ใช้ None หากไม่ต้องการ parent
        "Confirm Deletion",  # Title
        f"คุณต้องการลบข้อมูลที่มี case_id: {plant_id} จริงหรือไม่?",  # Message
        QMessageBox.Yes | QMessageBox.No,  # Buttons
        QMessageBox.No  # Default button
    )

    if confirm == QMessageBox.No:
        print("Deletion canceled.")
        return

    try:
        # Connect to the SQLite database
        db_path = '/Users/panpom/PycharmProjects/GreenGrow_Advisor/Database/Main_data.db'
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Execute the DELETE query
        cursor.execute("DELETE FROM Main_data WHERE plant_ID = ?", (plant_id,))
        conn.commit()

        # Check if rows were deleted
        if cursor.rowcount > 0:
            QMessageBox.information(None, "Success", f"ลบข้อมูลที่มี case_id: {plant_id} สำเร็จแล้ว!")
            print(f"Successfully deleted record with case_id: {plant_id}")
        else:
            QMessageBox.warning(None, "Not Found", f"ไม่พบข้อมูลที่มี case_id: {plant_id}")
            print(f"No record found with case_id: {plant_id}")

        # Reload the table data
        load_data_into_table(ui.tableView)

    except sqlite3.Error as e:
        print(f"Error deleting data: {e}")
        QMessageBox.critical(None, "Database Error", f"เกิดข้อผิดพลาดในการลบข้อมูล:\n{e}")
    finally:
        # Close the database connection
        conn.close()


def seach(table_view):
    seach_id = str(ui.textEdit.document().toPlainText())
    conn = sqlite3.connect('/Users/panpom/PycharmProjects/GreenGrow_Advisor/Database/Main_data.db')  # Database path
    cursor = conn.cursor()

    try:
        # Fetch data for the specific plant_id from the plant_data table
        cursor.execute("SELECT * FROM Main_data WHERE Plant_id = ?", (seach_id,))
        rows = cursor.fetchall()

        # Set up the model for the QTableView
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["plant_ID", "Name", "Type", "Age"])  # Set column headers

        # Populate the model with data from the database
        for row in rows:
            items = [QStandardItem(str(value)) for value in row]
            model.appendRow(items)

        # Set the model for the QTableView
        table_view.setModel(model)


        if not rows:
            print(f"No data found for Plant_id: {seach_id}")

    except sqlite3.Error as e:
        print(f"Database error: {e}")

    finally:
        # Close the database connection
        conn.close()
def seach_ck():
    seach(ui.tableView)

if __name__ == '__main__':
    print("data_popUp run")
    app = QApplication(sys.argv)  # Create the main application object
    win = QMainWindow()  # Create the main window
    ui = data_ui.Ui_Form()  # Initialize the UI from .ui file
    ui.setupUi(win)  # Set up the UI elements in the main window

    win.setWindowFlags(QtCore.Qt.WindowType.Window |
                       QtCore.Qt.WindowType.CustomizeWindowHint |
                       QtCore.Qt.WindowType.WindowCloseButtonHint |
                       QtCore.Qt.WindowType.WindowMinimizeButtonHint)

    # Load data into the QTableView after setting up the UI
    #load_data_into_table(ui.tableView)  # Use 'tableView' from your UI file
   # win.show()  # Show the main window

    app.setStyle("Fusion")
    palette = app.palette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(255, 255, 255))  # ขาว
    palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor(0, 0, 0))  # ดำ
    app.setPalette(palette)

    load_data_into_table(ui.tableView)  # Use 'tableView' from your UI file
    win.show()  # Show the main window
    # Connect buttons to their respective actions
    ui.data_Button.clicked.connect(openPlantdata)
    ui.Add_data_Button.clicked.connect(Open_Add_data_ui)
    ui.Dell_Button.clicked.connect(delete_selected_data)
    ui.reload_Button.clicked.connect(reload)
    ui.seach_Button.clicked.connect(seach_ck)
    # Connect the selection change to a function that gets the selected plant_ID

    # Execute the application
    sys.exit(app.exec_())
