minutes_weekend = float(input("you can enter the number of weekend minutes: "))
minutes_weekday = float(input("you can enter the number of weekday minutes: "))
minutes_night = float(input("you can enter the number of minute on night (8 pm - 7 am): "))

total_minutes = minutes_weekday + minutes_weekend + minutes_night
before_tax = 39.99

if minutes_weekday < 600:
    cost1 = float("{:.2f}".format(total_minutes / before_tax))
    after_tax = float("{:.2f}".format(before_tax * 0.0525))
    bill = float("{:.2f}".format(before_tax + after_tax))

else:
    additionsl_minutes = minutes_weekday % 600
    before_tax = float("{:.2f}".format(39.99 + (additionsl_minutes * 0.40)))
    cost2 = float("{:.2f}".format(total_minutes / before_tax))
    after_tax = float("{:.2f}".format(before_tax * 0.0525))
    bill = float("{:.2f}".format(before_tax + after_tax))


print(f"you're bill before tax is ${before_tax}")
print(f"total minutes you spend is cost {total_minutes}")
print(f"amount of tax ${bill}")
print(f"amount of bill ${bill}")