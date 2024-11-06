def read_file(path, *funcs):
    with open(path, 'r') as inp:
        res = []
        for i, line in enumerate(inp.readlines()):
            res.append(funcs[i](line.rstrip()))
    return res
        

def write_file(path, ans):
    with open(path, 'w') as out:
        print(ans, file=out, end='')


def read_multiple_string_file(path):
    with open(path, 'r') as inp:
        n = int(inp.readline())
        ret = []
        for _ in range(n):
            line = inp.readline()
            if line[0] == '+':
                cmd_i = line.split()
                cmd_i[1] = int(cmd_i[1])
            else:
                cmd_i = [line.rstrip(), None]
            ret.append(cmd_i)
    return (n, ret)

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

def write_lst_by_lines_file(path, lst):
    with open(path, 'w') as out:
        for el in lst:
            print(el, file=out)