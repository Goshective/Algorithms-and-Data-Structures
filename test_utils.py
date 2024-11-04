import time
import tracemalloc


MB = 1024**2


class ConsoleTimeMemory:
    def output_design(test_name, res_time, res_memory):
            if res_memory < 1024:
                out_mem = f'{res_memory} Байт'
            elif res_memory < 1024**2:
                out_mem = f'{round(res_memory / 1024, 1)} Килобайт'
            else:
                out_mem = f'{round(res_memory / (1024**2), 1)} Мегабайт'

            print(f"Тест {test_name}:")
            print("Время работы: %s секунд " % (res_time), end='\n')
            print("Затрачено памяти:", out_mem)
    
    def count_time(func, *args):
        t_start = time.perf_counter()
        func(*args)
        res_time = time.perf_counter() - t_start
        return res_time

    def count_memory(func, *args):
        tracemalloc.start()
        func(*args)
        memory = tracemalloc.get_traced_memory()[1]
        return memory


def output_design(test_name, func, *args): # to deletion after changing system
    tracemalloc.start()
    t_start = time.perf_counter()
    func(*args)
    res_time = time.perf_counter() - t_start
    res_memory = tracemalloc.get_traced_memory()[1]

    if res_memory < 1024:
        out_mem = f'{res_memory} Байт'
    elif res_memory < 1024**2:
        out_mem = f'{round(res_memory / 1024, 1)} Килобайт'
    else:
        out_mem = f'{round(res_memory / (1024**2), 1)} Мегабайт'

    print(f"Тест {test_name}:")
    print("Время работы: %s секунд " % (res_time), end='\n')
    print("Затрачено памяти:", out_mem)