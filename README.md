# Graphic Calculator


## Установка

### Windows
```bash
git clone https://github.com/tt0tem4ik22-archuser/Graphic-Calculator
pip install -r requirements.txt
cd Graphic-Calculator
```

### Linux | MacOS
```bash
git clone https://github.com/tt0tem4ik22-archuser/Graphic-Calculator
python3 -m pip install -r requirements.txt
cd Graphic-Calculator
```


## Создание виртуальной среды проекта (опционально)

### Windows
```bash
python -m venv .venv
.venv\Scripts\activate.bat
```

### Linux | MacOS
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Запуск программы

### Windows
```bash
python main.py
```

### Linux | MacOS
```bash
python3 main.py
```


## Использование

* Сначала программа получает количество уравнений в системе уравнений
    * По умолчанию программа обрабатывает одиночное уравнение
    * Любая ошибка ввода ведёт к обработке уравнений по умолчанию
    * Если вам нужно решить одно уравнение не в системе, то в системе одно уравнение
* При вводе уравнений важно соблюдать несколько правил, их игнорирование может привести к падению программы или некорректной работе
    * Программа принимает уравнения в виде ay-bx, равное нулю.
    * Разрешаются ТОЛЬКО буквы 'x' и 'y', регистер не важен
    * Умножение записывается только через звёздочку 
    * Степень записывается в виде a**b, 
        * a - основание, b - индекс
    * Для обозначения порядка действий можно использовать скобки
```
Хороший пример: '2*y-4*x+7'
Плохой пример: '4z-12 = 3i'
```