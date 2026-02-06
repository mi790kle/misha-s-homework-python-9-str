last_name: str = input("What is your last name? ")
first_name: str = input("What is your first name? ")
while True:
    country : str = input("What is your country? Use not more than 2 letters ")
    if country.isalpha() == True and len(country) < 3:
        break
    else:
        print("invalid country")
city_address : str = input("What is your city address? ")
while True:
    zipcode : str = input("What is your zipcode? Use only digits and more then 3 ")
    if zipcode.isdigit() == True and len(zipcode) > 3:
        break
    else:
        print("invalid zipcode")
print(f"FOR:{last_name.isupper()}, {first_name.islower()}")
print(f"COUNTRY:{country.isupper()} ")
print(f"CITY ADDRESS:{city_address}")
print(f"ZIPCODE:{zipcode}")