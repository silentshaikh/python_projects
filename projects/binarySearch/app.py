import random,time
def naive_search(l,target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1



def binarySearch(l,target,low=None,high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l)-1
    if high<low:
        return -1
    midPoint = (low+high) // 2
    # midPoint = len(l) // 2
    if l[midPoint] == target:
        return midPoint
    elif target < l[midPoint]:
        return binarySearch(l,target,low,midPoint-1)
    else:
        return binarySearch(l,target,midPoint+1,high)
    
if __name__ == "__main__":

    # lists = [1,3,5,10,12]
    # target = 10
    # print(naive_search(lists,target))
    # print(binarySearch(lists,target))

    length = 1000
    sortedList = set()
    while len(sortedList) < length:
        sortedList.add(random.randint(-3*length,3*length))
    sortedList = sorted(list(sortedList))

    start = time.time()
    for target in sortedList:
        naive_search(sortedList,target)
    end = time.time()
    print("Naive Search Time : ",(end-start)/length," seconds")

    start = time.time()
    for target in sortedList:
        binarySearch(sortedList,target)
    end = time.time()
    print("BInary Search Time : ",(end-start)/length," seconds")