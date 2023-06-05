def swap_case(s):
    line = list(s)
    temp = ''
    for i in range(len(line)):
        if line[i].isupper() == True:
            temp += line[i].lower()
        elif line[i].isupper() == False:
            temp += line[i].upper()
        else:
            continue
    return temp


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)