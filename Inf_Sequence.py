from itertools import count


def finder(number):

    def calc_index(num):
        rank = len(str(num))
        return 1 + rank * (num - 10 ** (rank - 1)) + sum([9 * i * 10 ** (i - 1) for i in range(1, rank)])

    def num_gen(num):
        for n in count(num):
            for d in str(n): yield d

    while 1:
        ret = 4988888888888888888888888888888888888888888888888890
        n = len(number)
        I = n + 1
        if number == '12345678910111213141516171819202122232425262728293'[:n]:
            return 1
        if number == n * '0':
            return calc_index(int('1' + number)) + 1
        for i in range(1, n + 1):
            if I < i: break
            for j in range(i):
                if number[j] != '0':
                    R = int(number[j:i])
                    if j: L = int(number[:j])
                    else: L = 0
                    expect_num= R * 10**j + L + 1
                    if (L + 1) / 10**j == 1:
                        if R / 10**i == 1:
                            expect_num = R
                        else:
                            expect_num = (R - 1) * 10**j + L + 1
                    gen = num_gen(expect_num)
                    for d in number[j:]:
                        if d != next(gen):
                            expect_num = 0
                            break
                    if expect_num:
                        I = i
                        ret = min(ret, calc_index(expect_num) - j)
        return ret

if __name__ == '__main__':
    while 1:
        x = input()
        if x == '' or x[0] not in '0123456789': break
        print(finder(x))

