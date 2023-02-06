n = input("Enter three digit value: ")
n = int(n)

first_value = n % 10
second_value = n % 100 // 10
third_value = n // 100

print("The sum of entered values:", first_value + second_value + third_value)