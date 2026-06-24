# 1. Найти и занести в массив сто простых чисел.
# Числа напечатать по 10 штук в строке.

def task1():
    primes = []
    n = 2

    while len(primes) < 100:
        ok = True

        for d in range(2, int(n ** 0.5) + 1):
            if n % d == 0:
                ok = False
                break

        if ok:
            primes.append(n)

        n += 1

    return primes


primes = task1()

for i in range(0, len(primes), 10):
    print(*primes[i:i + 10])


# 2. Дано натуральное число P. Получить его двоичное представление.

def task2(p):
    return bin(p)[2:]


p = 25
print(task2(p))


# 3. Даны строки S1 и S2.
# Удалить из S1 каждый символ, принадлежащий S2.

def task3(s1, s2):
    result = ""

    for ch in s1:
        if ch not in s2:
            result += ch

    return result


s1 = "программирование"
s2 = "гр"
print(task3(s1, s2))


# 4. Дан файл, компоненты которого являются действительными числами.
# Найти наибольшее из значений компонента.

def task4(filename):
    with open(filename, "r", encoding="utf-8") as f:
        nums = [float(x) for x in f.read().split()]

    return max(nums)


filename = "numbers.txt"
print(task4(filename))


# 5. Среди N целых чисел найти такое,
# в двоичной записи которого максимальное число единиц.

def task5(nums):
    answer = nums[0]

    for x in nums:
        if bin(x).count("1") > bin(answer).count("1"):
            answer = x

    return answer


nums = [5, 7, 8, 15, 10]
print(task5(nums))


# 6. Дана вещественная прямоугольная матрица.
# Определить произведение элементов в строках, которые не содержат нулей.

def task6(matrix):
    result = []

    for row in matrix:
        if 0 not in row:
            p = 1

            for x in row:
                p *= x

            result.append(p)

    return result


matrix = [
    [1.5, 2.0, 3.0],
    [4.0, 0.0, 6.0],
    [2.0, 3.0, 4.0]
]

print(task6(matrix))


# 7. Дана вещественная прямоугольная матрица.
# Определить локальные минимумы матрицы.

def task7(matrix):
    result = []
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        for j in range(m):
            neighbors = []

            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0:
                        continue

                    ni = i + di
                    nj = j + dj

                    if 0 <= ni < n and 0 <= nj < m:
                        neighbors.append(matrix[ni][nj])

            if all(matrix[i][j] < x for x in neighbors):
                result.append(matrix[i][j])

    return result


matrix = [
    [5, 3, 8],
    [4, 1, 6],
    [7, 2, 9]
]

print(task7(matrix))


# 8. Дано натуральное число N.
# Сколько различных цифр встречается в его записи.

def task8(n):
    return len(set(str(n)))


n = 12332145
print(task8(n))


# 9. Дан текст.
# Удалить среднюю букву из слов, имеющих нечетную длину.

def task9(text):
    result = []

    for word in text.split():
        if len(word) % 2 == 1:
            mid = len(word) // 2
            word = word[:mid] + word[mid + 1:]

        result.append(word)

    return " ".join(result)


text = "мама домик окно программирование"
print(task9(text))


# 10. Дан текст.
# Найти все слова, в которых доля букв а и б максимальна.

def task10(text):
    words = text.split()
    max_part = -1
    result = []

    for word in words:
        w = word.lower()
        part = (w.count("а") + w.count("б")) / len(w)

        if part > max_part:
            max_part = part
            result = [word]
        elif part == max_part:
            result.append(word)

    return result


text = "мама баба дом арбуз аббат"
print(task10(text))


# 11. Дана вещественная прямоугольная матрица.
# Уплотнить матрицу, удалив строки и столбцы, заполненные нулями.

def task11(matrix):
    rows = []
    cols = []

    for i in range(len(matrix)):
        if any(x != 0 for x in matrix[i]):
            rows.append(i)

    for j in range(len(matrix[0])):
        if any(matrix[i][j] != 0 for i in range(len(matrix))):
            cols.append(j)

    result = []

    for i in rows:
        row = []

        for j in cols:
            row.append(matrix[i][j])

        result.append(row)

    return result


matrix = [
    [0, 0, 0, 0],
    [0, 1, 2, 0],
    [0, 3, 4, 0],
    [0, 0, 0, 0]
]

print(task11(matrix))


# 12. Дан текст, состоящий из слов.
# Исключить повторное вхождение слов в текст.

def task12(text):
    used = []
    result = []

    for word in text.split():
        if word not in used:
            used.append(word)
            result.append(word)

    return " ".join(result)


text = "мама мыла раму мама раму"
print(task12(text))


# 13. Дана целочисленная квадратная матрица.
# Найти номера строк, все элементы которых четны.

def task13(matrix):
    result = []

    for i in range(len(matrix)):
        if all(x % 2 == 0 for x in matrix[i]):
            result.append(i + 1)

    return result


matrix = [
    [2, 4, 6],
    [1, 2, 4],
    [8, 10, 12]
]

print(task13(matrix))


# 14. Построить строку символов,
# являющуюся записью действительного числа в десятичной системе счисления.

def task14(x):
    return str(x)


x = 12.345
print(task14(x))


# 15. Дан текст.
# Поменять в нем первое слово с последним.

def task15(text):
    words = text.split()

    if len(words) > 1:
        words[0], words[-1] = words[-1], words[0]

    return " ".join(words)


text = "первое второе третье последнее"
print(task15(text))


# 16. Дан текст.
# Выдать слова, содержащие максимальное количество гласных букв.

def task16(text):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    words = text.split()
    max_count = -1
    result = []

    for word in words:
        count = 0

        for ch in word:
            if ch in vowels:
                count += 1

        if count > max_count:
            max_count = count
            result = [word]
        elif count == max_count:
            result.append(word)

    return result


text = "кот машина образование дом"
print(task16(text))


# 17. Дана вещественная прямоугольная матрица.
# Если элемент строки на главной диагонали меньше 0,
# изменить порядок строки на обратный, иначе упорядочить строку.

def task17(matrix):
    for i in range(len(matrix)):
        if i < len(matrix[i]) and matrix[i][i] < 0:
            matrix[i] = matrix[i][::-1]
        else:
            matrix[i].sort()

    return matrix


matrix = [
    [3, 1, 2],
    [4, -5, 6],
    [9, 7, 8]
]

print(task17(matrix))


# 18. Дан файл.
# Поменять местами первые пять записей с последними.

def task18(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = f.read().split()

    if len(data) >= 10:
        first = data[:5]
        middle = data[5:-5]
        last = data[-5:]
        data = last + middle + first

    with open(filename, "w", encoding="utf-8") as f:
        f.write(" ".join(data))

    return data


filename = "data.txt"
print(task18(filename))


# 19. Напечатать все трехзначные числа.

def task19():
    return list(range(100, 1000))


print(task19())


# 20. Дана вещественная прямоугольная матрица.
# Определить произведение элементов в строках без нулей.

def task20(matrix):
    result = []

    for row in matrix:
        if 0 not in row:
            p = 1

            for x in row:
                p *= x

            result.append(p)

    return result


matrix = [
    [2, 3, 4],
    [1, 0, 5],
    [3, 3, 3]
]

print(task20(matrix))


# 21. Дана вещественная прямоугольная матрица.
# Определить номер первой строки, содержащей хотя бы один нулевой элемент.

def task21(matrix):
    for i in range(len(matrix)):
        if 0 in matrix[i]:
            return i + 1

    return -1


matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]

print(task21(matrix))


# 22. Дан целочисленный массив.
# В начале расположить отрицательные элементы, остальные в конец.

def task22(arr):
    result = []

    for x in arr:
        if x < 0:
            result.append(x)

    for x in arr:
        if x >= 0:
            result.append(x)

    return result


arr = [3, -1, 5, -7, 0, -2, 4]
print(task22(arr))


# 23. Дан массив целых чисел.
# Вывести номер числа, наиболее часто встречающегося в массиве.

def task23(arr):
    answer = arr[0]
    max_count = arr.count(answer)

    for x in arr:
        count = arr.count(x)

        if count > max_count:
            max_count = count
            answer = x

    return arr.index(answer) + 1


arr = [1, 3, 2, 3, 4, 3, 2]
print(task23(arr))
