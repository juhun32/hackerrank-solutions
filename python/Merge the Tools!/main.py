def merge_the_tools(string, k):
    # your code goes here
    for i in range(len(string) // k):
        temp = string[i * k : i * k + k]
        result = ""
        for ch in temp:
            if ch not in result:
                result += ch
        print(result)


if __name__ == "__main__":
    string, k = input(), int(input())
    merge_the_tools(string, k)
