# Ascending MergeSort
def mergesortasc(l):
    if len(l) > 1:
        mid = int (len(l)/2)
        leftHalf = l[:mid]
        rightHalf = l[mid:]

        mergesortasc(leftHalf)
        mergesortasc(rightHalf)

        leftIndex,rightIndex,mergeIndex = 0,0,0

        mergeList = l
        #print(leftHalf,rightHalf)
        while leftIndex < len(leftHalf) and rightIndex < len(rightHalf):
            if leftHalf[leftIndex] < rightHalf[rightIndex]:
                mergeList[mergeIndex] = leftHalf[leftIndex]
                leftIndex+=1       
            else:
                mergeList[mergeIndex] = rightHalf[rightIndex]
                rightIndex+=1
            mergeIndex+=1

        # Handle those items still left in the left Half
        while leftIndex < len(leftHalf):
            mergeList[mergeIndex] = leftHalf[leftIndex]
            leftIndex+=1
            mergeIndex+=1
        # Handle those items still left in the right Half
        while rightIndex < len(rightHalf):
            mergeList[mergeIndex] = rightHalf[rightIndex]
            rightIndex+=1
            mergeIndex+=1
        return mergeList
    else:
        return l

# Descending MergeSort
def mergesortdesc(l):
    if len(l) > 1:
        mid = int (len(l)/2)
        leftHalf = l[:mid]
        rightHalf = l[mid:]

        mergesortdesc(leftHalf)
        mergesortdesc(rightHalf)

        leftIndex,rightIndex,mergeIndex = 0,0,0

        mergeList = l
        #print(leftHalf,rightHalf)
        while leftIndex < len(leftHalf) and rightIndex < len(rightHalf):
            if leftHalf[leftIndex] > rightHalf[rightIndex]:
                mergeList[mergeIndex] = leftHalf[leftIndex]
                leftIndex+=1       
            else:
                mergeList[mergeIndex] = rightHalf[rightIndex]
                rightIndex+=1
            mergeIndex+=1

        # Handle those items still left in the left Half
        while leftIndex < len(leftHalf):
            mergeList[mergeIndex] = leftHalf[leftIndex]
            leftIndex+=1
            mergeIndex+=1
        # Handle those items still left in the right Half
        while rightIndex < len(rightHalf):
            mergeList[mergeIndex] = rightHalf[rightIndex]
            rightIndex+=1
            mergeIndex+=1
        return mergeList
    else:
        return l