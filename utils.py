def read_file(path, *funcs):
    with open(path, 'r') as inp:
        res = []
        for i, line in enumerate(inp.readlines()):
            res.append(funcs[i](line.rstrip()))
    return res
        

def write_file(path, ans):
    with open(path, 'w') as out:
        print(ans, file=out, end='')


def read_len_lst_file(path, func):
    with open(path, 'r') as inp:
        n = int(inp.readline()) 
        lst = [func(i) for i in inp.readline().split()]
    return n, lst


def write_lst_file(path, lst):
    with open(path, 'w') as out:
        print(*lst, file=out, end='')