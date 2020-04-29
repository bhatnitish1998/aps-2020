# Minimum average waiting time for scheduling the tasks

# Input: array of tasks  in the form [arrivaltime, time required for task]

# Output: Returns the minimum average waiting time


def minimumAverage(tasks):
    n=len(tasks)
    tasks.sort()
    arr=[]
    wait=0
    current=0
    while tasks or arr:
        while tasks and tasks[0][0]<=current:
            bisect.insort(arr,[tasks[0][1],tasks[0][0]])
            tasks.pop(0)
        if arr:
            a=arr.pop(0)
            current+=a[0]
            wait+=current-a[1]
        else:
            bisect.insort(arr,[tasks[0][1],tasks[0][0]])
            tasks.pop(0)
            current=arr[0][1]
            
    return wait//n