def read_schematic(filename):
    with open(filename, 'r') as f:
        schematic = [list(line.strip()) for line in f]
    return schematic

def sum_of_parts(schematic):
    rows = len(schematic)
    cols = len(schematic[0])
    total = 0
    visited = [[False]*cols for _ in range(rows)]

    # def get_full_number(i, j):
    #     number = ''
    #     left, right = j, j
    #     while left >= 0 and schematic[i][left].isdigit() and not visited[i][left]:
    #         visited[i][left] = True
    #         number = schematic[i][left] + number
    #         left -= 1
    #     while right < cols and schematic[i][right].isdigit() and not visited[i][right]:
    #         visited[i][right] = True
    #         number += schematic[i][right]
    #         right += 1
    #     return int(number)

    for i in range(rows):
        for j in range(cols):
            if not schematic[i][j].isdigit() and schematic[i][j] != '.':
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < rows and 0 <= ny < cols and schematic[nx][ny].isdigit() and not visited[nx][ny]:
                            number = ''
                            left, right = ny, ny + 1
                            while left >= 0 and schematic[nx][left].isdigit() and not visited[nx][left]:
                                visited[nx][left] = True
                                number = schematic[nx][left] + number
                                left -= 1
                                print(f"Added left digit to number {number}")
                            while right < cols and schematic[nx][right].isdigit() and not visited[nx][right]:
                                visited[nx][right] = True
                                number += schematic[nx][right]
                                right += 1
                                print(f"Added right digit to number {number}")
                            print(f"found number {number}")
                            total += int(number)
                            # total += get_full_number(nx, ny)
    return total

# Usage:
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

print(sum_of_parts(schematic))