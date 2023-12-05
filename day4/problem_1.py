def calculate_points(filename):
    with open(filename, 'r') as file:
        cards = file.readlines()

    total_points = 0

    for card in cards:
        card = card.strip().split(': ')[1]
        winning_numbers, your_numbers = card.split(' | ')
        winning_numbers = set(map(int, winning_numbers.split()))
        your_numbers = set(map(int, your_numbers.split()))

        common_numbers = winning_numbers & your_numbers
        points = 2 ** (len(common_numbers) - 1) if common_numbers else 0

        total_points += points

    return total_points

print(calculate_points('day4/input_1.txt'))