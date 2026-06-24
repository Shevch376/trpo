# 1
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

for i in range(0, 100, 10):
    print(*primes[i:i + 10])


# 2
p = 25
print(bin(p)[2:])


# 3
s1 = "программирование"
s2 = "гр"
print("".join(ch for ch in s1 if ch not in s2))


# 4
filename = "numbers.txt"

with open(filename, "r", encoding="utf-8") as f:
    nums = [float(x) for x in f.read().split()]

print(max(nums))


# 5
nums = [5, 7, 8, 15, 10]
answer = nums[0]

for x in nums:
    if bin(x).count("1") > bin(answer).count("1"):
        answer = x

print(answer)


# 6
matrix = [
    [1.5, 2.0, 3.0],
    [4.0, 0.0, 6.0],
    [2.0, 3.0, 4.0]
]

for row in matrix:
    if 0 not in row:
        p = 1
        for x in row:
            p *= x
        print(p)


# 7
matrix = [
    [5, 3, 8],
    [4, 1, 6],
    [7, 2, 9]
]

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
            print(matrix[i][j])


# 8
n = 12332145
print(len(set(str(n))))


# 9
text = "мама домик окно программирование"
result = []

for word in text.split():
    if len(word) % 2 == 1:
        mid = len(word) // 2
        word = word[:mid] + word[mid + 1:]
    result.append(word)

print(" ".join(result))


# 10
text = "мама баба дом арбуз аббат"
words = text.split()

max_part = -1
answer = []

for word in words:
    w = word.lower()
    part = (w.count("а") + w.count("б")) / len(w)

    if part > max_part:
        max_part = part
        answer = [word]
    elif part == max_part:
        answer.append(word)

print(answer)


# 11
matrix = [
    [0, 0, 0, 0],
    [0, 1, 2, 0],
    [0, 3, 4, 0],
    [0, 0, 0, 0]
]

rows = [i for i in range(len(matrix)) if any(x != 0 for x in matrix[i])]
cols = [j for j in range(len(matrix[0])) if any(matrix[i][j] != 0 for i in range(len(matrix)))]

new_matrix = [[matrix[i][j] for j in cols] for i in rows]
print(new_matrix)


# 12
text = "мама мыла раму мама раму"
used = []
result = []

for word in text.split():
    if word not in used:
        used.append(word)
        result.append(word)

print(" ".join(result))


# 13
matrix = [
    [2, 4, 6],
    [1, 2, 4],
    [8, 10, 12]
]

for i in range(len(matrix)):
    if all(x % 2 == 0 for x in matrix[i]):
        print(i + 1)


# 14
x = 12.345
s = str(x)
print(s)


# 15
text = "первое второе третье последнее"
words = text.split()

if len(words) > 1:
    words[0], words[-1] = words[-1], words[0]

print(" ".join(words))


# 16
text = "кот машина образование дом"
vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
words = text.split()

max_count = -1
answer = []

for word in words:
    count = sum(1 for ch in word if ch in vowels)

    if count > max_count:
        max_count = count
        answer = [word]
    elif count == max_count:
        answer.append(word)

print(answer)


# 17
matrix = [
    [3, 1, 2],
    [4, -5, 6],
    [9, 7, 8]
]

for i in range(len(matrix)):
    if matrix[i][i] < 0:
        matrix[i] = matrix[i][::-1]
    else:
        matrix[i].sort()

print(matrix)


# 18
filename = "data.txt"

with open(filename, "r", encoding="utf-8") as f:
    data = f.read().split()

if len(data) >= 10:
    first = data[:5]
    middle = data[5:-5]
    last = data[-5:]
    data = last + middle + first

with open(filename, "w", encoding="utf-8") as f:
    f.write(" ".join(data))

print(data)


# 19
for n in range(100, 1000):
    print(n)


# 20
matrix = [
    [2, 3, 4],
    [1, 0, 5],
    [3, 3, 3]
]

for row in matrix:
    if 0 not in row:
        p = 1
        for x in row:
            p *= x
        print(p)


# 21
matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]

answer = -1

for i in range(len(matrix)):
    if 0 in matrix[i]:
        answer = i + 1
        break

print(answer)


# 22
arr = [3, -1, 5, -7, 0, -2, 4]
result = []

for x in arr:
    if x < 0:
        result.append(x)

for x in arr:
    if x >= 0:
        result.append(x)

print(result)


# 23
arr = [1, 3, 2, 3, 4, 3, 2]

answer = arr[0]
max_count = arr.count(answer)

for x in arr:
    count = arr.count(x)
    if count > max_count:
        max_count = count
        answer = x

index = arr.index(answer) + 1

print("Число:", answer)
print("Номер:", index)
