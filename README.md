# Инструкция по использованию скрипта

## Шаг 1: Установка Python

Прежде всего, убедитесь, что на вашем компьютере установлен Python. Если нет, [скачайте и установите Python](https://www.python.org/downloads/). В процессе установки убедитесь, что вы выбрали опцию "Add Python to PATH".

## Шаг 2: Скачивание Скрипта

1. Нажмите на кнопку "Code" в репозитории на GitHub.
2. Выберите "Download ZIP".
3. Распакуйте скачанный архив в удобное место на вашем компьютере.

## Шаг 3: Подготовка Кошельков

1. Создайте файл `addresses.txt` в той же папке, где находится ваш скрипт.
2. Запишите в файл каждый кошелек, который вы хотите проверить, на отдельной строке.

## Шаг 4: Подготовка и запуск Скрипта

1. Откройте командную строку (Command Prompt на Windows, Terminal на macOS/Linux).
2. Перейдите в папку, в которой находится скрипт, используя команду `cd путь_к_папке`.
3. Введите команду `pip install -r requirements.txt`.
4. Запустите скрипт: `python main.py`.
5. Выберите цифру, соответствующую сети, которую вы хотите проверить (например, 1 для ZkSync).

## Шаг 5: Ожидание Результата

Подождите, пока скрипт завершит свою работу. Он выведет информацию о каждом кошельке в командной строке.

## Шаг 6: Сохранение Результата

1. Выберите формат для сохранения результата: Json, CSV или оба.
2. Следуйте инструкциям в консоли для сохранения результата.

Готово! Теперь у вас есть информация о кошельках в выбранной сети.

# Donate (any EVM) 0x5416dac94ef60a4a1b77f90d90dd148af8789b5b