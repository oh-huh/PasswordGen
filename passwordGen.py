import time
import random

def main():
    randomNumber = random.randint(99, 999)
    print("Hey! I am designed to generate a password for you.")
    print("I will ask you a series of questions to help decide your password")
    name = input("What is your name?\n")
    favColour = input("What is your favourite colour\n")
    favAnimal = input("What is your favourite animal\n")
    birthday = input("What was the date when you were born?(the number)\n")
    birthmonth = input("What month were you born? Enter in number format(01,02,03,04,05,06,07,08,09,10,11,12)\n")
    birthyear = input("What are the last two digits of the year you were born?\n")
    print("Wait for construction.....")
    time.sleep(3)
    passwordChoice = input("I have constructed two different passwords for you, which one with you like?(Enter 1 or 2)\n")

    if passwordChoice == "1":
        print(name.lower() + birthday + birthmonth + birthyear)
    elif passwordChoice == "2":
        print(favColour + favAnimal + randomNumber)

if __name__ == "__main__":
    main()
