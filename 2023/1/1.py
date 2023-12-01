import re


# Get the first digit of a string
def get_first_digit(input):
    return re.search(r'\d', input).group(0)


# Get the last digit of a string
def get_last_digit(input):
    return re.search(r'\d(?=[^\d]*$)', input).group(0)


# Get the first and last digit of a string as an integer
def get_digits(input):
    first_digit = get_first_digit(input)
    last_digit = get_last_digit(input)
    final_digit = f"{first_digit}{last_digit}"

    return int(final_digit)


calibration_input_file = 'calibration_input_1.txt'
calibration_values = []

with open(calibration_input_file, 'r') as file:
    for line in file:
        calibration_values.append(get_digits(line))

print(sum(calibration_values))  # Result: 54450
