def reverse(a, x, y): 
    while(x < y): 
        temp = a[x] 
        a[x] = a[y] 
        a[y] = temp 
        x += 1
        y -= 1
  
def sortArr(a, n): 
    x, y = -1, -1
  
    for i in range(n-1): 
        if(a[i] > a[i+1]): 
            if(x == -1): 
                x = i 
            y = i + 1
  
    if(x != -1): 
        reverse(a, x, y) 
        for i in range(n-1): 
            if(a[i] > a[i+1]): 
                return False
  
    return True
  
arr = [1, 2, 5, 4, 3] 
n = len(arr) 
  
if(sortArr(arr, n)): 
    print("Yes") 
else: 
    print("No")

# Initialize two variables x and y with -1.
# Iterate over the array.
# Find the first number for which a[i] > a[i+1] and store it into x. 
# Similarly, Store index i+1 as well into y, As this will keep track of the ending of the subarray which is needed to reverse.
# Check if x == -1 then array is already sorted so return true.
# Otherwise, reverse the array from index x to index y.
# Traverse the array to check for every element is sorted or not.
# If not sorted, return false.
# Finally, return true.