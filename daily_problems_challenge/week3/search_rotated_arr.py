# BOUNDARY COnditions were getting wrong
    
def bin_search_rotate(self, arr, el):
    l, r = 0, len(arr)-1
    while l <= r:
        m = l + (r-l)//2
        
        if arr[m] == el:
            return m
        
        if el < arr[m]:
            if arr[m] < arr[r]:
                r = m-1
            else:
                if arr[l] > el:
                    l = m+1 # first half
                else: #part of second half
                    r = m-1
        else:
            if arr[m] > arr[r]: # m is part of second half
                l = m+1
            else: # m is part of first half
                if el <= arr[r]: # part of first half
                    l = m+1
                else:
                    r = m-1 # part of second half
                    
    return -1
                
        
def search(self, nums: list, target: int) -> int:
    return self.bin_search_rotate(nums, target)