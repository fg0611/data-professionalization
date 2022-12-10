from datetime import date, datetime, timedelta


today = date.today()
# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")

print(today)
print(d1)

print(datetime(2022, 12, 6, 0, 10))
print(datetime.utcnow())