
def bubbleSort(arr):
    
    #iterates through the entire array
    for r in range(0,len(arr)-1):
        #iterates through only up through how many needs to be checked
        for c in range(0, len(arr)-r-1):
            #checks if current is greather than next
            if arr[c]> arr[c+1]:
                #if it is then swap the values.
                arr[c], arr[c+1] = arr[c+1], arr[c];
    #return the array.
    return arr


nums= [8,6,100,200,3]
print(bubbleSort(nums))
