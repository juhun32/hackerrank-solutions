if __name__ == '__main__':
    N = int(input())
    res_lst = []
    
    for i in range(N):
        cmd = input().split()
        if "insert" in cmd:
            res_lst.insert(int(cmd[1]),int(cmd[2]))
        elif "print" in cmd:
            print(res_lst)
        elif "remove" in cmd:
            res_lst.remove(int(cmd[1]))
        elif "append" in cmd:
            res_lst.append(int(cmd[1]))
        elif "sort" in cmd:
            res_lst.sort()
        elif "pop" in cmd:
            res_lst.pop()
        elif "reverse" in cmd:
            res_lst.reverse()