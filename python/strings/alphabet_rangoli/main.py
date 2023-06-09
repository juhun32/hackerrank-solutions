def print_rangoli(size):
    # your code goes here
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(n - 1, -n, -1):
        string = '-'.join(alphabet[n - 1 : abs(i) : -1] + alphabet[abs(i) : n])
        print(string.center((n * 2 - 1) * 2 - 1, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)