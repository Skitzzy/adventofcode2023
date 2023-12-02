def minimum_cubes(input_data):
    total_power = 0
    for game in input_data:
        game_data = game.split(':')[1]
        rounds = game_data.split(';')
        min_red, min_green, min_blue = 0, 0, 0
        for round in rounds:
            cubes = round.split(',')
            for cube in cubes:
                count, color = cube.split()
                if color == 'red':
                    min_red = max(min_red, int(count))
                elif color == 'green':
                    min_green = max(min_green, int(count))
                elif color == 'blue':
                    min_blue = max(min_blue, int(count))
        total_power += min_red * min_green * min_blue
    return total_power

def minimum_cubes_from_file(file_path):
    with open(file_path, 'r') as file:
        input_data = file.readlines()
    return minimum_cubes(input_data)

print(minimum_cubes_from_file('day2/input_1.txt'))  