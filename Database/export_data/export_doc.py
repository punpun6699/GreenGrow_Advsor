import sqlite3
import pandas as pd

# 🔹 กำหนดเส้นทางไฟล์ Excel และฐานข้อมูล
excel_path = "/Users/panpom/PycharmProjects/GreenGrow_Advisor/Database/export_data/Book2_translated.xlsx"
db_path = "/Users/panpom/PycharmProjects/GreenGrow_Advisor/Database/Main_data.db"

# 🔹 อ่านข้อมูลจาก Excel
df = pd.read_excel(excel_path)

# 🔹 เชื่อมต่อฐานข้อมูล SQLite
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 🔹 กำหนดชื่อตารางในฐานข้อมูล
table_name = "docter_en"  # เปลี่ยนเป็นชื่อตารางที่ต้องการ

# 🔹 บันทึกข้อมูลลง SQLite
df.to_sql(table_name, conn, if_exists="replace", index=False)

# 🔹 ตรวจสอบว่าข้อมูลถูกบันทึกลงไปแล้ว
cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
count = cursor.fetchone()[0]
print(f"🎉 Data from '{excel_path}' has been saved to table '{table_name}' with {count} rows.")

# 🔹 ปิดการเชื่อมต่อ
conn.close()
