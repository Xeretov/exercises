# Gioele Amendola
# 29/04/2024

# Create a function that converts a given integer to its Roman numeral representation. 
# Handle numbers from 1 to 3999. Use a combination of string manipulation and conditional statements to build the Roman numeral.


def roman_conversion(number: int) -> str | None:
    try:
        if number < 1 or number > 3999:
            raise ValueError
    except ValueError:
        print("\nInvalid Number.")
        return None
    print("\nRoman numeral conversion:")
    print(f"{number}")

    # Find digits of number
    digits: list = []
    temp: int = number
    while temp >= 1:
        digits.append(temp%10)
        temp //= 10
    digits.reverse()
    place_value: int = len(digits)
    roman: str = ""

    # Replace numbers with roman numerals
    for digit in digits:
        if place_value == 4:
            while digit > 0:
                roman += 'M'
                digit -= 1
        elif place_value == 3:
            while digit > 0:
                if digit < 4:
                    roman += 'C'
                    digit -= 1
                elif digit == 4:
                    roman += 'CD'
                    digit = 0
                elif digit < 9:
                    roman += 'D'
                    digit -= 5
                else:
                    roman += 'CM'
                    digit = 0
        elif place_value == 2:
            while digit > 0:
                if digit < 4:
                    roman += 'X'
                    digit -= 1
                elif digit == 4:
                    roman += 'XL'
                    digit = 0
                elif digit < 9:
                    roman += 'L'
                    digit -= 5
                else:
                    roman += 'XC'
                    digit = 0
        elif place_value == 1:
            while digit > 0:
                if digit < 4:
                    roman += 'I'
                    digit -= 1
                elif digit == 4:
                    roman += 'IV'
                    digit = 0
                elif digit < 9:
                    roman += 'V'
                    digit -= 5
                else:
                    roman += 'IX'
                    digit = 0
        place_value -= 1

    return roman

print(roman_conversion(int(input("> "))),end="\n\n")