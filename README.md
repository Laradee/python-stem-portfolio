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
| 2 | [Number Guessing Game](game.py) | Loops, conditionals, random | ✅ Complete |
| 3 | [To-Do List](todolist.py) | Lists, functions, data structures | ✅ Complete |
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
        
main()```




