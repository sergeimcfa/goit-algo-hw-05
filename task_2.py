def binary_search_fractional(arr, target):
    low = 0
    high = len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (low + high) // 2

        if arr[mid] < target:
            low = mid + 1
        else:
            # Якщо arr[mid] >= target, це потенційна верхня межа.
            # Зберігаємо її і продовжуємо шукати в лівій частині, 
            # щоб знайти ще меншу "верхню межу" (ближчу до target).
            upper_bound = arr[mid]
            high = mid - 1
            
    return (iterations, upper_bound)

# --- Тестування ---
if __name__ == "__main__":
    sorted_floats = [0.1, 1.4, 2.5, 3.6, 4.7, 5.8, 6.9, 8.0]
    target_value = 4.0

    result = binary_search_fractional(sorted_floats, target_value)
    print(f"Масив: {sorted_floats}")
    print(f"Шукаємо число: {target_value}")
    print(f"Результат (ітерації, верхня межа): {result}")
    # Очікується: (3, 4.7) або (4, 4.7) залежно від кроків, верхня межа точно 4.7
