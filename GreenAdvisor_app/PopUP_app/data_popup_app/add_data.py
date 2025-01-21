import sys,subprocess,sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow
from GreenAdvisor_UI import add_data_ui
from PyQt5.QtGui import QStandardItemModel, QStandardItem

def calldata():
    # เชื่อมต่อฐานข้อมูล
    conn = sqlite3.connect('/Users/panpom/PycharmProjects/GreenGrow_Advisor/Database/Main_data.db')  # Database path
    cursor = conn.cursor()

    # ดึงค่า PK ล่าสุดจาก Main_data
    cursor.execute("SELECT MAX(plant_Id) FROM Main_data")  # เปลี่ยน pk_column_name เป็นชื่อคอลัมน์จริงของ PK
    latest_pk = cursor.fetchone()[0]

    # ตรวจสอบค่า PK ล่าสุดและเพิ่มค่าใหม่
    if latest_pk:
        # ตัดอักษร 'P_' และแปลงตัวเลขด้านหลังเป็น int
        latest_number = int(latest_pk.split('_')[1])
        # เพิ่มตัวเลขใหม่
        new_pk = f"P_{latest_number + 1:03d}"  # จัดรูปแบบเป็น 3 หลัก เช่น P_005
    else:
        # ถ้าไม่มีข้อมูล ให้เริ่มต้นที่ P_001
        new_pk = "P_001"

    print("New PK:", new_pk)
    ui.textEdit.setText(new_pk)
    # อย่าลืมปิดการเชื่อมต่อ
    cursor.close()
    conn.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create the main application object
    win = QMainWindow()  # Create the main window
    ui = add_data_ui.Ui_Form()  # Initialize the UI from .ui file
    ui.setupUi(win)  # Set up the UI elements in the main window
    calldata()
    # Load data into the QTableView after setting up the UI
    win.show()  # Show the main window

    # Execute the application
    sys.exit(app.exec_())