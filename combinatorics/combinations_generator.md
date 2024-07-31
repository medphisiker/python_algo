---
Author:
  - Ширяев Антон
tags:
  - алгоритмы
  - python
  - комбинаторика
  - сочетания_combination
  - полный_перебор
date: 2024-07-31
---

### Описание
Дано множество натуральных чисел: $\{1, 2, \ldots , n\}$
Хотим получить все возможные сочетания $C_n^k$  (из $n$ по $k$).

* Cочетания $C_n^k$ удобно представить как отсортированный набор из $𝑘$ разных чисел от $1$ до $𝑛$.
* Удобно вывести их все в лексикографическом порядке. Например, для $𝑛=5, 𝑘=3$ хотим получить сочетания от 123 до 345.
* Будем **генерировать следующее сочетание** в смысле лексикографического порядка на основе текущего.

Первым сочетанием, возьмем просто числа от 1 до 𝑘, зафиксируем текущее сочетание.

**Надо увеличивать последний элемент, который мы еще можем увеличить**, а всем последующим присвоить минимальные возможные значения. Если увеличить ничего нельзя, то полученное сочетание – максимальное. Когда элемент на позиции 𝑖 (считая с 0) можно увеличить? Когда существуют хотя бы 𝑘−𝑖 чисел больше текущего, чтобы можно было поставить их после него.

### Реализация на Python

ссылка на репозиторий [ссылка](https://github.com/medphisiker/python_algo/blob/main/combinatorics/combinations_generator.py)

```python
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

```

Вывод программы:
```
[1, 2, 3]
[1, 2, 4]
[1, 2, 5]
[1, 3, 4]
[1, 3, 5]
[1, 4, 5]
[2, 3, 4]
[2, 3, 5]
[2, 4, 5]
[3, 4, 5]
```

### Используя itertools в Python

ссылка на репозиторий [ссылка](https://github.com/medphisiker/python_algo/blob/main/combinatorics/combinations_generator_itertools.py)

```python
from itertools import combinations

if __name__ == "__main__":
    # генерирует все возможные сочетания объектов из n по k
    n = 5
    k = 3

    set_of_nums = list(range(1, n + 1))

    for i in combinations(set_of_nums, k):
        print(i)

```

Вывод программы:
```
(1, 2, 3)
(1, 2, 4)
(1, 2, 5)
(1, 3, 4)
(1, 3, 5)
(1, 4, 5)
(2, 3, 4)
(2, 3, 5)
(2, 4, 5)
(3, 4, 5)
```
### Источники
1. Tinkoff Generation "Перебор" [ссылка](https://algorithmica.org/tg/object-generation)