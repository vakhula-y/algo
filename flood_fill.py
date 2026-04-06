def flood_fill(matrix, x, y, new_color):
    n = len(matrix)
    m = len(matrix[0])
    old_color = matrix[x][y]

    print(f"--> Координати старту в пам'яті: рядок {x}, колонка {y}")
    print(f"--> Старий колір (на якому ми стоїмо): '{old_color}'")
    print(f"--> Новий колір (колір заливки): '{new_color}'")

    if old_color == new_color:
        print("--> СТОП: Кольори однакові! Матриця не потребує змін.")
        return matrix

    stack = [(x, y)]
    painted_count = 0 

    while stack:
        i, j = stack.pop()

        if i < 0 or i >= n or j < 0 or j >= m:
            continue

        if matrix[i][j] != old_color:
            continue

        matrix[i][j] = new_color
        painted_count += 1

        stack.append((i + 1, j))
        stack.append((i - 1, j))
        stack.append((i, j + 1))
        stack.append((i, j - 1))

    print(f"--> Зафарбовано клітинок: {painted_count}")
    return matrix

with open("input.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

n, m = map(int, lines[0].split(","))
x, y = map(int, lines[1].split(","))

x -= 1
y -= 1

new_color = lines[2].replace("'", "")

matrix = []
for i in range(3, 3 + n):
    row = lines[i].replace("[", "").replace("]", "").replace("'", "").replace(",", " ").split()
    matrix.append(row)

print("ЗАПУСК АЛГОРИТМУ")
result = flood_fill(matrix, x, y, new_color)

with open("output.txt", "w", encoding="utf-8") as f:
    for row in result:
        f.write(str(row) + "\n")
        
print("ФАЙЛ output.txt ОНОВЛЕНО")
