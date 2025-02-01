start_range = int(input("Enter the starting number of the range: "))
end_range = int(input("Enter the ending number of the range: "))

square_values = []

for num in range(start_range, end_range + 1):
    square_values.append(num ** 2)

print("Square values:", square_values)

odd_values = []
even_values = []

for value in square_values:
    if value % 2 == 0:
        even_values.append(value)
    else:
        odd_values.append(value)

print("Odd values:", odd_values)
print("Even values:", even_values)