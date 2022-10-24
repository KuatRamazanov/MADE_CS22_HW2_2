def get_closest_to_zero(a):
    abs_a = [abs(j) for j in a]
    closest_zero_list = [val for i, val in enumerate(a) if abs_a[i] == min(abs_a)]
    return closest_zero_list
    
