from termcolor import colored
print("Welcome to my BMI calculator.")
print("Let's check your health.")

while True:
    while True:
        try:
          user_input = float(input("Enter your weight (kg): "))
          break
        except ValueError:
           print("Invalid input!")
    while True:
       try:  
        user_input1 = float(input("Enter your height (m): "))
        break
       except ValueError:
          print("Invalid input!")
    bmi = user_input / user_input1**2
    if bmi < 18.5:
       print(f"Your bmi is: {bmi:.2f}")
       print("Under weight (need to gain weight) 🏋🏻‍♀️")
    elif bmi < 24.9:
       print(colored(f"Your bmi is: {bmi:.2f}", "green"))
       print("Normal weight (healthy) 🥦")
    elif bmi < 29.9:
       print(f"Your bmi is: {bmi:.2f}")
       print("Over weight (need to lose weight) ❤️‍🔥")
    else:
       print(colored(f"Your bmi is: {bmi:.2f}", "red"))
       print("Obesity! (life in danger ☠️)")

    ask_user = input("Do you want to calculate again? (yes/no) ")
    if ask_user.lower().strip() != "yes":
       print("Have a nice day.")
       break

