def selection_sort(list):
    if len(list) == 0:
        return []
    
    min_element = min(list)
    list.remove(min_element)

    result = selection_sort(list)
    result.insert(0, min_element)
    return result

print(selection_sort([7,6,4,-1,0]))