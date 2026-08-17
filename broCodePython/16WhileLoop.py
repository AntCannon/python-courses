name = input("Enter your name: ")

while not name:
  print("Please enter a name!")
  name = input("Enter your name: ")

print(f"Hello {name}!")