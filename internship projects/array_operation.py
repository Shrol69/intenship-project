def insert_element(arr, element, position):
    arr.insert(position, element)
    return arr

def delete_element(arr, element):
    if element in arr:
        arr.remove(element)
    else:
        print("Element not found in the array.")
    return arr

def search_element(arr, element):
    try:
        return arr.index(element)
    except ValueError:
        return -1

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def display_array(arr):
    print("Array:", arr)

if __name__ == "__main__":
    array = [10, 20, 30, 40, 50]
    print("Initial Array:")
    display_array(array)

    # Insertion
    element_to_insert = 25
    position_to_insert = 2
    array = insert_element(array, element_to_insert, position_to_insert)
    print(f"\nAfter inserting {element_to_insert} at position {position_to_insert}:")
    display_array(array)

    # Deletion
    element_to_delete = 30
    array = delete_element(array, element_to_delete)
    print(f"\nAfter deleting {element_to_delete}:")
    display_array(array)

    # Searching
    element_to_search = 40
    index = search_element(array, element_to_search)
    if index != -1:
        print(f"\nElement {element_to_search} found at index {index}.")
    else:
        print(f"\nElement {element_to_search} not found in the array.")

    # Sorting
    print("\nArray before sorting:")
    display_array(array)
    array = bubble_sort(array)
    print("Array after sorting:")
    display_array(array)
