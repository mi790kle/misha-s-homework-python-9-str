time_in_minutes: int = int(input("For how long have ypu beem waiting for your meal in minutes: "))
price_in_shekels: int = int(input("How much did you pay in shekels: "))
is_quick_service: bool = time_in_minutes < 15
is_expensive: bool = price_in_shekels > 100
if is_quick_service and not is_expensive:
    print("Recommended")
else:
    print("Not recommended")