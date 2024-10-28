def read_file(path, *funcs):
    with open(path, 'r') as inp:
        res = []
        for i, line in enumerate(inp.readlines()):
            res.append(funcs[i](line.rstrip()))
    return res
        

def write_file(path, ans):
    with open(path, 'w') as out:
        print(ans, file=out, end='')


def read_multi_lst_file(path, last_string=False):
    with open(path, 'r') as inp:
        args = [int(x) for x in inp.readline().rstrip().split()]
        lst = []
        for _ in range(args[0]):
            lst.append([int(x) for x in inp.readline().rstrip().split()])
        if last_string:
            return (args, lst, [int(x) for x in inp.readline().rstrip().split()])
    return (args, lst)

def read_lst_file(path, func, sep=" "):
    with open(path, 'r') as inp:
        lst = [func(i) for i in inp.readline().split(sep=sep)]
    return lst


def read_len_lst_file(path, func):
    with open(path, 'r') as inp:
        n = int(inp.readline()) 
        lst = [func(i) for i in inp.readline().split()]
    return n, lst


def write_lst_file(path, lst, sep=" "):
    with open(path, 'w') as out:
        print(*lst, file=out, sep=sep, end='')