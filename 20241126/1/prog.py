import sys

data = input().encode("utf-8")  # Получаем ввод через input и преобразуем в байты
N = data[0]  # Первый байт — количество частей
tail = data[1:]  # Оставшаяся часть данных
L = len(tail)  # Длина оставшихся данных

# Разделяем данные на N частей
parts = [tail[round(i * L / N) : round((i + 1) * L / N)] for i in range(N)]

# Сортируем части
parts.sort()

# Объединяем результат и добавляем первый байт
result = bytes([N]) + b"".join(parts)

# Выводим результат
sys.stdout.buffer.write(result)
