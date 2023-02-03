""""
    Healthy Times
"""
print("""
        Healthy Times
        Plans:
        
          MEMBERSHIP/PLAN      GOLD    DIAMOND     SILVER
          Type A                10%     15%         20%
          Type B                15%     20%         25%
          MEMBERSHIP_CODE        1       2           3
    """)

customer_name = input("Enter your Name: ")
membership_code = int(input("Enter your code"))
meal_plan = int(input("Select Meal Plan (Type-A/Type-B as 0/1):"))
days = int(input("How many day: "))

print()
print("Thank you for coming :)"
      "\nPlease wait for sec your bill is generating...")


def bill_generator(customer_name, membership_code, meal_plan, days):
    bill_amount = 0
    discount = 0
    payable_amount = 0

    if meal_plan == 0:
        bill_amount = days * 250
    else:
        bill_amount = days * 350

    if membership_code == 1 and meal_plan == 0:
        discount = bill_amount * 10 / 100
    elif membership_code == 1 and meal_plan == 1:
        discount = bill_amount * 15 / 100
    elif membership_code == 2 and meal_plan == 0:
        discount = bill_amount * 15 / 100
    elif membership_code == 2 and meal_plan == 1:
        discount = bill_amount * 20 / 100
    elif membership_code == 3 and meal_plan == 0:
        discount = bill_amount * 20 / 100
    elif membership_code == 3 and meal_plan == 1:
        discount = bill_amount * 25 / 100

    payable_amount = bill_amount - discount
    print(f"""
            ++++++++++++++++++++++++++++++
            Name: {customer_name}\t\tCode:{membership_code}
            Meal_Plan: {meal_plan} \t\tDays:{days}
            Total Amount: {bill_amount}\t\tDiscount: {discount}
            Payable Amount: {payable_amount}
            +++++++++++++++++++++++++++++++
                    Visit Again....
        """)


bill_generator(customer_name, membership_code, meal_plan, days)
