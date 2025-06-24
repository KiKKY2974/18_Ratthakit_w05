# คำนวนภาษีคนที่ 1
salary = 13000
tax = 0.07
ot_time = 10
ot_rate = 200

gross_pay = salary + (ot_time * ot_rate)
tax_pay = gross_pay * tax
net_pay = gross_pay - tax_pay
print(f"จ่ายคนที่ 1 : {net_pay}")

def calculate_pay(salary, tax, ot_time, ot_rate):
    '''Calculate net pay after tax and overtime'''
    gross_pay = salary + (ot_time * ot_rate)
    tax_pay = gross_pay * tax
    net_pay = gross_pay - tax_pay
    return net_pay

emp_1 = calculate_pay(13000, 0.07, 10, 200)
print(f"จ่ายคนที่ 1 : {emp_1}")