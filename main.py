import sqlite3

# الاتصال بقاعدة البيانات (سيتم إنشاؤها إذا لم تكن موجودة)
conn = sqlite3.connect('clinic.db')
cursor = conn.cursor()

# إنشاء جدول المرضى
cursor.execute('''
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    history TEXT
)
''')

# حفظ التغييرات وإغلاق الاتصال
conn.commit()
conn.close()

print("تم إنشاء قاعدة البيانات وجدول المرضى بنجاح!")
  
