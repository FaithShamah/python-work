#1. The volume of a sphere with radius r is (4/3)* pie * r**2.
# What is the volume of the sphere with radius 5.
# Make sure the program enters the radius from the keyboard and provide the answer in 2 decimal places.

# radius = float(input("Enter the radius of the sphere: "))
# pie=22/7
# volume = (4/3)* pie * radius**2
# print(f"The volume of the sphere with radius {radius} is:{volume:.2f}")

##2. Create a program to calculate the area of a triangle (1/2 * base * height).
# Base and height should be entered using the keyboard.

# Base = float(input("Enter the base of the triangle: "))
# Height = float(input("Enter the height of the triangle: "))
# Area_of_a_triangle = (1/2 * Base * Height)
# print(f"The area of a triangle is:{Area_of_a_triangle}")


##3. WITI has tasked you to automate a simple grading system. 
# As a python student, write a program used  to display the grades that 
# the students will be receiving based on the mark scored in a subject. 
# The grades are:
# 90% - 100%  Grade is A
# 80% - 89%   Grade is  B
# 70% - 79%   Grade is C                                                        
# 60% - 69%   Grade is D                  
# 50% - 59%   Grade is E  
# < 50% Fail 
# def get_grade(score):
#     if 90 <= score <= 100:
#         return 'A'
#     elif 80 <= score < 90:
#         return 'B'
#     elif 70 <= score <80:
#         return 'C'
#     elif 60 <= score <70:
#         return'D'
#     elif 50 <= score <60:
#         return 'E'
#     else:
#         return 'Fail'
    
# def main():
#     try:
#         score=float(input("Enter the student's score (0-100): "))
#         if 0 <= score <= 100:
#             grade = get_grade(score)
#             print(f"The grade is: {grade}")
#         else:
#             print("Please enter a valid score between 0 and 100.")
#     except ValueError:
#         print("invalid input.Please enter a numeric score.")
# if __name__ == "__main__":
#     main()


##4. WITI Academy is proposing a Sacco to help students save their money. 
#  Design a platform that will do the following.
#  Welcome to, WITIAcademy Sacco.
#  1. Deposit Money
#  2. Withdraw Money
#  3. Check Balance
#  Ensure if the student selects 1, money is deposited and the minimum deposit should be 1000.
#  If the student selects 2, money should be withdrawn and a minimum withdrawal is 500.
#  If the student selects 3, the account balance should be displayed.

# class SaccoAccount:
#     def __init__(self):
#         self.balance = 0

#     def deposit(self, amount):
#         if amount < 1000:
#             return "Error: Minimum deposit is 1000."
#         self.balance += amount
#         return f"Deposit successful! New balance: {self.balance}"

#     def withdraw(self, amount):
#         if amount < 500:
#             return "Error: Minimum withdrawal is 500."
#         if amount > self.balance:
#             return "Error: Insufficient funds."
#         self.balance -= amount
#         return f"Withdrawal successful! New balance: {self.balance}"

#     def check_balance(self):
#         return f"Current balance: {self.balance}"


# def main():
#     account = SaccoAccount()
#     while True:
#         print("\nWelcome to WITI Academy Sacco!")
#         print("Please choose an option:")
#         print("1. Deposit Money")
#         print("2. Withdraw Money")
#         print("3. Check Balance")
#         print("4. Exit")

#         choice = input("Enter your choice (1-4): ")
#         if choice == '1':
#             try:
#                 amount = int(input("Enter amount to deposit: "))
#                 print(account.deposit(amount))
#             except ValueError:
#                 print("Error: Please enter a valid number.")
#         elif choice == '2':
#             try:
#                 amount = int(input("Enter amount to withdraw: "))
#                 print(account.withdraw(amount))
#             except ValueError:
#                 print("Error: Please enter a valid number.")
#         elif choice == '3':
#             print(account.check_balance())
#         elif choice == '4':
#             print("Thank you for using WITI Academy Sacco!")
#             break
#         else:
#             print("Invalid choice, please select again.")

# if __name__ == "__main__":
#     main()


