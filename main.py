from art import logo
print(logo)

def calculate_cookie_price(cookie_type, quantity):
    cookie_prices = {
        "chocolate chip": 3.00,
        "double chocolate": 3.50,
        "ginger snap": 3.50,
        "macarons": 4.00,
        "butter cookies": 2.00,
        "sugar cookies": 2.99,
        "peanut butter": 3.00,
    }

    if cookie_type.lower() in cookie_prices:
        price_per_cookie = cookie_prices[cookie_type.lower()]
        total_price = price_per_cookie * quantity
        return total_price

    else:
        return None

def main():
    print("Welcome to the Binary Bakery!")
    cookie_type = input("We have: \nChocolate Chip    $3.00\nDouble Chocolate  $3.50\nGinger Snap       $3.50\nMacarons          $4.00\nButter Cookies    $2.00\nSugar Cookies     $2.99\nPeanut Butter     $3.00\nWhat type of cookie would you like?: ")
    quantity = int(input("How many cookie packets would you like?: "))
    total_price = calculate_cookie_price(cookie_type, quantity)
    if total_price is not None:
        print(f"The total price for {quantity} {cookie_type} cookies is ${total_price:.2f}")
    else:
        print("Sorry, we don't have that type of cookie available.")
        return None

    payment = input("How much would you like to pay? Enter just a number:")
    if float(payment) > float(total_price):
        remaining_amount = (float(payment) - float(total_price))
        print(f"Here is your change: ${remaining_amount:.2f}")
        print("Thank you for purchasing!")
    else:
        print("Sorry, that's not enough.")

if __name__ == "__main__":
    main()
