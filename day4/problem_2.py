from collections import deque, Counter

def calculate_total_cards(file_path):
    with open(file_path, 'r') as file:
        cards = file.readlines()
    total_cards = len(cards)
    queue = deque(range(len(cards)))
    card_counts = Counter(range(len(cards)))

    while queue:
        i = queue.popleft()
        card = cards[i]
        card = card.strip().split(': ')[1]
        winning_numbers, your_numbers = card.split(' | ')
        winning_numbers = set(map(int, winning_numbers.split()))
        your_numbers = set(map(int, your_numbers.split()))

        common_numbers = winning_numbers & your_numbers
        matches = len(common_numbers)

        for j in range(1, matches + 1):
            if i + j < len(cards):
                card_counts[i + j] += card_counts[i]

    total_cards = sum(card_counts.values())
    return total_cards

print(calculate_total_cards('day4/input_1.txt'))