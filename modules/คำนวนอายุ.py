# คำนวนอายุจากวันเดือนปีเกิด
from datetime import datetime, date, timedelta
import time 

def calculate_age(birth_date):
    """คำนวนอายุจากวันเดือนปีเกิด"""
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

day =int(input("ป้อนวันเกิด (1-31): "))
month = int(input("ป้อนเดือนเกิด (1-12): "))
year = int(input("ป้อนปีเกิด (พ.ศ.): ")) - 543  # แปลง พ.ศ. เป็น ค.ศ.
birth_day = date(year, month, day)

age = calculate_age(birth_day)
print(f"อายุของคุณคือ {age} ปี")