import sqlite3

conn = sqlite3.connect('clinic.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    history TEXT
)
''')

def add_patient(name, age, history):
    cursor.execute('INSERT INTO patients (name, age, history) VALUES (?, ?, ?)', (name, age, history))
    conn.commit()
    print(f"\nتمت إضافة المريض: {name} بنجاح!")

def search_patient(name):
    cursor.execute('SELECT * FROM patients WHERE name = ?', (name,))
    patient = cursor.fetchone()
    if patient:
        print(f"\n--- المريض تم العثور عليه ---")
        print(f"ID: {patient[0]} | الاسم: {patient[1]} | العمر: {patient[2]} | التاريخ: {patient[3]}")
    else:
        print(f"\nعذراً، لم يتم العثور على مريض باسم: {name}")
import sqlite3

conn = sqlite3.connect('clinic.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    history TEXT
)
''')

def add_patient(name, age, history):
    cursor.execute('INSERT INTO patients (name, age, history) VALUES (?, ?, ?)', (name, age, history))
    conn.commit()
    print(f"\nتمت إضافة المريض: {name} بنجاح!")

def search_patient(name):
    cursor.execute('SELECT * FROM patients WHERE name = ?', (name,))
    patient = cursor.fetchone()
    if patient:
        print(f"\n--- تم العثور عليه ---")
        print(f"ID: {patient[0]} | الاسم: {patient[1]} | العمر: {patient[2]} | الحالة: {patient[3]}")
    else:
        print(f"\nعذراً، لم يتم العثور على مريض باسم {name}")

# هنا يبدأ الجزء التفاعلي
print("\n--- نظام إضافة مريض جديد ---")
name = input("أدخل اسم المريض: ")
age = input("أدخل عمر المريض: ")
history = input("أدخل ما يعاني منه المريض: ")

# إضافة المريض وحفظه
add_patient(name, int(age), history)

# البحث عن المريض للتأكد من إضافته
search_patient(name)

# إغلاق الاتصال
conn.close()
print("\nتمت العمليات بنجاح.")

