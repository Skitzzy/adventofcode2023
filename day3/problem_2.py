def calculate_gear_ratio(schematic):
    # Parse the input into a 2D array
    # schematic = [list(row) for row in schematic.split('\n')]

    # Initialize the total gear ratio and the array to keep track of the full numbers
    total_gear_ratio = 0
    full_numbers = [[0]*len(row) for row in schematic]

    # Function to form the full number from a digit
    def form_number(i, j):
        number = ''
        for dj in range(j, -1, -1):  # Read to the left
            if schematic[i][dj].isdigit():
                number = schematic[i][dj] + number
            else:
                break
        for dj in range(j+1, len(schematic[i])):  # Read to the right
            if schematic[i][dj].isdigit():
                number += schematic[i][dj]
            else:
                break
        return int(number)

    # Iterate over each element in the array
    for i in range(len(schematic)):
        for j in range(len(schematic[i])):
            # When an asterisk (*) is found
            if schematic[i][j] == '*':
                numbers = []
                # Check all adjacent cells for digits, including diagonals
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if di == 0 and dj == 0:  # Skip the current cell
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < len(schematic) and 0 <= nj < len(schematic[i]) and schematic[ni][nj].isdigit():
                            # Form the full number and add it to the numbers list
                            number = form_number(ni, nj)
                            if number not in numbers:
                                numbers.append(number)
                # If two unique numbers were found
                if len(numbers) == 2:
                    # Multiply them together to get the gear ratio and add it to the total gear ratio
                    total_gear_ratio += numbers[0] * numbers[1]

    return total_gear_ratio

def read_schematic(filename):
    with open(filename, 'r') as f:
        schematic = [list(line.strip()) for line in f]
    return schematic

schematic = read_schematic('day3/input_1.txt')
# schematic = [
#     list("467..114.."),
#     list("...*......"),
#     list("..35..633."),
#     list("......#..."),
#     list("617*......"),
#     list(".....+.58."),
#     list("..592....."),
#     list("......755."),
#     list("...$.*...."),
#     list(".664.598..")
# ]

print(calculate_gear_ratio(schematic))