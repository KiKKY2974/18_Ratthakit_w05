# รับ Parameter 
'''def ชื่อฟังก์ชัน(พารามิเตอร์):
    พารามิเตอร์1 + พารามิเตอร์2 = xxx
'''
def get_name(name):
    '''Show name from parameter'''
    print(f"Hello !!! : {name}")


def add_number(a,b):
    '''ฟังก์ชันบวกเลข'''
    result = a + b
    return result

a = int(input(f"Enter first number: "))
b = int(input(f"Enter second number: "))
sum = add_number(a, b)
print(f" result : {sum}")



def recr_cal(width, height):
    '''ฟังก์ชันคำนวณพื้นที่สี่เหลี่ยมผืนผ้าและเส้นกรอบ'''
    area = width * height
    frame = 2 * (width + height)
    return area, frame

width = 3
height = 10

area, frame = recr_cal(width, height) 
print(f"พื้นที่สี่เหลี่ยม =  {area}  เส้นกรอบ =  {frame}")