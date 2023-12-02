def extract_and_sum_calibration_values(file_path):
    total_sum = 0
    digit_map = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        first_digit = None
        last_digit = None

        # Iterate over each character in the line
        for i in range(len(line)):
            # Check for numeric digits
            if line[i].isdigit():
                if not first_digit:
                    first_digit = line[i]
                last_digit = line[i]

            # Check for spelled out digits in a sliding window of characters
            for word, digit in digit_map.items():
                if line[i:i+len(word)] == word:
                    if not first_digit:
                        first_digit = digit
                    last_digit = digit

        if first_digit and last_digit:
            # Combine the first and last digit to form a two-digit number
            calibration_value = int(first_digit + last_digit)
            total_sum += calibration_value

    return total_sum

# Example usage
file_path = 'day1/input_1.txt'
result = extract_and_sum_calibration_values(file_path)
print(result)