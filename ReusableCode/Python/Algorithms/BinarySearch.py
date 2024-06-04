# Binary Search (**list needs to be sorted ascendingly first to use this**)
def BinarySearch(l, target):
    index = [i for i in range(len(l))]
    while True:
        midIndex = int (len(l) /2)
        if len(l) == 0:
            return 'Not found'
        else:
            if l[midIndex] == target:
                return index[midIndex]
            elif l[midIndex] > target:
                l = l[:midIndex]
                index = index[:midIndex]
            else:
                l = l[midIndex + 1:]
                index = index[midIndex + 1:]
                