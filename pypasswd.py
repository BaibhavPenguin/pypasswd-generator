#The main s=glue script which handlers input data and testing order
import password as pypasswd
import sequential_args as seq_analyser
import preliminary_tests as pre_test

def PasswordValidationSequence(fpasswd :pypasswd.Password):
    pre_test.PreliminaryLengthCheck(fpasswd)
    seq_analyser.RunPatternMatchingTest(fpasswd)



user_password = pypasswd.Password()
print("Enter a password to analyse its strength : ")
user_password.pwd = str(input("> "))

PasswordValidationSequence(user_password)

print(user_password.test_rating_length_check)
print(user_password.test_rating_sequential_analysis)