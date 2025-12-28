import timeit

# 1. Алгоритм Боєра-Мура
def build_shift_table(pattern):
    table = {}
    length = len(pattern)
    for i in range(length - 1):
        table[pattern[i]] = length - 1 - i
    return table

def boyer_moore_search(text, pattern):
    shift_table = build_shift_table(pattern)
    i = 0
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i
        else:
            i += shift_table.get(text[i + len(pattern) - 1], len(pattern))
    return -1

# 2. Алгоритм Кнута-Морріса-Пратта (KMP)
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)
    lps = compute_lps(pattern)
    i = j = 0
    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        if j == M:
            return i - j
        elif i < N and pattern[j] != main_string[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

# 3. Алгоритм Рабіна-Карпа
def rabin_karp_search(main_string, pattern):
    d = 256
    q = 101
    M = len(pattern)
    N = len(main_string)
    p = 0
    t = 0
    h = 1
    if M > N: return -1

    for i in range(M - 1):
        h = (h * d) % q

    for i in range(M):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(main_string[i])) % q

    for i in range(N - M + 1):
        if p == t:
            if main_string[i:i + M] == pattern:
                return i
        if i < N - M:
            t = (d * (t - ord(main_string[i]) * h) + ord(main_string[i + M])) % q
            if t < 0:
                t = t + q
    return -1

# Функція для зчитування файлів
def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
        return ""

# --- Основна частина ---
if __name__ == "__main__":
    # Зчитуємо тексти з файлів
    text1 = read_file("стаття 1.txt")
    text2 = read_file("стаття 2 (1).txt")

    if text1 and text2:
        # Визначаємо підрядки
        substrings = {
            "text1": {"existing": "алгоритми", "fake": "трансформатор"},
            "text2": {"existing": "рекомендаційної", "fake": "синхрофазотрон"}
        }

        algorithms = [
            ("Boyer-Moore", boyer_moore_search),
            ("KMP", kmp_search),
            ("Rabin-Karp", rabin_karp_search)
        ]

        print(f"{'Algorithm':<15} | {'Text':<10} | {'Type':<10} | {'Time (sec)':<15}")
        print("-" * 60)

        for name, func in algorithms:
            # Тест для статті 1
            time_exist_1 = timeit.timeit(lambda: func(text1, substrings["text1"]["existing"]), number=10)
            time_fake_1 = timeit.timeit(lambda: func(text1, substrings["text1"]["fake"]), number=10)
            
            # Тест для статті 2
            time_exist_2 = timeit.timeit(lambda: func(text2, substrings["text2"]["existing"]), number=10)
            time_fake_2 = timeit.timeit(lambda: func(text2, substrings["text2"]["fake"]), number=10)

            print(f"{name:<15} | Text 1     | Existing   | {time_exist_1:.5f}")
            print(f"{name:<15} | Text 1     | Fake       | {time_fake_1:.5f}")
            print(f"{name:<15} | Text 2     | Existing   | {time_exist_2:.5f}")
            print(f"{name:<15} | Text 2     | Fake       | {time_fake_2:.5f}")
            print("-" * 60)
    else:
        print("Помилка: не вдалося завантажити тексти для аналізу.")
