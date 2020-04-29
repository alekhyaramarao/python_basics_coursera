import numpy as np
numTCs = int(input())
result = []
timeList = []
for i in range(numTCs):
    numActivity = int(input())
    activities = []
    for a in range(numActivity):
        temp = [int(act) for act in input().split()]
        activities.append(temp)
        for item in temp:
            timeList.append(item)

    x=np.argmin(timeList)
    y=np.argmax((timeList))
    if(x==y-1):
        print("Impossible")
    # for j in range(len(activities)):

    # print("Case #" + str(i + 1) + ": " + result)