income=int(input('enter gross income'))
dependent=int(input('enter number of dependent'))
taxable_income=income-10000-(3000*dependent)
tax=taxable_income*0.2
print(tax)
