# menu driven python program for temperature conversions


def main():
    while True:
        print(
            """\t\t\tmenu\n
              1.celsius to farenheit
              2.farenheit to celsius 
              3.celsius to kelvin
              4.kelvin to celsius
              5.farenheit to kelvin
              6.kelvin to farenheit
              7.exit from program\n"""
        )
        choice = int(input("Enter the choice "))

        if choice == 1:
            celcius = float(input("Enter the temperature in celsius "))

            farenheit = (celcius * 9 / 5) + 32
            print(f"the temperature in farenheit is {farenheit}")

        elif choice == 2:
            farenheit = float(input("Enter the temperature in farenheit "))

            celsius = (farenheit - 32) * 5 / 9
            print(f"the temperature in celsius is {celsius}")

        elif choice == 3:
            celsius = float(input("Enter the temperature in celsius "))

            kelvin = celsius + 273.15
            print(f"the temperature in kelvin is {kelvin}")

        elif choice == 4:
            kelvin = float(input("Enter the temperature in kelvin "))

            celsius = kelvin - 273.15
            print(f"the temperature in celsius is {celsius}")

        elif choice == 5:
            farenheit = float(input("Enter the temperature in farenheit "))

            kelvin = ((farenheit - 32) * (5 / 9)) + 273.15
            print(f"the temperature in kelvin is {kelvin}")

        elif choice == 6:
            kelvin = float(input("Enter the temperature in kelvin "))

            farenheit = ((kelvin - 273.15) * (9 / 5)) + 32
            print(f"the temperature in farenheit is {farenheit}")

        elif choice == 7:
            print("exiting....")
            break

        else:
            print("Enter a valid input ")


if __name__ == "__main__":
    main()
