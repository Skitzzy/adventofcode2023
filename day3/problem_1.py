def sum_of_parts(schematic):
    symbols = {'*', '#', '+', '$'}
    rows = len(schematic)
    cols = len(schematic[0])
    total = 0
    visited = [[False]*cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if schematic[i][j] in symbols:
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < rows and 0 <= ny < cols and schematic[nx][ny].isdigit() and not visited[nx][ny]:
                            total += int(schematic[nx][ny])
                            visited[nx][ny] = True
    return total