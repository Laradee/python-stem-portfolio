**Name:** Lara Dee
**School:** Bishop's Stortford College  
**Course:** Python for STEM  
**Year:** Year 12, 2025-26

## About Me

I'm a year 12 student who is maintaining A*,A*,A,A and taking Maths, physics, further maths and DT. I hope to study Engineering at University, and I am intrested in bridges and space.

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
Game to guess numbers between 1 and 100, 
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
Code to View taks, add tasks, remove tasks, mark tasks as done, and to quit

**Code**
```python
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

def task_done(tasks):
    show_tasks(tasks)
    number = int(input("Enter task to mark as done: "))
    if 1 <= number <= len(tasks):
        tasks[number-1]= "Done: "+tasks[number-1]
        print(tasks[number-1])
    else:
        print("Invalid number.")

def main():
    tasks = []
    
    while True:
        print("=== To-Do List ===")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Mark as Done")
        print("5. Quit")
        
        choice = input("Choose: ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            task_done(tasks)
        else:
            print("Goodbye!")
            break

main()
```
## Student grade calculator

**Description**
Code to store students scores and allow new scores to be added

**Code**
```python
def get_grade(average):
    """Return a letter grade based on average percentage."""
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "U"

def get_valid_score(subject):
    """Ask for a score and keep asking until a valid number is entered."""
    while True:
        try:
            score = float(input(f"Enter score for {subject} (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a number.")
def calculate_results():
    """Collect scores and display results."""
    name = input("Student name: ")
    subjects = ["Maths", "English", "Science"]
    scores = {}
    
    for subject in subjects:
        scores[subject] = get_valid_score(subject)
    
    average = sum(scores.values()) / len(scores)
    grade = get_grade(average)
    
    print(f"\n=== Results for {name} ===")
    for subject, score in scores.items():
        print(f"  {subject}: {score:.1f}")
    print(f"Average: {average:.1f}%")
    print(f"Grade: {grade}")

while True:
    calculate_results()
    doagain = input("add another student(Y/N): ")
    if doagain =="Y":
        continue
    else: break

    
calculate_results()

def other_students():
    """add other students to list."""
    students = input("would you like to add another student: ")
    if students == 'yes':
        calucate_results()
```

## OPP Bank

**Description**
Code to create account holder, enter funds and impliment intrest

**Code**
```python
def __init__(self, owner, initial_balance=0):
    """Set up the account with an owner name and starting balance."""
    self.owner = owner
    self.balance = initial_balance
    self.transactions = []

def deposit(self, amount):
    """Add money to the account."""
    if amount > 0:
        self.balance += amount
        self.transactions.append(f"Deposit: +£{amount:.2f}")
        print(f"Deposited £{amount:.2f}. New balance: £{self.balance:.2f}")
    else:
        print("Deposit amount must be positive.")

def withdraw(self, amount):
    """Remove money from the account if funds are available."""
    if amount <= 0:
        print("Withdrawal amount must be positive.")
    elif amount > self.balance:
        print(f"Insufficient funds. Balance is only £{self.balance:.2f}")
    else:
        self.balance -= amount
        self.transactions.append(f"Withdrawal: -£{amount:.2f}")
        print(f"Withdrew £{amount:.2f}. New balance: £{self.balance:.2f}")

def show_balance(self):
    """Display the current balance."""
    print(f"\nAccount holder: {self.owner}")
    print(f"Current balance: £{self.balance:.2f}")

def GetBalance(self):
    return self.balance

def show_history(self):
    """Display all transactions."""
    print(f"\n=== Transaction History for {self.owner} ===")
    for t in self.transactions:
        print(f"  {t}")
    print(f"  Current balance: £{self.balance:.2f}")

#I noticed you have written def instead of class      
class SavingsAccount(BankAccount):
# we need to add a constructor so the rate can be added
def __init__(self, owner, initial_balance=0, rate =0.0):
    super().__init__(owner, initial_balance) # calls the contructor of the parent class i.e. BankAccount
    #set the rate
    self.rate = rate

def apply_interest(self):
    interest = self.balance * self.rate
    self.balance = self.balance + interest
    self.transactions.append(f"Interest ({self.rate:.1%}): +£{interest:.2f}")
    print(f"Interest applied: +£{interest:.2f}. New balance: £{self.balance:.2f}")

#added a little helper to ensure that user enters a number before proceeding
def validateInput(prompt):
'''Keep asking until the user enters a valid number.'''
while True:
    try:
        return float(input(prompt))
    except ValueError:
        print("Please enter a floating point number")

# --- Using the class ---
def main():
name = input("Enter account holder name: ")
opening = validateInput("Enter opening balance: £")
rate = validateInput('Enter annual Interest rate (e.g. 0.03 for 3%): ')

#We create one object - a saving account is a type of bank account
account = SavingsAccount(name, opening, rate)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. View history")
    print("5. Apply Interest")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        amount = float(input("Amount to deposit: £"))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("Amount to withdraw: £"))
        account.withdraw(amount)
    elif choice == "3":
        account.show_balance()
    elif choice == "4":
        account.show_history()
    elif choice =="5":
        account.apply_interest()
    elif choice == "6":
        print("Thank you for banking with us.")
        break
    else:
        print("Invalid choice.  Please pick 1-6")
```

 ## Student Records database

**Description**
Code to view, add and search for students scores

**Code**
```python 
import sqlite3

def create_database():
    """Create the database and table if they don't exist."""
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            score REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_student(name, score):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, score) VALUES (?, ?)", (name, score))
    conn.commit()
    conn.close()
    print(f"Added {name} with score {score}.")

def view_all_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, score FROM students ORDER BY score DESC")
    rows = cursor.fetchall()
    conn.close()
    
    if not rows:
        print("No records found.")
        return
    print("\n=== All Students ===")
    print(f"{'ID':<5} {'Name':<20} {'Score':<10}")
    print("-" * 35)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<20} {row[2]:<10}")

def search_student(name):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name LIKE ?", (f"%{name}%",))
    results = cursor.fetchall()
    conn.close()
    
    if not results:
        print(f"No student found with name '{name}'.")
    else:
        for r in results:
            print(f"ID: {r[0]}, Name: {r[1]}, Score: {r[2]}")

def main():
    create_database()
    
    while True:
        print("\n=== Student Records ===")
        print("1. View all  2. Add student  3. Search  4. Exit")
        choice = input("Choose: ")
        
        if choice == "1":
            view_all_students()
        elif choice == "2":
            name = input("Name: ")
            score = float(input("Score: "))
            add_student(name, score)
        elif choice == "3":
            name = input("Search name: ")
            search_student(name)
        elif choice == "4":
            break

main()
```  


