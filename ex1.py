volume: int = int(input("Enter the volume: "))
match volume:
    case 1:
        print("Very quiet")
    case 2:
        print("Quiet")
    case 3 | 4:
        print("Low")
    case 5:
        print("Medium")
    case 6:
        print("Medium high")
    case 7:
        print("Loud")
    case 8:
        print("Very loud")
    case 9 | 10:
        print("Max volume")
    case _:
        print("Invalid number")