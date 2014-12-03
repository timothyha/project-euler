# https://projecteuler.net/problem=17
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

one_nine = list(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])
ten_nineteen = list(["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"])
twenty_ninety = list(["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"])

def hundred():
    result = 0
    for i in range(0,9):
        result = result + 9 * len(one_nine[i])
    for i in range(0,10):
        result = result + len(ten_nineteen[i])
    for i in range(0,8):
        result = result + 10 * len(twenty_ninety[i])
    return result

def thousand():
    result = 0
    for i in range(1,10):
        # one hundred, one hundred and one, ... and ninety-nine
        result = result + (len(one_nine[i-1]) + len("hundredand")) * 99 + hundred() + len(one_nine[i-1]) + len("hundred")
    return result

print hundred() + thousand() + len("onethousand")