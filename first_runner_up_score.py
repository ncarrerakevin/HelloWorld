if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)

    max_value = max(arr)
    arr = [i for i in arr if i!=max_value]
    print(max(arr))