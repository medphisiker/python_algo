def next_combination(combination):
    # изменяет массив на следующее лексикографически сочетание
    for i in range(k - 1, -1, -1):
        if combination[i] <= n - k + i:
            combination[i] += 1
            for j in range(i + 1, k):
                combination[j] = combination[j - 1] + 1
            return True

    return False


if __name__ == "__main__":
    # генерирует все возможные сочетания объектов из n по k
    n = 5
    k = 3

    # самое первое сочетание
    combination = [i + 1 for i in range(k)]

    print(combination)
    while next_combination(combination):
        print(combination)
