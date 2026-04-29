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