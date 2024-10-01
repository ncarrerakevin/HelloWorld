if __name__ == "__main__":
    number = int(input())
    for i in range(1,number):
        print(i * (10**i // 9))