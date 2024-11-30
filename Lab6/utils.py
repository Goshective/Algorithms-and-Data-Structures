def read_file(path, *funcs):
    with open(path, 'r') as inp:
        res = []
        for i, line in enumerate(inp.readlines()):
            res.append(funcs[i](line.rstrip()))
    return res
        

def write_file(path, ans):
    with open(path, 'w') as out:
        print(ans, file=out, end='')


def read_lst_file(path, func, sep=" "):
    with open(path, 'r') as inp:
        lst = [func(i) for i in inp.readline().split(sep=sep)]
    return lst


def read_n_lst(path, func=int):
    with open(path, 'r') as inp:
        n = int(inp.readline()) 
        lst = [func(i) for i in inp.readline().split()]
    return n, lst


def read_commands(path):
    with open(path, 'r') as inp:
        n = int(inp.readline())
        ret = []
        for _ in range(n):
            ret.append(inp.readline().rstrip())
    return ret


def write_lst_file(path, lst, sep=" "):
    with open(path, 'w') as out:
        print(*lst, file=out, sep=sep, end='')


def write_lst_by_lines_file(path, lst, sep=' '):
    with open(path, 'w') as out:
        for el in lst:
            print(el, file=out, sep=sep)


def write_mat_by_lines_file(path, mat, sep=' '):
    with open(path, 'w') as out:
        for lst in mat:
            print(*lst, file=out, sep=sep)