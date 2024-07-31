from itertools import combinations
if __name__ == "__main__":
    # генерирует все возможные сочетания объектов из n по k
    n = 5
    k = 3
    
    set_of_nums = list(range(1, n+1))
    
    for i in combinations(set_of_nums, k):
        print(i)