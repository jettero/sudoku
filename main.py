#!/usr/bin/env python

# this might help:

# http://effbot.org/zone/import-confusion.htm

from sudoku.puzzle import puzzle

x = puzzle()

print repr(x)

# sudoku = puzzle([
#     [ 2,1,0, 6,0,0, 0,0,0 ],
#     [ 0,0,0, 0,0,5, 4,0,0 ],
#     [ 0,0,8, 0,0,0, 0,3,0 ],
# 
#     [ 9,0,3, 0,2,0, 0,6,0 ],
#     [ 0,0,0, 0,0,0, 0,0,0 ],
#     [ 0,7,0, 0,1,0, 5,0,4 ],
# 
#     [ 0,5,0, 0,0,0, 2,0,0 ],
#     [ 0,0,6, 8,0,0, 0,0,0 ],
#     [ 0,0,0, 0,0,4, 0,9,7 ],
# ]);
