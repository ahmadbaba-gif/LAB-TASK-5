#  Question #01 
print("=== Question 1 ===")
name = input("Enter name: ")
age = int(input("Enter age: "))
program = input("Enter program: ")
marks = float(input("Enter marks: "))

student = (name, age, program, marks)
print("Student tuple:", student)






#  Question #02 
print("\n=== Question 2 ===")
sentence = input("Enter a sentence: ")

characters = len(sentence)
words = len(sentence.split())
vowels = 0
spaces = 0
digits = 0

for ch in sentence:
    if ch.lower() in "aeiou":
        vowels += 1
    if ch == " ":
        spaces += 1
    if ch.isdigit():
        digits += 1

print("Number of characters:", characters)
print("Number of words:", words)
print("Number of vowels:", vowels)
print("Number of spaces:", spaces)
print("Number of digits:", digits)







# Question #03 
print("\n=== Question 3 ===")
employees = []

for i in range(3):
    print(f"\nEmployee {i + 1}")
    emp_name = input("Enter name: ")
    emp_age = int(input("Enter age: "))
    emp_salary = float(input("Enter salary: "))
    employees.append((emp_name, emp_age, emp_salary))

print("\nEmployees list:")
print(employees)








#  Question #04
print("\n=== Question 4 ===")
numbers = (10, 15, 20, 25, 30, 35, 40)

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
