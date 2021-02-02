def binary_search(element, some_list):
    start, end = 0, len(some_list)-1
    
    while start != end:
        mid = (start + end) // 2    
        if start == mid or end == mid:
            if element == some_list[start]:
                return start
            elif element == some_list[end]:
                return end
            else:
                return None
        if element > some_list[mid]:
            start = mid
        elif element < some_list[mid]:
            end = mid
        else:
            return mid
        
    return None