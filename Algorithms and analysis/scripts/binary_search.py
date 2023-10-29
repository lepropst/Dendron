def binary_search(arr, low, high, x):
    print("PASS")
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
        print(f"HIGH: {high}\tLOW: {low}\tMID: {mid}\tTarget: {x}")
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        # Element is not present in the array
        return -1
 
# Test array
if __name__=="__main__":
    arr = [ 3,6,8,12,19,23,32,44,48,51,62,70,73,74,78,80,85,88 ]

    print("Finding 32:\n\n")
    x = 32
    print(binary_search(arr, 0, len(arr)-1, x))
    print("Finding 79:\n\n")
    x = 79
    print(binary_search(arr, 0, len(arr)-1,x))


 