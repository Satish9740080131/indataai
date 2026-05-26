"""
Create the MySQL database before running migrations.
Run from the project root: python scripts/create_db.py
"""
import MySQLdb

try:
    conn = MySQLdb.connect(host='localhost', user='root', passwd='root123', port=3306)
    cursor = conn.cursor()
    cursor.execute(
        "CREATE DATABASE IF NOT EXISTS indata_clone "
        "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
    )
    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Database 'indata_clone' created successfully!")
except Exception as e:
    print(f"❌ Error: {e}")
