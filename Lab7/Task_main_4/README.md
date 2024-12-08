# Задание №4 по варианту : `Наибольшая общая подпоследовательность двух последовательностей`
Студент ИТМО,  Скворцов Денис Александрович, 472486

## Вариант 15

## Задание 
Вычислить длину самой длинной общей подпоследовательности из двух по
следовательностей.
Даны две последовательности A = (a1,a2,...,an) и B = (b1,b2,...,bm), найти
длину их самой длинной общей подпоследовательности, т.е. наибольшее неотри
цатеьное целое число p такое, что существуют индексы 1 ≤ i1 < i2 < ... < ip ≤ n
и 1 ≤ j1 < j2 <... < jp ≤ m такие,что ai1 = bj1 ,..., aip = bjp.

## Input / Output 

| Input    | Output |
|----------|----------|
|3         | 2        |
|2 7 5     |          |
|2         |          |
|2 5       |          |

## Ограничения по времени и памяти

- Ограничение по времени. 1 сек.
- Ограничение по памяти. 256 мб.


## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Goshective/Algorithms-and-Data-Structures
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd Algorithms-and-Data-Structures/Lab7/Task_main_4
   ```

3. Запустите программу
    ```bash
        python src/main.py
    ```

4. Запуск тестов
    ```bash
        python tests/test.py
    ```

## Тестирование
Для запуска всех тестов выполните:
```bash
    python tests_runner.py
```