# 1
# try:
#     user_name = input("Enter your name: ")
#     user_salary = int(input("Enter your desired salary level: "))
#
#     tax_level = user_salary*0.2
#
#     print(f"{user_name},the tax level you will pay with the salary {user_salary} is {tax_level}")
#
# except ValueError:
#     print(f"{user_name},please enter your desired salary as a digit.")


# 2
# def add(a, b):
#     return a+b
#
#
# def multiply(a, b):
#     return a*b
#
#
# def division(a, b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         print("This is mistake")
#
#
# def exponentiation(a, b):
#     return a**b
#
#
# try:
#     print("Please chose the task you want to perform:")
#     print("1.	Addition")
#     print("2.	Multiplication")
#     print("3.	Division")
#     print("4.	Exponentiation")
#
#     operation = int(input())
#
#     print("Please enter two numbers for addition, comma separated")
#     user_first_num = float(input("Enter your first number: "))
#     user_second_num = float(input("Enter your second number: "))
#
#     if operation == 1:
#         result = add(user_first_num, user_second_num)
#         print(result)
#     elif operation == 2:
#         result = multiply(user_first_num, user_second_num)
#         print(result)
#     elif operation == 3:
#         result = division(user_first_num, user_second_num)
#         print(result)
#     elif operation == 4:
#         result = exponentiation(user_first_num, user_second_num)
#         print(result)
#     else:
#         print("Please, choice showed operations")
#
# except ValueError:
#     print("Please enter a number")


# 3
# length = int(input("Please enter the length of Fibonacci sequence: "))
#
# fibonacci_sequence = []
# x, y = 1, 1
#
# while length > 0:
#     fibonacci_sequence.append(x)
#     x, y = y, x + y
#     length -= 1
#
# print(fibonacci_sequence)

# # 4
# try:
#     print("Please chose the task you want to perform: 1.Enter items,   2.Exit")
#     user_input = int(input())
#
#     if user_input == 1:
#         print("Please enter items separated by comma")
#
#     elif user_input == 2:
#         print("You left")
#
# except ValueError:
#     print("Please enter a number")


# 5
# empty_list = []
# complete_list = []
#
#
# def add(task):
#     return empty_list.append(task)
#
#
#
# def view():
#     return empty_list
#
#
# def mark(task):
#     return complete_list.append(task)
#
#
#
# def view_complete():
#     return complete_list
#
#
# try:
#     print("Please chose the task you want to perform:")
#     print("1.Add Task")
#     print("2.View All Tasks")
#     print("3.Mark Task as Completed")
#     print("4.View All Completed Tasks")
#     print("5.Exit")
#
#     user_choice = input()
#
#     print("Enter the name of the task: ")
#     user_task = input()
#
#     if user_choice == 1:
#         print(f"The task {user_task} was added to the todo list")
#     elif user_choice == 2:
#
#
# except ValueError:
#     print("Please enter a number")
