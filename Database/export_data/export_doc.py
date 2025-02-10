import sqlite3
import pandas as pd

# 🔹 กำหนดเส้นทางไฟล์ Excel และฐานข้อมูล
excel_path_user = str(input("Excel path >>> "))
excel_path = f"/Users/panpom/PycharmProjects/GreenGrow_Advisor/Database/export_data/{excel_path_user}.xlsx"
db_path = "/Users/panpom/PycharmProjects/GreenGrow_Advisor/Database/Main_data.db"

# 🔹 อ่านข้อมูลจาก Excel
df = pd.read_excel(excel_path)

# 🔹 เชื่อมต่อฐานข้อมูล SQLite
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 🔹 กำหนดชื่อตารางในฐานข้อมูล
table_name = str(input("Table name >>> ")).strip()  # ลบช่องว่างส่วนเกินออก

# 🔹 ตรวจสอบว่าตารางมีอยู่หรือไม่
cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
table_exists = cursor.fetchone()

if table_exists:
    confirm = input(f"⚠️ Table '{table_name}' already exists. Do you want to delete it? (y/n) >>> ").strip().lower()
    if confirm == 'y':
        print(f"🗑️ Deleting table '{table_name}'...")
        cursor.execute(f"DROP TABLE {table_name}")
        conn.commit()
    else:
        print("❌ Operation cancelled. No data was modified.")
        conn.close()
        exit()

# 🔹 บันทึกข้อมูลลง SQLite
df.to_sql(table_name, conn, if_exists="replace", index=False)

# 🔹 ตรวจสอบว่าข้อมูลถูกบันทึกลงไปแล้ว
cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
count = cursor.fetchone()[0]
print(f"🎉 Data from '{excel_path}' has been saved to table '{table_name}' with {count} rows.")

# 🔹 ปิดการเชื่อมต่อ
conn.close()