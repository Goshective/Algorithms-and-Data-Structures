def read_file(path, *funcs):
    with open(path, 'r') as inp:
        res = []
        for i, line in enumerate(inp.readlines()):
            res.append(funcs[i](line.rstrip()))
    return res
        

def write_file(path, ans):
    with open(path, 'w') as out:
        print(ans, file=out, end='')


def read_n_lst_file(path):
    with open(path, 'r') as inp:
        _ = int(inp.readline())
        lst = [int(x) for x in inp.readline().split()]
    return lst


def read_2_n_lst_file(path):
    with open(path, 'r') as inp:
        _ = int(inp.readline())
        lst1 = [int(x) for x in inp.readline().split()]
        _ = int(inp.readline())
        lst2 = [int(x) for x in inp.readline().split()]
    return lst1, lst2


def write_lst_file(path, lst, sep=" "):
    with open(path, 'w') as out:
        print(*lst, file=out, sep=sep, end='')


def write_n_lst_file(path, n, lst, sep=" "):
    with open(path, 'w') as out:
        print(n, file=out)
        print(*lst, file=out, sep=sep, end='')


def write_lst_by_lines_file(path, lst, sep=' '):
    with open(path, 'w') as out:
        for el in lst:
            print(el, file=out, sep=sep)