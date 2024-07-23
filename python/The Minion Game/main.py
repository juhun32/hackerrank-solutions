def minion_game(string):
    # your code goes here
    vowels = "AEIOU"
    leng = len(string)
    kevin, stuart = 0, 0

    for i in range(leng):
        if string[i] in vowels:
            kevin += leng - i
        else:
            stuart += leng - i

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")


if __name__ == "__main__":
    s = input()
    minion_game(s)
