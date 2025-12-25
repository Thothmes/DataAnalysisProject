import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


def main():

    array = np.genfromtxt(
        fname='data2.csv',
        delimiter=';',      # Указываем разделитель колонок
        encoding='utf-8-sig'  # Учитываем BOM в начале файла
    )

    # A*x=b, где А = матрица Вандермонда 3 порядка (для полинома 2 степени), x - вектор коэффициентов, b = вектор итоговых результатов 
    A_vector = [array[0][0], array[len(array)//2][0], array[-1][0]]
    b_vector = [array[0][1], array[len(array)//2][1], array[-1][1]]
    A_matrix = np.vander(A_vector)

    #print(np.linalg.det(A_matrix))

    print("Определяем детерминант матрицы")

    if np.linalg.det(A_matrix) == 0:
        print("Матрица вырожденная")
        return False

    print("Матрица не вырожденная")

    np_solve = np.linalg.solve(A_matrix, b_vector)

    sp_solve = sp.linalg.solve(A_matrix, b_vector)

    print(np_solve)
    
    print(sp_solve)

    print(A_vector, A_matrix, b_vector)

    print((A_matrix@sp_solve)) #Это моя заметка: @ - знак матричного умножения

    print(b_vector)

    plt.plot(A_matrix@sp_solve)
    plt.show()

    plt.plot(b_vector)
    plt.show()

    residuals = A_matrix@sp_solve - b_vector

    RSS = np.sum(residuals**2)

    print(A_matrix@sp_solve, " sdgsdg ", b_vector)
    print(RSS, "dsgg")

    A_vector_4 = [array[0][0], array[len(array)//3][0], array[len(array)//2][0], array[-1][0]]
    b_vector_4 = [array[0][1], array[len(array)//3][1], array[len(array)//2][1], array[-1][1]]
    A_matrix_4 = np.vander(A_vector_4)

    #print(np.linalg.det(A_matrix))

    print("Определяем детерминант матрицы")

    if np.linalg.det(A_matrix_4) == 0:
        print("Матрица вырожденная")
        return False

    print("Матрица не вырожденная")

    np_solve_4 = np.linalg.solve(A_matrix_4, b_vector_4)

    sp_solve_4 = sp.linalg.solve(A_matrix_4, b_vector_4)

    print(np_solve_4)
    
    print(sp_solve_4)

    print(A_vector_4, A_matrix_4, b_vector_4)

    print((A_matrix_4@sp_solve_4)) #Это моя заметка: @ - знак матричного умножения

    print(b_vector_4)

    plt.plot(A_matrix_4@sp_solve_4)
    plt.show()

    plt.plot(b_vector_4)
    plt.show()

    residuals_4 = A_matrix_4@sp_solve_4 - b_vector_4

    RSS_4 = np.sum(residuals_4**2)

    print(A_matrix_4@sp_solve_4, " sdgsdg ", b_vector_4)
    print(RSS_4, "dsgg")


    return

if __name__ == "__main__":
    main()