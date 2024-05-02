# A python program to display the grades of students
def grade_student(student_mark):
# Handling invalid input
    if student_mark == int(student_mark):
        pass
    else:
            print('invalid input')
    if student_mark>=90 and student_mark<=100 and student_mark:
        print(f"Grade is A ")
    elif student_mark>=80 and student_mark<=89:
        print(f"Grade is B")
    elif student_mark>=70 and student_mark<=79:
        print(f"Grade is C ")
    elif student_mark>=60 and student_mark<=69:
        print(f"Grade is D ")
    elif student_mark>=50 and student_mark<=59:
        print(f"Grade is E ")
    else:
        print(f"Fail ")
    
grade_student(50)
grade_student(90)



# ii Converting temperatures to and from celcius to fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (9/5*celsius) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

celsius_to_fahrenheit(27)
fahrenheit_to_celsius(32)

# b i) Calculating the area of a triangle of base=2, height=3 
def calculate_triangle_area(base, height):
    return (1/2) * base * height
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = calculate_triangle_area(base, height)

# Print the result
print("The area of the triangle with base =", base, "and height =", height, "is", area)



# ii) 
def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Example usage:
numbers = [9, 2, 3, 5, 8]
result = sum_numbers(numbers)
print("Sum of the numbers in the list:", result)




    



