import sys,subprocess,sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QTableWidgetItem
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from GreenAdvisor_UI.ui import data_ui  # Import UI from .ui file
from PyQt5.QtGui import QStandardItemModel, QStandardItem

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

def openPlantdata():
    """
    เรียกใช้โปรแกรม plant_data.py โดยใช้เส้นทางในโฟลเดอร์ปัจจุบัน
    """
    try:
        result = subprocess.run(
            ["python", "/Users/panpom/PycharmProjects/GreenGrow_Advisor/GreenAdvisor_app/PopUP_app/data_popup_app/plant_data.py"],
            capture_output=True,
            text=True
        )
        print("Script Output from openPlantdata:", result.stdout)
        print("Script Errors from openPlantdata:", result.stderr)
    except Exception as e:
        print(f"Error running openPlantdata(): \n{e}")

if __name__ == '__main__':
    print("data_popUp run")
    app = QApplication(sys.argv)  # Create the main application object
    win = QMainWindow()  # Create the main window
    ui = data_ui.Ui_Form()  # Initialize the UI from .ui file
    ui.setupUi(win)  # Set up the UI elements in the main window
    # Load data into the QTableView after setting up the UI
    load_data_into_table(ui.tableView)  # Use 'tableView' from your UI file
    win.show()  # Show the main window
    ui.data_Button.clicked.connect(openPlantdata)
    # Execute the application
    sys.exit(app.exec_())
