def extract_and_sum_calibration_values(file_path):
    """
    Extracts the calibration values from each line by combining the first and last digit (in that order) 
    to form a single two-digit number, and then sums these values.

    :param file_path: Path to the file containing the calibration document.
    :return: Sum of the extracted calibration values.
    """
    total_sum = 0

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        # Find the first digit in the line
        first_digit = next((char for char in line if char.isdigit()), None)
        # Find the last digit in the line (reversed order)
        last_digit = next((char for char in reversed(line) if char.isdigit()), None)

        if first_digit and last_digit:
            # Combine the first and last digit to form a two-digit number
            calibration_value = int(first_digit + last_digit)
            total_sum += calibration_value

    return total_sum

# Example usage
file_path = 'day1/input_1.txt'
result = extract_and_sum_calibration_values(file_path)
print(result)