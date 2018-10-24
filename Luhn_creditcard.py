def Luhn(card_number):
    card_number = card_number.replace(" ", "")
    check = int(card_number[-1])
    new_card_number = []
    for idx, val in enumerate(card_number[:-1][::-1]):
        if idx % 2 == 0:
            val = int(val) * 2
            val = val if val < 9 else val - 9
            new_card_number.append(val)

        else:
            new_card_number.append(int(val))

    if (sum(new_card_number) + check) % 10 == 0:
        print("the card is OK")
        return True
    else:
        print("fail card!!!!!!!!!!")
        return (sum(new_card_number) + check) % 10


card = "4111 7555 3380 0642"
card = "1234 5678 9123 4567"
print(Luhn(card))
