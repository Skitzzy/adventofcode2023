def possible_games(input_data, red_cubes, green_cubes, blue_cubes):
    possible_game_ids = []
    for game in input_data:
        game_id, game_data = game.split(':')
        game_id = int(game_id.split()[1])  # Extract the game ID
        rounds = game_data.split(';')
        possible = True
        for round in rounds:
            cubes = round.split(',')
            for cube in cubes:
                count, color = cube.split()
                if color == 'red' and int(count) > red_cubes:
                    possible = False
                    break
                elif color == 'green' and int(count) > green_cubes:
                    possible = False
                    break
                elif color == 'blue' and int(count) > blue_cubes:
                    possible = False
                    break
            if not possible:
                break
        if possible:
            possible_game_ids.append(game_id)
    return sum(possible_game_ids)

def possible_games_from_file(file_path, red_cubes, green_cubes, blue_cubes):
    with open(file_path, 'r') as file:
        input_data = file.readlines()
    return possible_games(input_data, red_cubes, green_cubes, blue_cubes)

print(possible_games_from_file('day2/input_1.txt', 12, 13, 14))