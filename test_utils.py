import time
import tracemalloc


def output_design(test_name, func, *args):
        t_start = time.perf_counter()
        tracemalloc.start()
        func(*args)

        memory = tracemalloc.get_traced_memory()[1]
        if memory < 1024:
            out_mem = f'{memory} Байт'
        elif memory < 1024**2:
            out_mem = f'{round(memory / 1024, 1)} Килобайт'
        else:
            out_mem = f'{round(memory / (1024**2), 1)} Мегабайт'

        print(f"Тест {test_name}:")
        print("Время работы: %s секунд " % (time.perf_counter() - t_start), end='\n')
        print("Затрачено памяти:", out_mem)
        tracemalloc.stop()