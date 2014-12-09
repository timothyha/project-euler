# https://projecteuler.net/problem=24
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.
# What is the total of all the name scores in the file?

def worth(s):
    result = 0
    for a in range(0,len(s)):
        if s[a]=='"': continue
        result = result + ord(s[a]) - ord('A') + 1
    return result
    
if __name__ == '__main__':
    lines = [line.strip() for line in open('p022_names.txt')]
    names = lines[0].split(",")
    sortednames = sorted(names)
    #print sortednames[0], sortednames[-1]
    #print worth('"COLIN"'), sortednames.index('"COLIN"')
    
    result = 0
    for i in range(0,len(sortednames)):
        print sortednames[i]
        result = result + (i+1)*worth(sortednames[i])
        
    print "Result", result # Result 871198282