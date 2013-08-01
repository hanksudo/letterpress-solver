#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import solver


def demo1():
    letters = 'elsphpnurufswwfbjcrvvewwm'
    start_time = time.time()
    words = solver.solve(letters, min_length=1, sort_by_length=True)

    print words
    print 'Found %d words in %f seconds' % (len(words), time.time() - start_time)

def demo2():
    letters = 'sfysmzgkrivsdwhaqgpecxakk'
    start_time = time.time()
    words = solver.solve(letters, min_length=1, sort_by_length=True, contains='e')

    print words
    print 'Found %d words in %f seconds' % (len(words), time.time() - start_time)

if __name__ == "__main__":
    demo1()
    demo2()