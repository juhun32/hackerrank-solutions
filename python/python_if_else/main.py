if __name__ == '__main__':
    n = int(input().strip())
    if n%2 == 1:
        print("Weird")
    if 2 <= n <= 5 and n%2 == 0:
        print("Not Weird")
    elif 6 <= n <= 20 and n%2 == 0:
        print("Weird")
    elif 20 < n and n%2 == 0:
        print("Not Weird")