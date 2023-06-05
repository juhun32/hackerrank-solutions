if __name__ == "__main__":
    lis_name = []
    lis_score = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        lis_name.append(name)
        lis_score.append(score)

    temp = 0
    temp = sorted(set(lis_score))[1]
    result = []
    for i in range(len(lis_score)):
        if temp == lis_score[i]:
            result.append(lis_name[i])
        else:
            continue

    print(*sorted(result), sep="\n")
