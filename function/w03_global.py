counter = 0

def increment_counter():
    """เพิ่มค่า counter ทีละ 1"""
    global counter
    counter += 1
    print(f"Counter : {counter}")
    
def reset_counter():
    """รีเซ็ตค่า counter เป็น 0"""
    global counter
    counter = 0
    print("Counter reset to 0")
    
increment_counter() 
increment_counter()
increment_counter()
reset_counter()
increment_counter()