def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [34, 2, 200, 15, 56, 87, 28, 70, 23, 89]
print(f"Tabelnya sebelum sorting: {arr}")

sorted_arr = bubble_sort(arr)
print(f"Tabelnya setelah sorting: {sorted_arr}")