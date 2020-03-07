


def reverseArray(array, start, end):
    temp = 0
    if (start >= end):
        return
    reverseArray(array, start+1, end-1)
    temp = array[start]
    array[start] = array[end]
    array[end] = temp

def printArray(array, size):
    for x in range(size):
        output = "{} is the value at index {}"
        print(output.format(array[x], x))


array = [1, 2, 3, 4, 5, 6]
print("Original array: \n")
printArray(array, len(array))
reverseArray(array, 0, len(array)-1)
print("Reversed Array: \n")
printArray(array, len(array))