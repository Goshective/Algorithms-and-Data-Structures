# Задание №1 по варианту : `Стек`
Студент ИТМО,  Скворцов Денис Александрович, 472486

## Вариант 15

## Задание 
Реализуйте работу стека. Для каждой операции изъятия элемента выведите ее
 результат.
 На вход программе подаются строки, содержащие команды. Каждая стро
ка содержит одну команду. Команда — это либо “+ N”, либо “–”. Команда “+
 N”означает добавление в стек числа N, по модулю не превышающего 109. Ко
манда “–”означает изъятие элемента из стека. Гарантируется, что не происходит
 извлечения из пустого стека. Гарантируется, что размер стека в процессе выпол
нения команд не превысит 106 элементов. 

## Input / Output 

| Input    | Output |
|----------|----------|
|6         | 10       |
|+ 1       | 1234     |
|+ 10      |          |
|-         |          |
|+ 2       |          |
|+ 1234    |          |
|-         |          |

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
   cd Algorithms-and-Data-Structures/Lab4/Task_main_1
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