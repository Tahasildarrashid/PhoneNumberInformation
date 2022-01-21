import phonenumbers
from phonenumbers import geocoder, carrier

mobileno = input("Ënter your mobilenumber with country code: ")

mobileno = phonenumbers.parse(mobileno)

print(carrier.name_for_number(mobileno, 'en'))

print(geocoder.description_for_number(mobileno, "en"))

print("Valid phone number: ",phonenumbers.is_valid_number(mobileno))
