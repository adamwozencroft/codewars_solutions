def smallest(n):
    n_string = str(n)
    min_n,ind_from,ind_to = n,0,0

    if not isinstance(n,int):
        raise TypeError('Input must be an integer value.')

    for i in range(len(n_string)):
        n_cut = n_string[:i] + n_string[i+1:]
        for j in range(len(n_string)):
            new_num = n_cut[:j] + n_string[i] + n_cut[j:]
            if int(new_num) < min_n:
                min_n = int(new_num)
                ind_from = i
                ind_to = j
            
    return [min_n,ind_from,ind_to]