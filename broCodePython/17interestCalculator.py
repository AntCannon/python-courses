import math

principle = 1000
rate = 5
time = 5

while principle <= 0:
  principle = float(input("Enter the principle amount: "))
  if principle <= 0:
    print(f"You entered {principle}. Principle must be greater than 0.")
  else:
    print(f"You entered ${principle:.2f}.")

while time <= 0:
  time = float(input("Enter the time in years: "))
  if time <= 0:
    print(f"You entered {time}. Time must be greater than 0.")
  else:
    print(f"You entered {time} years.")

while rate <= 0:
  rate = float(input("Enter the percentage rate: "))
  if rate <= 0:
    print(f"You entered {rate:.2f}%. Rate must be greater than 0.")
  else:
    print(f"You entered {rate}%.")

interest = principle * math.pow((1 + rate / 100), time) - principle
interestDisplay = f"${interest:.2f}"
balance = principle + interest
balanceDisplay = f"${balance:.2f}"

print(f"After {time} year{'' if time == 1 else 's'}:")
print(f"You wil have earned {interestDisplay}")
print(f"Your balance would be {balanceDisplay}")