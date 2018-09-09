def execute_program():
    # Retrieve and store user input
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # Output a list of lists where x+y+z != n
    stored_result = [[i, j, k] for i in range(x+1) for j in range(y+1)
                     for k in range(z+1) if (i+j+k) != n]
    print(stored_result)


if __name__ == '__main__':
    execute_program()
