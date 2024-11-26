# Лабораторная работа №6: ` Хеширование. Хеш-таблицы`

Студент ИТМО, Скворцов Денис Александрович, 472486

## Вариант 15

### Навигация
- [Задача 2 - Высота дерева ](Task_main_2)
- [Задача 4 - Прошитый ассоциативный массив ](Task_main_4)
- [Задача 5 - Выборы в США ](Task_plus_5)
- [Задача 6 - Фибоначчи возвращается ](Task_main_6)


## Описание
В этой лабораторной работе будут реализованы алгоритмы, задействующие Хеш-таблицы и операцию хеширования.

## Структура проекта
- `Task_main_n/` — задания по варианту.
- - `/src/` — исходный код программы.
- - - `/txtf/` — текстовые файлы
- - - `/main.py` — решение задачи
- - `/tests/` — автоматические тесты для проверки работы кода.
- - - `/test.py` — unit тесты
- `Task_plus_n/` — дополнительные задания.
- - `/src/` — исходный код программы.
- - `/tests/` — автоматические тесты для проверки работы кода.
- `tests_runner.py` - запуск всех тестовых файлов лабороторной
- `tasks_runner.py` - запуск всех файлов решений лабороторной
- `utils.py` — вспомогательные функции

## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Goshective/Algorithms-and-Data-Structures
   ```

2. Перейдите в папку с проектом:
   ```bash
   cd '.\Algorithms and Data Structures\Lab6\'
   ```

3. **Запуск всех задач**
    ```bash
        python tasks_runner.py
    ```

4. **Запуск всех тестов задач**
    ```bash
        python tests_runner.py
    ```