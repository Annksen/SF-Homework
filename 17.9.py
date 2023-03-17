array = [int(x) for x in input("Введите числа от 0 до 99: ").split()]

# сортировка методом пузырек
def sort_array(a):
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

# алгоритм двоичного поиска

def binary_search(a, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if a[middle] == element:
        return middle
    elif element < a[middle]:
        return binary_search(a, element, left, middle - 1)
    else:
        return binary_search(a, element, middle + 1, right)


while True:
    try:
        element = int(input("Введите любое число: "))
        if element < 0 or element > 99:
            raise Exception
        break
    except ValueError:
        print("Введите число!")
    except Exception:
        print("Неправильный диапазон, попробуйте еще раз!")

print(sort_array(array))
print(binary_search(array, element, 0, len(array)))
