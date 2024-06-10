def heapify(arr, n, i, is_max_heap):
    largest_or_smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if is_max_heap:
        if left < n and arr[largest_or_smallest] < arr[left]:
            largest_or_smallest = left
        if right < n and arr[largest_or_smallest] < arr[right]:
            largest_or_smallest = right
    else:
        if left < n and arr[largest_or_smallest] > arr[left]:
            largest_or_smallest = left
        if right < n and arr[largest_or_smallest] > arr[right]:
            largest_or_smallest = right

    if largest_or_smallest != i:
        arr[i], arr[largest_or_smallest] = arr[largest_or_smallest], arr[i]
        heapify(arr, n, largest_or_smallest, is_max_heap)

def heap_sort(arr, is_max_heap=True):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, is_max_heap)
    
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, is_max_heap)

def main():
    array = [12, 11, 13, 5, 6, 7]
    print("Original array:", array)
    
    choice = input("Enter 'max' for max-heap sort or 'min' for min-heap sort: ").strip().lower()
    
    if choice == 'max':
        heap_sort(array, is_max_heap=True)
        print("Sorted array using max-heap:", array)
    elif choice == 'min':
        heap_sort(array, is_max_heap=False)
        print("Sorted array using min-heap:", array)
    else:
        print("Invalid choice. Please enter 'max' or 'min'.")

if __name__ == "__main__":
    main()
