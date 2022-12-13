def get_n(a, q, n):
    if n == 1:
        return a
    return get_n(a, q, n-1) * q
        
def get_digits_a(num: int):
    if num < 1:
        return 0
    return get_digits_a(num/10) + 1
        
def get_suff(n: int):
    if n == 1:
        return 'st'
    elif n == 2:
        return 'nd'
    elif n == 3:
        return 'rd'
    return 'th'
        
def first():
    a = int(input('a = '))
    q = int(input('q = '))
    n = int(input('n = '))
            
    print(f'{n}{get_suff(n)} member = {get_n(a, q, n)}')

def second():
    num = int(input('num = '))
    print(f'Digits amount: {get_digits_a(num)}')
