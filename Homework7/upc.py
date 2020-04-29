"""
Takes a barcode number as a string and translates it to a series
    of bar widths (a string that consists of 1's, 2's, 3's and 4's with
    each number corresponding to a width of a bar).
"""


def generate_bar_widths(s):
    bar_width = "111"
    counter = 0

    for i in s:
        if i == '0':
            bar_width += '3211'
        elif i == '1':
            bar_width += '2221'
        elif i == '2':
            bar_width += '2122'
        elif i == '3':
            bar_width += '1411'
        elif i == '4':
            bar_width += '1132'
        elif i == '5':
            bar_width += '1231'
        elif i == '6':
            bar_width += '1114'
        elif i == '7':
            bar_width += '1312'
        elif i == '8':
            bar_width += '1213'
        elif i == '9':
            bar_width += '3112'

        counter += 1

        if counter == 6:
            bar_width += '11111'

    bar_width += '111'

    return bar_width


def valid_barcode(s):
    is_valid = False
    has_check = False
    odd_barcode_list = s[0::2]
    odd_barcode_sum = 0
    even_barcode_list = s[1:10:2]
    even_barcode_sum = 0

    if not s.isnumeric():
        return is_valid

    for i in odd_barcode_list:
        odd_barcode_sum += int(i)

    for i in even_barcode_list:
        even_barcode_sum += int(i)

    new_barcode = odd_barcode_sum * 3
    new_barcode += even_barcode_sum
    check_modulo = new_barcode % 10

    if check_modulo == 0:
        check_digit = 0

    else:
        check_digit = 10 - check_modulo

    if check_digit == int(s[11]):
        has_check = True

    if len(s) == 12 and has_check is True:
        is_valid = True

    return is_valid


if __name__ == '__main__':
    print(generate_bar_widths('043000181706'))

    print(valid_barcode('036000291452')) # --> True
    print(valid_barcode('036000291450'))  # --> False
    print(valid_barcode('075678164125'))  # --> True
    print(valid_barcode(''))  # --> False
