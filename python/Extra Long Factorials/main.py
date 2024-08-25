def extraLongFactorials(n):
    def factorials(n):
        if n == 1:
            return 1
        return factorials(n - 1) * n

    print(factorials)


if __name__ == "__main__":
    n = int(input().split())

    extraLongFactorials(n)
