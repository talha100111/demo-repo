def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1
    while begin_index < end_index:
        midpoint_index = (begin_index + end_index) // 2
        midpoint_value = sequence[midpoint_index]
        
        if midpoint_value == item:
            return midpoint_index
        
        elif midpoint_value < item:
            begin_index = begin_index + 1

        else:
            end_index = end_index - 1

        
    return None


print(binary_search([1,2,3,4,5,6,7,8,9,10], 8))