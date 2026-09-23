# ==========================================
#       TEMPERATURE CONVERTER
#       Cognifyz Technologies - Task 4
# ==========================================


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def temperature_converter():

    print("\n==========================================")
    print("          TEMPERATURE CONVERTER")
    print("==========================================")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")
    print("==========================================")

    while True:

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":

            try:
                celsius = float(input("Enter temperature in Celsius: "))

                fahrenheit = celsius_to_fahrenheit(celsius)

                print(f"\n{celsius:.2f}°C = {fahrenheit:.2f}°F")

            except ValueError:
                print("\nInvalid input! Please enter a numeric temperature.")

        elif choice == "2":

            try:
                fahrenheit = float(
                    input("Enter temperature in Fahrenheit: ")
                )

                celsius = fahrenheit_to_celsius(fahrenheit)

                print(f"\n{fahrenheit:.2f}°F = {celsius:.2f}°C")

            except ValueError:
                print("\nInvalid input! Please enter a numeric temperature.")

        elif choice == "3":

            print("\n==========================================")
            print("     Thank you for using the converter!")
            print("                 Goodbye!")
            print("==========================================")

            break

        else:

            print("\nInvalid choice!")
            print("Please select an option from 1 to 3.")


# Start the application
temperature_converter()