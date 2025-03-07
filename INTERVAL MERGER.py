def addInterval(intervals, start, end):
    merged, inserted = [], False
    for i in intervals:
        if i[1] < start:
            merged.append(i)
        elif i[0] > end:
            if not inserted:
                merged.append([start, end])
                inserted = True
            merged.append(i)
        else:
            start, end = min(start, i[0]), max(end, i[1])
    if not inserted:
        merged.append([start, end])
    return merged

def getIntervals(intervals):
    return intervals

intervals = []
while True:
    n=int(input("enter number \n1.add interval\n2.getinterval\n"))
    if(n==1):
        start, end = map(int, input("Enter interval (start end): ").split())
        intervals = addInterval(intervals, start, end)
    elif(n==2):
        print(getIntervals(intervals))
    else:
        break
