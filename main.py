#problema 1
def get_prim(p):
    '''Verifica daca numarul este prim
    :param :p intreg
    :return: True daca este prim sau False daca nu
    '''
    if p<2:
        return 0
    else:
        for div in range(2,p//2+1):
            if p%div==0:
                return 0
    return 1

def test_get_prim():
    assert get_prim(3)==1
    assert get_prim(6)==0

def get_largest_prime_below(n):
    '''Verifica care este cel mai mare numar prim mai mic decat un numar dat
    : param: n : nr intreg
    :return: i: cel mai mare nr prim mai mic decat n
    '''
    for i in range(1,n):
        p=n-i
        if get_prim(p)==1:
            return p


def test_get_largest_prime_below() :
    assert get_largest_prime_below(12)==11
    assert get_largest_prime_below(20)==19
    assert get_largest_prime_below(7)==5

#problema 14
def get_cmmmc(numbers):
    '''Calculeaza cmmmc a n numere
        :param: numbers: lista de nr intregi
        :return: cmmmc
    '''
    global m
    x = numbers[0]
    i = 1
    while i < len(numbers):
        y = numbers[i]
        a = x
        b = y
        while x != y:
            if x > y:
                x =x - y
            else:
                y =y - x
        m = a * b / x
        x = m
        i = i + 1
    return m



def test_get_cmmmc():
    assert get_cmmmc([1, 2, 3]) == 6
    assert get_cmmmc([2, 3, 4]) == 12
    assert get_cmmmc([12,1,24])==24
    assert get_cmmmc([1,1,1])==1

#Prblema 5
def is_palindrome(n):
    '''Verifica daca un numar este palindrom
    :param: n: un numar intreg
    :return: true daca numarul este palindrom si false in rest '''
    aux=n
    pal=0
    while n>0:
        ultima_cifra=n%10
        pal=pal*10+ultima_cifra
        n=n//10
    if aux==pal:
        return True
    return False
def test_is_palindrome():
    assert is_palindrome(12321)==True
    assert is_palindrome(1123) == False
    assert is_palindrome(232) == True



def meniu():
    print('''introduceti:
    1 pentru problema 1
    2 pentru problema 14
    3 pentru problema 5
    x pentru a inchide''')

def main():
    # interfata de tip consola aici
    test_get_prim()
    test_get_largest_prime_below()
    test_get_cmmmc()
    test_is_palindrome()
    numbers = []
    while True:
        meniu()
        cmd = input("Comanda:")
        if cmd == '1':
            n = int(input("introduceti un numar intreg n"))
            if n <= 3:
                print("nu exista niciun nr prim mai mic decat", n)
            else:
                print(get_largest_prime_below(n))

        elif cmd == '2':
            n = int(input("pentru cate numere se va afisa cmmdc?"))
            for x in range(n):
                elem = int(input("introduceti un numar"))
                numbers.append(elem)
            print(get_cmmmc(numbers))
        elif cmd == '3':
            n = int(input("introduceti un numar posibil palindrom  "))
            print(is_palindrome(n))
        elif cmd == 'x':
            break
        else:
            print('comanda invalida')

if __name__ == '__main__':
    main()



