"""
Kullanıcıdan doğum tarihin alan ona yaşını döndüren ve bir sonraki yaşına
kaç kadar gün kaldığını söyleyen bir kod yazın
"""
from datetime import datetime

birth_date_str = input("Lütfen doğum tarihinizi (DD/MM/YYYY formatında) girin: ")
birth_date = datetime.strptime(birth_date_str, "%d/%m/%Y")
now = datetime.now()
age = now.year - birth_date.year

if now.month < birth_date.month or (now.month == birth_date.month and now.day < birth_date.day):
  age -= 1
if now.month == birth_date.month and now.day == birth_date.day:
  print(f"Bugün doğum gününüz! {age} yaşındasınız.")
else:
  next_birthday = birth_date.replace(year=now.year)
  if next_birthday < now:
    next_birthday = next_birthday.replace(year=now.year + 1)
  days_until_next_birthday = (next_birthday - now).days
  print(f"{age} yaşındasınız ve bir sonraki doğum gününüze {days_until_next_birthday} gün kaldı.")
