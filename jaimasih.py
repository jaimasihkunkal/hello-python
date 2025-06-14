#Program 1: Print basic info
name = "Jaimasih"
age = 20
height = 5.8
is_student = True
print(name, age, height, is_student)
print("\n")
#Program 2: compare two number
a = 40
b = 20
if a > b:
    print("a is greater")
else:
    print("b is greater")
print("\n")
#Program 3: User input
user_name = input("Enter your name:")
print("Hello",user_name)
print("\n")
#Program 4: Print numbers from 1 to 5 using loop
for i in range(1,6):
    print("Numbers:",i)
print("\n")
#Program 5: User input even or odd
num = int(input("Enter a number:"))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")