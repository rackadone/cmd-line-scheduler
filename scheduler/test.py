from input_check import *

# input_check module test cases

# TEST: is_natural_number
pass_count = 7
if not is_natural_number('00000000099'):
    print'TEST is_natural_number #1 FAIL'
    pass_count -= 1
if not is_natural_number('99999'):
    print'TEST is_natural_number #2 FAIL'
    pass_count -= 1
if is_natural_number('-21'):
    print'TEST is_natural_number #3 FAIL'
    pass_count -= 1
if is_natural_number('2a'):
    print'TEST is_natural_number #4 FAIL'
    pass_count -= 1
if is_natural_number('a3f3fd'):
    print'TEST is_natural_number #5 FAIL'
    pass_count -= 1
if is_natural_number('2a'):
    print'TEST is_natural_number #6 FAIL'
    pass_count -= 1
if is_natural_number('av'):
    print'TEST is_natural_number #7 FAIL'
    pass_count -= 1

print 'TEST >> is_natural_number passed ' + str(pass_count) + ' out of 7 tests.'