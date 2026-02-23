def snake_breaks(matrix):
    if not matrix or not matrix[0]:
        print("Жодного разу не зробить перерву")
        return

    m = len(matrix)
    n = len(matrix[0])

    time = 0
    breaks = []
    
    for i in range(m):
       
        if i % 2 == 0:
            cols = range(n)
        else:
            cols = range(n-1, -1, -1)

        for j_index, j in enumerate(cols):
            
            if i == 0 and j_index == 0:
                continue

           
            if j_index == 0:
                time += 2
            else:
                time += 1

            if time % 30 == 0:
               
                breaks.append((i+1, j+1))

    if not breaks:
        print("Жодного разу не зробить перерву")
    else:
        print("Перерви на клітинках:", breaks)
        print("Кількість перерв:", len(breaks))
if __name__ == "__main__":
    matrix1 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    matrix2 = [
        [1, 2, 3, 4, 9, 6],
        [5, 6, 7, 8, 1, 7],
        [23, 2, 5, 4, 9, 6],
        [7, 8, 2, 4, 9, 6],
        [9, 10, 11, 12, 5, 10]
    ] 

snake_breaks(matrix1)
snake_breaks(matrix2)


    
