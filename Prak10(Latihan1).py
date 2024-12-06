def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            left = mid + 1  
        else:
            right = mid - 1  
    return -1  

def main():
    print("Ini merupakan program Binary Search")
    try:
        arr = [34, 2, 200, 15, 56, 87, 28, 70, 23, 89]
        print(f"Tabelnya sebelum sorting: {arr}")

        sorted_arr = bubble_sort(arr)
        print(f"Tabelnya setelah sorting: {sorted_arr}")

        target = input("Masukkan Angka: ").strip()

        if target == "":
            print("Program Selesai")
            return

        target = int(target)
        print(f"Targetnya: {target}")

        result = binary_search(sorted_arr, target)
        if result != -1:
            print(f"Elemen {target} ditemukan pada indeks {result}.")
        else:
            print(f"Elemen {target} tidak ditemukan dalam list setelah sorting.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

main()