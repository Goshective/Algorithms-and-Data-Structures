def read_file(path, *funcs):
    with open(path, 'r') as inp:
        res = []
        for i, line in enumerate(inp.readlines()):
            res.append(funcs[i](line.rstrip()))
    return res


def read_lst_file(path, func, sep=" "):
    with open(path, 'r') as inp:
        lst = [func(i) for i in inp.readline().split(sep=sep)]
    return lst


def read_len_lst_file(path, func):
    with open(path, 'r') as inp:
        n = int(inp.readline()) 
        lst = [func(i) for i in inp.readline().split()]
    return n, lst


def read_len_double_lst_file(path, func):
    with open(path, 'r') as inp:
        n = int(inp.readline()) 
        lst = [func(i) for i in inp.readline().split()]
        lst2 = [func(i) for i in inp.readline().split()]
    return n, lst, lst2


def read_double_len_lst_file(path, func):
    with open(path, 'r') as inp:
        n = int(inp.readline())
        lst = [func(i) for i in inp.readline().split()]
        k = int(inp.readline())
        lst2 = [func(i) for i in inp.readline().split()]
    return n, lst, k, lst2


def write_file(path, ans):
    with open(path, 'w') as out:
        print(ans, file=out, end='')


def write_lst_file(path, lst):
    with open(path, 'w') as out:
        print(*lst, file=out, end='')


def write_lst_line_file(path, lst, line):
    with open(path, 'w') as out:
        print(*lst, file=out)
        print(line, file=out, end='')