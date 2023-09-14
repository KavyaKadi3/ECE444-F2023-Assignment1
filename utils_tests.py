from utils import *

test_case = utils()

# Testing the reversed function with inputs of type string, float and int
rev_test_str = test_case.reversed("1234567")
rev_test_float = test_case.reversed(12345.67)
rev_test_int = test_case.reversed(1234567)

if rev_test_str != None:
    print("Error. Test Failed.")  # expecting string input to fail
else:
    print("Success. Test Passed.")
    
if rev_test_float != None:
    print("Error. Test Failed.")  # expecting float input to fail
else:
    print("Success. Test Passed.")

if rev_test_int != 7654321:
    print("Error. Test Failed.")
else:
    print("Success. Test Passed.")  # expecting int input to pass

# Testing the formatter function with inputs of type string, float and int
form_test_str = test_case.formatter("1234567")
form_test_float = test_case.formatter(12345.67)
form_test_int = test_case.formatter(1234567)

if form_test_str != None:
    print("Error. Test Failed.")  # expecting string input to fail
else:
    print("Success. Test Passed.")
    
if form_test_float != None:
    print("Error. Test Failed.")  # expecting float input to fail
else:
    print("Success. Test Passed.")

if form_test_int[0] != '0b100101101011010000111' and form_test_int[1] != '0o4553207':
    print("Error. Test Failed.")
else:
    print("Success. Test Passed.")  # expecting int input to pass
