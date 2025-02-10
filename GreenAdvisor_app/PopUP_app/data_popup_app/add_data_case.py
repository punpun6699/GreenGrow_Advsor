import sys,sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow
from GreenAdvisor_UI import Add_data_case_ui
from PyQt5 import  QtCore
def exit_with_code():
    app.exit(0)  # Exit with status code 0
def calldata():
    # เชื่อมต่อฐานข้อมูล
    conn = sqlite3.connect('/Users/panpom/PycharmProjects/GreenGrow_Advisor/Database/Main_data.db')  # Database path
    cursor = conn.cursor()

    # ดึงค่า PK ล่าสุดจาก Main_data
    cursor.execute("SELECT MAX(case_id) FROM plant_data")  # เปลี่ยน pk_column_name เป็นชื่อคอลัมน์จริงของ PK
    latest_pk = cursor.fetchone()[0]

    # ตรวจสอบค่า PK ล่าสุดและเพิ่มค่าใหม่
    if latest_pk:
        # ตัดอักษร 'c_' และแปลงตัวเลขด้านหลังเป็น int
        latest_number = int(latest_pk.split('_')[1])
        # เพิ่มตัวเลขใหม่
        new_pk = f"c_{latest_number + 1:03d}"  # จัดรูปแบบเป็น 3 หลัก เช่น P_005
    else:
        # ถ้าไม่มีข้อมูล ให้เริ่มต้นที่ P_001
        new_pk = "c_001"

    print("New PK:", new_pk)
    ui.case_id_textEdit.setText(new_pk)
    # อย่าลืมปิดการเชื่อมต่อ
    cursor.close()
    conn.close()
def Add_data():
    try:
        # เชื่อมต่อฐานข้อมูล
        conn = sqlite3.connect('/Users/panpom/PycharmProjects/GreenGrow_Advisor/Database/Main_data.db')
        cursor = conn.cursor()

        # ดึงค่าจาก UI
        case = str(ui.case_id_textEdit.document().toPlainText())
        Type = str(ui.Type_textEdit.document().toPlainText())
        plant_id = str(ui.plant_id_textEdit.document().toPlainText())
        info = str(ui.info_textEdit.document().toPlainText())

        # เตรียมข้อมูลสำหรับเพิ่มในตาราง
        new_data = [(case, Type, plant_id, info)]
        print("New Data:", new_data)

        # เพิ่มข้อมูลลงใน Main_data
        cursor.executemany("INSERT INTO plant_data VALUES (?, ?, ?, ?)", new_data)
        conn.commit()  # บันทึกการเปลี่ยนแปลง

        # ดึงข้อมูลทั้งหมดในตารางเพื่อแสดงผล
        cursor.execute("SELECT * FROM plant_data")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        ui.Log.setText(str("Update success."))
        calldata()

    except sqlite3.IntegrityError as e:
        print("Database Integrity Error:", e)
        ui.Log.setText(str(f"Database Integrity Error: {e}"))
    except sqlite3.OperationalError as e:
        print("Operational Error:", e)
        ui.Log.setText(str(f"Operational Error: {e}"))
    except ValueError as e:
        print("Value Error (e.g., invalid age):", e)
        ui.Log.setText(str(f"Value Error (e.g., invalid age): {e}"))
    except Exception as e:
        print("Unexpected Error:", e)
        ui.Log.setText(str(f"Unexpected Error: {e}"))
    finally:
        # ปิดการเชื่อมต่อกับฐานข้อมูล
        if 'conn' in locals() and conn:
            conn.close()
            print("Connection closed.")
            clear(0)

def clear(x):
    ui.info_textEdit.setText("")
    ui.Type_textEdit.setText("")
    if x == 1:
        ui.Log.setText("")
        ui.plant_id_textEdit.setText("")
def clear_bt():
    clear(1);calldata()
def main():
    if len(sys.argv) > 2:
        case_type = sys.argv[1]
        plant_id = sys.argv[2]
        print(f"Received case_type: {case_type}, plant_ID: {plant_id}")
        ui.plant_id_textEdit.setText(str(plant_id))
        ui.Type_textEdit.setText(str(case_type))
    else:
        print("Insufficient arguments provided.")

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create the main application object
    win = QMainWindow()  # Create the main window
    ui = Add_data_case_ui.Ui_Form()  # Initialize the UI from .ui file
    ui.setupUi(win)  # Set up the UI elements in the main window

    win.setWindowFlags(QtCore.Qt.WindowType.Window |
                       QtCore.Qt.WindowType.CustomizeWindowHint |
                       QtCore.Qt.WindowType.WindowCloseButtonHint |
                       QtCore.Qt.WindowType.WindowMinimizeButtonHint)

    calldata()
    main()
    # Load data into the QTableView after setting up the UI
    win.show()  # Show the main window
    ui.Add_pushButton.clicked.connect(Add_data)
    ui.Cls_pushButton.clicked.connect(clear_bt)
    ui.pushButton_3.clicked.connect(exit_with_code)
    # Execute the application
    sys.exit(app.exec_())