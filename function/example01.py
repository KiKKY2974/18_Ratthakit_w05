# คำนวนภาษีคนที่ 1
salary = 13000
tax = 0.07
ot_time = 10
ot_rate = 200

gross_pay = salary + (ot_time * ot_rate)
tax_pay = gross_pay * tax
net_pay = gross_pay - tax_pay
print(f"จ่ายคนที่ 1 : {net_pay}")


# คำนวนภาษีคนที่ 2
salary_2 = 14000
tax_2 = 0.07
ot_time_2 = 10
ot_rate_2 = 200

gross_pay_2 = salary_2 + (ot_time * ot_rate)
tax_pay_2 = gross_pay_2 * tax
net_pay_2 = gross_pay_2 - tax_pay
print(f"จ่ายคนที่ 1 : {net_pay}")