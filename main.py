import sqlite3

# 1. إعداد قاعدة البيانات والجدول
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
conn.commit()

# 2. تعريف الدوال
def add_patient(name, age, history):
    cursor.execute('INSERT INTO patients (name, age, history) VALUES (?, ?, ?)', (name, age, history))
    conn.commit()
    print(f"\nتمت إضافة المريض: {name} بنجاح!")

def search_patient(name):
    cursor.execute('SELECT * FROM patients WHERE name = ?', (name,))
    patient = cursor.fetchone()
    if patient:
        print(f"\n--- تم العثور على المريض ---")
        print(f"ID: {patient[0]} | الاسم: {patient[1]} | العمر: {patient[2]} | الحالة: {patient[3]}")
    else:
        print(f"\nعذراً، لم يتم العثور على مريض باسم: {name}")

# 3. الجزء التفاعلي (يطلب المدخلات من المستخدم)
print("\n--- مرحباً بك في نظام العيادة ---")
name_input = input("أدخل اسم المريض: ")
age_input = input("أدخل عمر المريض: ")
history_input = input("أدخل التاريخ المرضي: ")

# استدعاء الدوال بناءً على مدخلاتك
add_patient(name_input, int(age_input), history_input)
search_patient(name_input)

# إغلاق الاتصال
conn.close()
