def get_closest_to_zero(a):
    abs_a = [abs(i) for i in a]
    closest_val = min(abs_a)
    closest_zero_list = [val for i, val in enumerate(a) if abs_a[i] == closest_val]
    return closest_zero_list
    