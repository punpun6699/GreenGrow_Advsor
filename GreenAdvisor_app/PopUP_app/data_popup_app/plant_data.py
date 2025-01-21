import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from GreenAdvisor_UI import plant_data_ui
import sqlite3  # For SQLite connection
from PyQt5.QtGui import QStandardItemModel, QStandardItem

def load_data_into_table(table_view):
    # Connect to the SQLite database
    conn = sqlite3.connect('/Users/panpom/PycharmProjects/GreenGrow_Advisor/Database/Main_data.db')  # Database path
    cursor = conn.cursor()

    # Fetch data from the Main_data table
    cursor.execute("SELECT * FROM plant_data")
    rows = cursor.fetchall()

    # Set up the model for the QTableView
    model = QStandardItemModel()
    model.setHorizontalHeaderLabels(["Case_id", "Type", "Plant_id"])  # Set column headers

    # Populate the model with data from the database
    for row in rows:
        items = [QStandardItem(str(value)) for value in row]
        model.appendRow(items)

    # Set the model for the QTableView
    table_view.setModel(model)

    # Close the database connection
    conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create the main application object
    win = QMainWindow()  # Create the main window
    ui = plant_data_ui.Ui_Form()  # Initialize the UI from .ui file
    ui.setupUi(win)  # Set up the UI elements in the main window

    # Load data into the QTableView after setting up the UI
    load_data_into_table(ui.tableView)  # Use 'tableView' from your UI file
    win.show()  # Show the main window

    # Execute the application
    sys.exit(app.exec_())