import phonenumbers
from phonenumbers import timezone,geocoder,carrier
num = input()
phone = phonenumbers.parse(num)
time = phonenumbers.timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone,"en")
reg = geocoder.description_for_number(phone,"en")
print(phone)
print(time)
print(car)
print(reg)

