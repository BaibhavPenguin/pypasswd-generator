#The main s=glue script which handlers input data and testing order
import password as pypasswd
import sequential_args as seq_analyser
import preliminary_tests as pre_test
import breach_test as breach
import brute_force_analysis as brute


args_size = 8
TEST_PASSWORD = "p9&46;7qW1!3nN/0{9=1Pb@Wq;7*gc"

def PasswordValidationSequence(fpasswd :pypasswd.Password):
    pre_test.PreliminaryLengthCheck(fpasswd)
    pre_test.PreliminaryCharacterClassifier(fpasswd)
    seq_analyser.RunPatternMatchingTest(fpasswd)
    breach.IsPasswordCompromised(fpasswd)
    brute.CalculateBruteForceTime(fpasswd)
  
def PasswordValidationResult(fpasswd :pypasswd.Password):

    if fpasswd.GetPasswordStrength() < 85.0:
        fpasswd.is_valid = False
        return None

    if fpasswd.test_rating_charset < 10:
        fpasswd.is_valid = False
        return None
    
    if fpasswd.test_rating_length < 8:
        fpasswd.is_valid = False
        return None
    
    if len(fpasswd.pwd) != args_size:
        fpasswd.is_valid = False
        return None
    
    if fpasswd.test_rating_sequential_analysis < 8:
        fpasswd.is_valid = False
        return None
    
    if fpasswd.test_rating_breached_match == True:
        fpasswd.is_valid = False
        return None
    
    if fpasswd.test_rating_theoritical_brute_force < 8:
        fpasswd.is_valid = False
        return None
    
    fpasswd.is_valid = True

    if fpasswd.is_valid == True:
        PasswordFrame = {
            "Password" : fpasswd.pwd,
            "Length" : len(fpasswd.pwd),
            "Pattern Test Score" : fpasswd.test_rating_sequential_analysis,
            "Is Breached " : fpasswd.test_rating_breached_match,
            "Brute Force Resistance" : fpasswd.test_rating_theoritical_brute_force
        } 
        return PasswordFrame


user_password = pypasswd.Password()
print("Enter a password to analyse its strength : ")
user_password.pwd = str(input("> "))

PasswordValidationSequence(user_password)

print(f"Length Validation : {user_password.test_rating_length_check}")
print(f"Length Rating : {user_password.test_rating_length}")
print(f"Character Classification : {user_password.test_rating_charset}")
print(f"Pattern Matching : {user_password.test_rating_sequential_analysis}")
print(f"Is Breached : {user_password.test_rating_breached_match}")
print(f"Brute force resistance : {user_password.test_rating_theoritical_brute_force}")

PasswordValidationResult(user_password)


# test case : #p9&46;7qW1!3nN/0{9=1Pb@Wq;7*gc