import random

'''
print(f"{random.random()}") # สุ่มเลขทศนิยมระหว่าง 0 ถึง 1
print(f"{random.randint(1,99)}") # สุ่มเลขจำนวนเต็มระหว่าง 1 ถึง 99
print(f"{random.randrange(1, 100, 2)}") # สุ่มเลขจำนวนเต็มระหว่าง 1 ถึง 99 โดยมีช่วงห่าง 2
print(f"{random.uniform(1, 10):.4f}") # สุ่มเลขทศนิยมระหว่าง 1 ถึง 10
'''

clolors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']

random_list = random.choice(clolors)  # เลือกสีแบบสุ่มจากรายการ
random_3 = random.choices(clolors, k=3)  # เลือกสีแบบสุ่ม 3 สีจากรายการ
random_unique = random.sample(clolors, 3)  # เลือกสีแบบสุ่ม 3 สีจากรายการ โดยไม่ซ้ำกัน
print(f"สุ่มสีเดียว: {random_list}")
print(f"สุ่มสี 3 สี: {random_3}")
print(f"สุ่มสีแบบไม่ซ้ำกัน: {random_unique}")


numbers = list(range(1, 101))  # สร้างรายการเลข 1 ถึง 100
num_shuffle = random.shuffle(numbers)  # สุ่มเรียงลำดับรายการเลข
print(f"รายการเลขที่สุ่มเรียงลำดับ: {numbers}")
print(f"รายการเลขที่สุ่มเรียงลำดับ: {num_shuffle}")
print(f"รายการเลข 1 ถึง 100: {numbers}")
