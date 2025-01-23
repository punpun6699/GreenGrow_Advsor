import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from GreenAdvisor_UI import plant_data_ui
import sqlite3  # For SQLite connection
from PyQt5.QtGui import QStandardItemModel, QStandardItem

def load_data_into_table(table_view, plant_id):
    """
    Load data into the QTableView for the specified plant_id.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect('/Users/panpom/PycharmProjects/GreenGrow_Advisor/Database/Main_data.db')  # Database path
    cursor = conn.cursor()

    try:
        # Fetch data for the specific plant_id from the plant_data table
        cursor.execute("SELECT * FROM plant_data WHERE Plant_id = ?", (plant_id,))
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

        if not rows:
            print(f"No data found for Plant_id: {plant_id}")

    except sqlite3.Error as e:
        print(f"Database error: {e}")

    finally:
        # Close the database connection
        conn.close()

def get_plant_data(plant_id):
    """
    Fetch data for the specified plant_ID from the database.
    """
    db_path = '/Users/panpom/PycharmProjects/GreenGrow_Advisor/Database/Main_data.db'  # Database path
    try:
        # Connect to the database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Query data for the specific plant_ID
        cursor.execute("SELECT * FROM Main_data WHERE plant_ID = ?", (plant_id,))
        plant_data = cursor.fetchone()

        # Check if data exists for the given plant_ID
        if plant_data:
            print(f"Data for plant_ID {plant_id}: {plant_data}")
            return plant_data
        else:
            print(f"No data found for plant_ID {plant_id}.")
            return None
    except sqlite3.Error as e:
        print(f"Error querying the database: {e}")
        return None
    finally:
        conn.close()

def main():
    # Check if plant_ID is provided as an argument
    if len(sys.argv) > 1:
        plant_id = sys.argv[1]
        print(f"Received plant_ID: {plant_id}")
        ui.plant_ID_textEdit.setText(str(plant_id))

        # Fetch and process data
        data = get_plant_data(plant_id)
        if data:
            # Example: process or display the data
            print(f"Fetched Data: {data}")
            ui.Name_textEdit.setText(str(data[2]))
            ui.Type_textEdit.setText(str(data[1]))
            ui.Age_textEdit.setText(str(data[3]))
        else:
            print("No data to display.")
        load_data_into_table(ui.tableView, plant_id)
    else:
        print("No plant_ID provided.")


def update_data():
    Name = str(ui.Name_textEdit.document().toPlainText())
    Type = str(ui.Type_textEdit.document().toPlainText())
    Age = int(ui.Age_textEdit.document().toPlainText())


if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create the main application object
    win = QMainWindow()  # Create the main window
    ui = plant_data_ui.Ui_Form()  # Initialize the UI from .ui file
    ui.setupUi(win)  # Set up the UI elements in the main window
    main()
    # Load data into the QTableView after setting up the UI
   # load_data_into_table(ui.tableView)  # Use 'tableView' from your UI file
    win.show()  # Show the main window

    # Execute the application
    sys.exit(app.exec_())