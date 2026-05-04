**Name:** Lara Dee
**School:** Bishop's Stortford College  
**Course:** Python for STEM  
**Year:** Year 12, 2025-26

## About Me

I'm a year 12 student who is maintaining A*,A*,A and taking Maths, Further Maths, physics and DT. I hope to study Engineering at University, and I am intrested in bridges and space.

## Course Overview

This portfolio documents my progress through a Python programming course designed for students preparing for STEM pathways at university. The course covers:

- Python fundamentals (variables, input/output, data types)
- Control structures (loops and conditionals)
- Functions and modular code
- Data structures (lists, dictionaries, tuples, sets)
- Validation and error handling
- File handling
- Object-Oriented Programming (OOP)
- Version control with Git and GitHub
- Working with Jupyter Notebooks

## Portfolio Projects

| # | Project | Key Skills | Status |
|---|---|---|---|
| 1 | [Unit Converter](#unit-converter) | Variables, functions, input/output | ✅ Complete |
| 2 | [Number Guessing Game](#guessing-number-game) | Loops, conditionals, random | ✅ Complete |
| 3 | [To-Do List](#to-do-list) | Lists, functions, data structures | ✅ Complete |
| 4 | [Student Grade Calculator](#) | Dictionaries, validation, error handling | ✅ Complete |
| 5 | [OOP Bank Account](#) | Classes, OOP principles | ✅ Complete |
| 6 | [Data Analysis Notebook](#) | Jupyter Notebooks, data exploration | ✅ Complete |

## Skills I Have Developed

**Programming Concepts**
- Writing clean, well-commented Python code
- Using functions to organise and reuse code
- Handling user input safely with validation

**Tools and Technologies**
- Python 3 (Thonny IDE)
- Jupyter Notebooks
- Git version control
- GitHub for code sharing and portfolio management
- Markdown for documentation

## Contact

- **GitHub:** Laradee
- **Email:** 26deel@bscmail.org

# Projects

## Unit converter

**Description**

I made this unit converter which can convert kilometers to miles, miles to kilometers, Celcius to Fahrenheit, and Fahrenheit to degrees. This was quite a simple code as only required some calculations and basic code.

**Code**

```python
def km_to_miles(km):
    """Convert kilometres to miles."""
    miles = km * 0.621371
    return miles

def miles_to_km(miles):
    """Convert miles to kilometres."""
    km = miles / 0.621371
    return km

def cel_to_fan(cel):
    """convert Celsius to Fahrenheit"""
    fan = cel * 3.38
    return fan

def fan_to_cel(fan):
    """convert Fahrenheit to Celsius"""
    cel = fan / 3.38
    return cel

def show_menu():
    print("=== Unit Converter ===")
    print("1. Kilometres to Miles")
    print("2. Miles to Kilometres")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")

def main():
    show_menu()
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        km = float(input("Enter kilometres: "))
        result = km_to_miles(km)
        print(f"{km} km = {result:.2f} miles")
    elif choice == "2":
        miles = float(input("Enter miles: "))
        result = miles_to_km(miles)
        print(f"{miles} miles = {result:.2f} km")
    elif choice == "3":
        cel = float(input("Enter Celsius: "))
        result = cel_to_fan(cel)
        print(f"{cel} celsius = {result:.2f} fahrenheit")
    elif choice == "4":
        fan = float(input("Enter Fahrenheit: "))
        result = fan_to_cel(fan)
        print(f"{fan} fahrenheit = {result:.2f} celsius")
        
main()
```

**Output**
screenshot
## Guessing number game

**Description**

**Code**
```python
import random

highScore = 100000

def play_game(highScore):
    """Play one round of the guessing game."""
    secret = random.randint(1, 100)
    attempts = 0
    
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        guess = int(input("Your guess: "))
        attempts += 1
        
        if guess < secret:
            print("Too low! Try again.")
        elif guess > secret:
            print("Too high! Try again.")
        else:
            print(f"Correct! You got it in {attempts} attempts.")
            break  # Exit the loop

    if highScore > attempts:
        highScore = attempts
    choice = input("Would you like to play again: ")
    if choice == "yes":
        play_game(highScore)
    else:
        print("okay, high score: ", highScore)
        
play_game(highScore)
```
screenshot
## To do list

**Description**

**Code**
```phython
def show_tasks(tasks):
    """Display all tasks with their numbers."""
    if len(tasks) == 0:
        print("No tasks yet!")
        return
    
    print("\n=== Your Tasks ===")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()

def add_task(tasks):
    """Add a new task to the list."""
    new_task = input("Enter task: ")
    tasks.append(new_task)
    print(f"Added: '{new_task}'")
    

def remove_task(tasks):
    """Remove a task by number."""
    show_tasks(tasks)
    number = int(input("Enter task number to remove: "))
    if 1 <= number <= len(tasks):
        removed = tasks.pop(number - 1)
        print(f"Removed: '{removed}'")
    else:
        print("Invalid number.")

def main():
    tasks = []
    
    while True:
        print("=== To-Do List ===")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Quit")
        
        choice = input("Choose: ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break

main()
```