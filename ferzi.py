import random

def main():
    lst_alpha = []
    lst_digit = []

    def get_alpha(alphabet: list) -> list:
        eff = 0
        while eff < 8:
            ran_alpha = chr(random.randint(ord('a'), ord('h')))
            for i in ran_alpha:
                eff += 1
                alphabet.append(ran_alpha)
        return alphabet
    a = get_alpha(lst_alpha)
    #print(a)

    def get_digit(number: list) -> list:
        eff = 0
        while eff < 8:
            for i in range(1, 9):
                eff += 1
                number.append(random.randint(1,8))
        return number
    b = get_digit(lst_digit)
    c = list(map(str, b))
    #print(b)

    #print(a,c)
    lst_1 = a[0] + c[0]
    #print(lst_1)
    lst_2 = a[1] + c[1]
    #print(lst_2)
    lst_3 = a[2] + c[2]
    #print(lst_3)
    lst_4 = a[3] + c[3]
    #print(lst_4)
    lst_5 = a[4] + c[4]
    #print(lst_5)
    lst_6 = a[5] + c[5]
    #print(lst_6)
    lst_7 = a[6] + c[6]
    #print(lst_7)
    lst_8 = a[7] + c[7]
    #print(lst_8)

    if lst_1 == lst_2 or lst_1 == lst_3 or lst_1 == lst_4 or lst_1 == lst_5 or lst_1 == lst_6 or lst_1 == lst_7 or lst_1 == lst_8 :

        main()
    elif lst_2 == lst_3 or lst_2 == lst_4 or lst_2 == lst_5 or lst_2 == lst_6 or lst_2 == lst_7 or lst_2 == lst_8 :
        main()
    elif lst_3 == lst_4 or lst_3 == lst_5 or lst_3 == lst_6 or lst_3 == lst_7 or lst_3 == lst_8:
        main()
    elif lst_4 == lst_5 or lst_4 == lst_6 or lst_4 == lst_7 or lst_4 == lst_8:
        main()
    elif lst_5 == lst_6 or lst_5 == lst_7 or lst_5 == lst_8:
        main()
    elif lst_6 == lst_7 or lst_6 == lst_8:
        main()
    elif lst_7 == lst_8:
        main()
    else:
        print(f'{lst_1}\n{lst_2}\n{lst_3}\n{lst_4}\n{lst_5}\n{lst_6}\n{lst_7}\n{lst_8}\n')

    def get_check(first, second, third, fourth, fifth, sixth, seventh, eighth):
        a = int(''.join(filter(str.isdigit, first)))
        print(a)
        b = int(''.join(filter(str.isdigit, second)))
        print(b)
        c = int(''.join(filter(str.isdigit, third)))
        print(c)
        d = int(''.join(filter(str.isdigit, fourth)))
        print(d)
        e = int(''.join(filter(str.isdigit, fifth)))
        print(e)
        g = int(''.join(filter(str.isdigit, sixth)))
        print(g)
        f = int(''.join(filter(str.isdigit, seventh)))
        print(f)
        i = int(''.join(filter(str.isdigit, eighth)))
        print(i)
        if a == b or a == c or a == d or a == e or a == g or a == f or a == i:
            return 'Бьют друг друга'
        elif b == c or b == d or b == e or b == g or b == f or b == i:
            return 'Бьют друг друга'
        elif c == d or c == e or c == g or c == f or c == i:
            return 'Бьют друг друга'
        elif d == e or d == g or d == f or d == i:
            return 'Бьют друг друга'
        elif e == g or e == f or e == i:
            return 'Бьют друг друга'
        elif g == f or g == i:
            return 'Бьют друг друга'
        elif f == i:
            return 'Бьют друг друга'
        else:
            return 'По горизонтали все чисто'


    check = get_check(lst_1, lst_2, lst_3, lst_4, lst_5, lst_6, lst_7, lst_8)
    print(check)

if __name__ == '__main__':
    main()











