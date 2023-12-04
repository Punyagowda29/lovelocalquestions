def findElements(arr):
    result = [] #result in list
    freq = {} #dictionery freq
    for i in arr: #traverse the arr
        if i in freq: #if the element in i is present in freq then add 1 or increment it by 1
            freq[i] += 1
        else:
            freq[i] = 1 #if not already present in freq then create new key value pair assigning the value 1
    limit = len(arr)/3  #calculate limit
    for key in freq:
        if freq[key] > limit:   # check each key in freq with limits
            result.append(key) #append the value to result list
    return result

n = int(input("Enter the num of elements: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter {i+1} element: ")))
print(findElements(arr)) #call function findElements
