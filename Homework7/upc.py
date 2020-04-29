# Matthew Apuya
# 11/10/19
# CSCI-UA.00003-001

"""
upc.py
=====
Implement the following two functions as specified in the docstrings:

1. generate_bar_widths(s)
2. valid_barcode(s)

Some resources that may help with your implementation:

* https://en.wikipedia.org/wiki/Universal_Product_Code#Encoding
* http://electronics.howstuffworks.com/gadgets/high-tech-gadgets/upc3.htm
* http://www.adams1.com/upccode.html

"""


def generate_bar_widths(s):
    """Takes a barcode number as a string and translates it to a series
    of bar widths (a string that consists of 1's, 2's, 3's and 4's with
    each number corresponding to a width of a bar). For example, a
    series of bar widths starting with '1113 ... ' would consists of
    a black single width bar, a white single width bar, a black single
    width bar... and then a white triple width bar'.

    generate_bar_widths('043000181706')
    # --> '11132111132141132113211321111111222112132221131232111114111'

    HINT: try to do this by using the index and elements of a list to
    map between a number and a series of bar_widths

    :param s: the number to be translated to a series of bar widths
    :type s: str
    :return: a string representing the width of each bar, including the
    start, middle and end patterns (111, 11111, and 111)
    :rtype: str
    """
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
    """Determines whether a barcode is valid or not based on length and
    the check digit. A "UPC-A" barcode consists of 12 digits, with the
    last digit being the check digit. Some examples:

    valid_barcode('036000291452') # --> True
    valid_barcode('036000291450') # --> False
    valid_barcode('075678164125') # --> True
    valid_barcode('')            # --> False

    :param s: barcode number
    :type s: str
    :return: true if the barcode is valid, false otherwise
    :rtype: bool
    """
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
