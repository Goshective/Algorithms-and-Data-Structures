# Задание №5 по варианту : `Стек с максимумом`
Студент ИТМО,  Скворцов Денис Александрович, 472486

## Вариант 15

## Задание 
 Стек - это абстрактный тип данных, поддерживающий операции Push() и
 Pop(). Не трудно реализовать его таким образом, чтобы обе эти операции работали
 за константное время. В этой задаче ваша цель- реализовать стек, который также
 поддерживает поиск максимального значения и гарантирует, что все операции
 по-прежнему работают за константное время.
 Реализуйте стек, поддерживающий операции Push(), Pop() и Max().

## Input / Output 

| Input    | Output |
|----------|----------|
|5         | 2        |
|push 2    | 2        |
|push 1    |          |
|max       |          |
|pop       |          |
|max       |          |

## Ограничения по времени и памяти

- Ограничение по времени. 2сек.
- Ограничение по памяти. 256 мб.


## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Goshective/Algorithms-and-Data-Structures
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd Algorithms-and-Data-Structures/Lab4/Task_main_5
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