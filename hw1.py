def abc(arr,m,n):
    if m == n:
        print(arr)
    else:   
        for l in range(m, n + 1):
            temp = arr[m]
            arr[m] = arr[l]
            arr[l] = temp
            abc(arr, m+1, n)
            temp = arr[m]
            arr[m] = arr[l]
            arr[l] = temp

word = input()
n = len(word)
arr = list(word)
abc(arr, 0, n-1)
