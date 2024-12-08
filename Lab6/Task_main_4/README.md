# Задание №4 по варианту : `Прошитый ассоциативный массив`
Студент ИТМО,  Скворцов Денис Александрович, 472486

## Вариант 15

## Задание 
Реализуйте прошитый ассоциативный массив. Ваш алгоритм должен поддер
живать следующие типы операций:
- get x– если ключ x есть в множестве, выведите соответствующее ему
 значение, если нет, то выведите <none>.
- prev x–вывести значение, соответствующее ключу, находящемуся в ассо
циативном массиве, который был вставлен позже всех, но до x, или <none>,
если такого нет или в массиве нет x.
- next x –вывести значение, соответствующее ключу, находящемуся в ассо
циативном массиве, который был вставлен раньше всех, но после x , или <none>, если такого нет или в массиве нет x .
- put x y – поставить в соответствие ключу x значение y. При этом следует
 учесть, что– eсли, независимо от предыстории, этого ключа на момент вставки в
 массиве не было, то он считается только что вставленным и оказыва
ется самым последним среди добавленных элементов– то есть, вызов
 next с этим же ключом сразу после выполнения текущей операции put
 должен вернуть <none>;– если этот ключ уже есть в массиве, то значение необходимо изменить,
 и в этом случае ключ не считается вставленным еще раз, то есть, не
 меняет своего положения в порядке добавленных элементов.
- delete x – удалить ключ x. Если ключа в ассоциативном массиве нет, то
 ничего делать не надо.

## Input / Output 

| Input    | Output |
|----------|----------|
|14        | c     |
|put zero a| b     |
|put one b | d     |
|put two c | c     |
|put three d| a     |
|put four e | e     |
|get two    | <none>     |
|prev two   |       |
|next two   |       |
|delete one|       |
|delete three|       |
|get two|       |
|prev two|       |
|next two|       |
|next four|       |


## Ограничения по времени и памяти

- Ограничение по времени. 4сек.
- Ограничение по памяти. 256 мб.


## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Goshective/Algorithms-and-Data-Structures
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd Algorithms-and-Data-Structures/Lab6/Task_main_4
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