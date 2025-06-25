from datetime import datetime, date, timedelta
import time 

# today = date.today()

# print(f"วันนี้ : {today}")
# print(f"วันที่ {today.day}")
# print(f"เดือน {today.month}")
# print(f"ปี {today.year}")

now = datetime.now()
print(now)
# print(f"เวลาปัจจุบัน : {now.hour}:{now.minute}:{now.second}")
# print(f"เวลาปัจจุบัน Hr:{now.hour}")
# print(f"เวลาปัจจุบัน Hr:{now.minute}")
# print(f"เวลาปัจจุบัน Hr:{now.second}")

# จัด fomat ว ด ป
formatted_date = now.strftime("%d/%m/%Y")
formatted_time = now.strftime("%H:%M:%S")
print(f"เวลาปัจจุบัน : {formatted_time}")
print(f"วัน/เดือน/ปี : {formatted_date}")


# คำนวนวันที่
tomorrow = now + timedelta(days=1)
print(f"วันพรุ่งนี้ : {tomorrow.strftime('%d/%m/%Y')}")
yesterday = now - timedelta(days=1)
print(f"เมื่อวานนี้ : {yesterday.strftime('%d/%m/%Y')}")
next_week = now + timedelta(weeks=1)
print(f"สัปดาห์หน้า : {next_week.strftime('%d/%m/%Y')}")
next_month = now + timedelta(days=30)
print(f"เดือนหน้า : {next_month.strftime('%d/%m/%Y')}")



# counter = 0
# counter += 1
# counter = counter + 1