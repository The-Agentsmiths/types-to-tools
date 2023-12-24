import datetime

# fibonacci fn
def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

# get tomorrows date
def tomorrow():
    return (datetime.date.today() + datetime.timedelta(days=1)).isoformat()

# mergesort
def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        mergesort(left)
        mergesort(right)
        
        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
        
        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        
        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1

# username and email validation
def validate(username, email):
    if len(username) < 3:
        return False
    if len(email) < 3:
        return False
    return True