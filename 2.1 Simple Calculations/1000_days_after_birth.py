from datetime import datetime, timedelta

birth_date = input()

birth_date_string = datetime.strptime(birth_date, "%d""-""%m""-""%Y") + timedelta(days=1000)

print(birth_date_string.strftime("%d-%m-%Y"))