def solution(n):
    num_to_sym = {
        1000:'M',
        900:'CM',
        500:'D',
        400:'CD',
        100:'C',
        90:'XC',
        50:'L',
        40:'XL',
        10:'X',
        9:'IX',
        5:'V',
        4:'IV',
        1:'I',
    }
    sym = ""
    
    if not isinstance(n,int):
        raise TypeError('Error: Input year must be an integer.')

    for num in num_to_sym:
        rep = n // num
        if rep >= 1:
            for i in range(rep):
                sym += num_to_sym[num]
                n -= num
    return sym