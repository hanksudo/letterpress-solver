# -*- coding: utf-8 -*-
#
import re

dict_path = './Words/Words/en.txt'

def solve(letters, min_length=1, sort_by_length=False, contains=''):

    if (min_length < 1):
        min_length = 1

    f = open(dict_path, 'r')

    result = re.findall(r'\b[%s]{%d,}\b' % (letters, min_length), f.read())
    for c in list_unique(letters):
        result = filter(lambda x: x.count(c) <= letters.count(c), result)

    if len(contains) > 0:
        result = filter(lambda x: re.match(r'[%s]' % contains, x), result)

    if sort_by_length:
        result.sort(key=len, reverse=True)

    f.close()
    return result

def list_unique(seq):
    seen = set()
    return [ x for x in seq if x not in seen and not seen.add(x)]


if __name__ == "__main__":
    import sys
    import time

    if len(sys.argv) >= 2:
        start_time = time.time()
        words = solve(sys.argv[1])
        print words
        print 'Found %d words in %f seconds' % (len(words), time.time() - start_time)
