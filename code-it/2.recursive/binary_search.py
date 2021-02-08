def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1
    
    search_index = (start_index + end_index) // 2

    if search_index == start_index or search_index == end_index:
        if some_list[start_index] == element:
            return search_index
        elif some_list[end_index] == element:
            return end_index
        else:
            return None

    if element == some_list[search_index]:
        return search_index
    else:
        if element < some_list[search_index]:
            return binary_search(element, some_list, start_index, search_index)
        else:
            return binary_search(element, some_list, search_index, end_index)
    


print(binary_search(11, [2, 3, 5, 7, 11]))
