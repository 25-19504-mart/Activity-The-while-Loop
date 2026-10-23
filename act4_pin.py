correct_pin = "0128"
attempts = 0

while attempts < 3:
    pin = input("PIN: ")

    if pin == correct_pin:
        print("Access granted")
        break
    else:
        attempts += 1

if attempts == 3:
    print("Card blocked")