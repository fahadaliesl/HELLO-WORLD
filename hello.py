
print("=== Leap Year Checker ===")
year = int(input("Please enter a year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"✅ {year} is a leap year!")
else:
    print(f"❌ {year} is not a leap year.")
    previous_leap_year = year - 1
    while not (previous_leap_year % 400 == 0 or (previous_leap_year % 4 == 0 and previous_leap_year % 100 != 0)):
        previous_leap_year -= 1

    next_leap_year = year + 1
    while not (next_leap_year % 400 == 0 or (next_leap_year % 4 == 0 and next_leap_year % 100 != 0)):
        next_leap_year += 1

    if year - previous_leap_year <= next_leap_year - year:
        print(f"The nearest leap year is {previous_leap_year}.")
    else:
        print(f"The nearest leap year is {next_leap_year}.")
