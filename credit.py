from sys import exit

AmericanExpress = ['34', '37']
MasterCard = ['51', '52', '53', '54', '55']
Visa = '4'
valid_len = [15, 16, 13, 16]


def main():
    number = get_number()
    valid = valid_card(number)
    card = type_card(number)

    if valid:
        print(card)
    else:
        print('Invalid')


def get_number():
    while True:
        try:
            number = input("Number: ")
            if len(number) in valid_len:
                break
            else:
                print("Invalid")
                exit(1)
        except:
            print(f"INVALID")
            exit(1)
    return number


def valid_card(number):
    sum_double = 0
    sum_one = 0
    lista = list(number)
    array = lista[::-1]

    sum_double = sum((int(x) * 2 // 10) + (int(x) * 2 % 10) for x in array[1::2])
    sum_one = sum(int(x) for x in array[0::2])
    total = sum_double + sum_one
        
    if total % 10 == 0:
        return True
    else:
        return False
        

def type_card(number):
    visa = "VISA"
    mastercard = "MASTERCARD"
    amex = "AMEX"
    if len(number) == 16:
        for start in MasterCard:
            if number.startswith(start):
                return mastercard
    
    if len(number) == 15:
        for start in AmericanExpress:
            if number.startswith(start):
                return amex
    
    if len(number) == 13 or len(number) == 16:
        for start in Visa:
            if number.startswith(start):
                return visa
                
    return "Invalid"


main()