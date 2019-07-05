import random

def hakidashi(matrix, dim):
    for i in range(dim):
        for j in range(dim):
            if i == j:
                pass
            else:
                a = matrix[j][i]
                for k in range(i, dim):
                    matrix[j][k] = matrix[j][k]- a * matrix[i][k]
        print(matrix)

def main():
    dim = 10    #次元
    matrix = a1 = [[random.randint(0,1) for i in range(10)] for j in range(10)]
    hakidashi(matrix, dim)
    print(matrix)

if __name__ == '__main__':
    main()