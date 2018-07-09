import numpy as np


def main():
    first_equation()


def first_equation():
    a = np.array([[3, 1], [1,2]])
    b = np.array([9, 8])
    result = np.linalg.solve(a, b)
    print(result)


if __name__ == "__main__":
    main()
