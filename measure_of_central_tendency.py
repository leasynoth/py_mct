# -*- coding: utf-8 -*-

__author__ = 'leasynoth'
__email__ = 'nordiccatsinc@gmail.com'
__DATE__ = '04.06.2022'

'''

    measure of central tendency

'''

def arithmetic_mean(data):

    res = 0

    for elem in data:

        res += elem

    return res/len(data)


def geometric_mean(data):

    res = 1

    for elem in data:

        if (elem > 0):

            res *= elem

    return res ** (1/len(data))


def geometric_mean2(data=[1, 2]):

    res = 0

    for elem in data:

        res += (elem ** 0.5)

    return (res / len(data)) ** (1/0.5)


def quadratic_mean(data):

    res = 0

    for elem in data:

        res += elem ** 2

    return (res / len(data)) ** (1/2)


def harmonic_mean(data):

    res = 0

    for elem in data:

        if (elem > 0):

            res += (1 / elem)

    return (len(data) / res)


def cubic_mean(data):

    res = 0

    for elem in data:

        res += elem ** 3

    return (res / len(data)) ** (1/3)


def winsorized_mean(data):

    res = 0
    data.sort()
    percent = round((len(data) / 100) * 20)
    cutted_data = data[percent:len(data)-percent]

    first_elem = cutted_data[0]
    last_elem = cutted_data[-1]

    for i in range(percent):

        cutted_data.insert(0, first_elem)
        cutted_data.insert(-1, last_elem)

    for elem in cutted_data:

        res += elem

    return res / len(cutted_data)


def trimmed_mean(data):

    res = 0
    data.sort()
    percent = round((len(data) / 100) * 20)
    cutted_data = data[percent:len(data)-percent]

    for elem in cutted_data:

        res += elem

    return res / len(cutted_data)


def mediana(data):

    res = 0
    data.sort()
    half = len(data) // 2

    if ((len(data) % 2) == 1):

        res = data[half]

    elif ((len(data) % 2) == 0):

        res = (data[half-1] + data[half]) / 2

    return res


def moda(data):

    res = 0
    summary_dict = {}

    for elem in data:

        alpha = summary_dict.get(elem)

        if (alpha == None):

            summary_dict.update({elem:1})

        elif (alpha != None):

            summary_dict.update({elem:alpha+1})

    res = max(summary_dict, key=summary_dict.get)

    return res


def main():

    test_data = [_ for _ in range(10)]
    a_m = round(arithmetic_mean(test_data), 1)
    g_m = round(geometric_mean(test_data), 1)
    g_m2 = round(geometric_mean2(test_data), 1)
    q_m = round(quadratic_mean(test_data), 1)
    h_m = round(harmonic_mean(test_data), 1)
    c_m = round(cubic_mean(test_data), 1)
    w_m = round(winsorized_mean(test_data), 1)
    t_m = round(trimmed_mean(test_data), 1)
    med = round(mediana(test_data), 1)
    mo = moda(test_data)

    print('Input array: ' + str(test_data) + '\n')

    print('Harmonic mean: ' + str(h_m) + '\n')
    print('Geometric mean: ' + str(g_m) + '\n')
    print('Geometric mean 2: ' + str(g_m2) + '\n')
    print('Arithmetic mean: ' + str(a_m) + '\n')
    print('Quadratic mean: ' + str(q_m) + '\n')
    print('Cubic mean: ' + str(c_m) + '\n')
    print('Winsorized mean: ' + str(w_m) + '\n')
    print('Trimmed mean: ' + str(t_m) + '\n')
    print('Mediana: ' + str(med) + '\n')
    print('Moda: ' + str(mo) + '\n')


if (__name__ == '__main__'):

    main()
