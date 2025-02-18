import sys, subprocess, sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow , QMessageBox ,QHeaderView
from GreenAdvisor_UI import docter_plant_v2
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import QtGui,QtCore
plant_id_G = "N/A"
# def seach(table_view):
#     if ui.radioButton.isChecked():
#         seach_id = "มะม่วง"
#     elif ui.radioButton_2.isChecked():
#         seach_id = "ทุเรียน"
#     elif ui.radioButton_3.isChecked():
#         seach_id = "มังคุด"
#     else:
#         seach_id = "None"
#     conn = sqlite3.connect('/Users/panpom/PycharmProjects/GreenGrow_Advisor/Database/Main_data.db')  # Database path
#     cursor = conn.cursor()
#     if seach_id != "None":
#         try:
#             # Fetch data for the specific plant_id from the plant_data table
#             cursor.execute("SELECT * FROM docter_th WHERE ชนิดพืช = ?", (seach_id,))
#             rows = cursor.fetchall()
#
#             # Set up the model for the QTableView
#             model = QStandardItemModel()
#             model.setHorizontalHeaderLabels(["ID", "ชนิดพืช","ชื่อโรค", "สาเหตุ", "แนวทางการรักษา"])  # Set column headers
#
#             # Populate the model with data from the database
#             for row in rows:
#                 items = [QStandardItem(str(value)) for value in row]
#                 model.appendRow(items)
#
#             # Set the model for the QTableView
#             table_view.setModel(model)
#
#
#             if not rows:
#                 print(f"No data found for ชนิดพืช: {seach_id}")
#
#         except sqlite3.Error as e:
#             print(f"Database error: {e}")
#
#         finally:
#             # Close the database connection
#             conn.close()

def load_data_into_table(table_view):
    plant_id = ui.textEdit_plant.document().toPlainText()
    # Connect to the SQLite database
    conn = sqlite3.connect('/Users/panpom/PycharmProjects/GreenGrow_Advisor/Database/Main_data.db')  # Database path
    cursor = conn.cursor()

    cursor.execute("SELECT Type FROM Main_data WHERE plant_id = ?", (plant_id,))
    result = cursor.fetchone()  # ใช้ fetchone() เพราะคาดว่าผลลัพธ์มี 1 แถว

    if result:
        plant_type = result[0]  # ดึงค่า plant_type จาก tuple
        print(f"Plant Type: {plant_type}")
        ui.textEdit_plant.setText(str(plant_type))
    else:
        plant_type = "None"
        print("ไม่พบข้อมูล")



    if plant_type != "None":
        try:
            # Fetch data for the specific plant_id from the plant_data table
            cursor.execute("SELECT * FROM docter_en WHERE Plant_Type = ?", (plant_type,))
            rows = cursor.fetchall()

            # Set up the model for the QTableView
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(
                ["ID", "Plant Type", "Disease Name", "Cause", "Treatment"])  # Set column headers

            # Populate the model with data from the database
            for row in rows:
                items = [QStandardItem(str(value)) for value in row]
                model.appendRow(items)

            # Set the model for the QTableView
            table_view.setModel(model)

            ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
            ui.tableView.setColumnWidth(0, 50)  # คอลัมน์ที่ 1 กว้าง 150 px
            ui.tableView.setColumnWidth(1, 100)  # คอลัมน์ที่ 2 กว้าง 200 px
            ui.tableView.setColumnWidth(2, 200)  # คอลัมน์ที่ 3 กว้าง 180 px
            ui.tableView.setColumnWidth(3, 250)  # คอลัมน์ที่ 4 กว้าง 180 px
            ui.tableView.setColumnWidth(4, 450)  # คอลัมน์ที่ 5 กว้าง 180 px



        except sqlite3.Error as e:
            print(f"Database error: {e}")

        finally:
# Close the database connection
            conn.close()


# Set the model for the QTableView



    # Close the database connection
    conn.close()

def main():
    # plant_id = "P_001"
    # ui.textEdit_plant.setText(str(plant_id))
    # global plant_id_G
    # plant_id_G = plant_id
    # load_data_into_table(ui.tableView)

    # Check if plant_ID is provided as an argument
    if len(sys.argv) > 1:
        plant_id = sys.argv[1]
        print(f"Received plant_ID: {plant_id}")
        ui.textEdit_plant.setText(str(plant_id))
        global plant_id_G
        plant_id_G = plant_id
        load_data_into_table(ui.tableView)
    else:
        print("No plant_ID provided.")

# def seach_ck():
#     seach(ui.tableView)
def get_selected_case_id(table_view):
    """
    Get the plant_ID from the selected row in the QTableView.
    """
    selection_model = table_view.selectionModel()
    selected_indexes = selection_model.selectedRows()

    if selected_indexes:
        # Get the plant_ID from the first selected row (index 0 corresponds to 'plant_ID' column)
        type = selected_indexes[0].sibling(selected_indexes[0].row(), 0).data()
        print(f"Selected plant_ID: {type}")
        return type
    else:
        print("No row selected.")
        return None
def call():
    """
    Open the plant_data.py script and pass the selected plant_ID as a command-line argument.
    """
    # Get the selected plant_ID
    type = get_selected_case_id(ui.tableView)
    global plant_id_G

    if plant_id_G and type:  # ตรวจสอบว่า plant_id_G มีค่า
        try:
            result = subprocess.run(
                ["python", "/Users/panpom/PycharmProjects/GreenGrow_Advisor/GreenAdvisor_app/PopUP_app/data_popup_app/add_data_case.py", type, str(plant_id_G)],
                capture_output=True,
                text=True
            )
            print("Script Output:", result.stdout)
            print("Script Errors:", result.stderr)
        except Exception as e:
            print(f"Error running add_data_case.py: {e}")
    else:
        print("No plant_ID selected to send.")


if __name__ == '__main__':
    print("data_popUp run")
    app = QApplication(sys.argv)  # Create the main application object
    win = QMainWindow()  # Create the main window
    ui = docter_plant_v2.Ui_Form()  # Initialize the UI from .ui file
    ui.setupUi(win)  # Set up the UI elements in the main window

    win.setWindowFlags(QtCore.Qt.WindowType.Window |
                       QtCore.Qt.WindowType.CustomizeWindowHint |
                       QtCore.Qt.WindowType.WindowCloseButtonHint |
                       QtCore.Qt.WindowType.WindowMinimizeButtonHint)

    # Load data into the QTableView after setting up the UI
    #load_data_into_table(ui.tableView)  # Use 'tableView' from your UI file
   # win.show()  # Show the main window

  # Use 'tableView' from your UI file
    win.show()  # Show the main window
    main()
    # Connect buttons to their respective actions
    #ui.pushButton.clicked.connect(seach_ck)
    # Connect the selection change to a function that gets the selected plant_ID

    ui.pushButton_2.clicked.connect(call)
    # Execute the application
    sys.exit(app.exec_())
