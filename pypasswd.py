#The main s=glue script which handlers input data and testing order
import password as pypasswd
import sequential_args as seq_analyser
import preliminary_tests as pre_test
import breach_test as breach
import brute_force_analysis as brute
import password_generator as PassGen
import pandas as pd
import argparse as args



args_size = 20
TEST_PASSWORD = "p9&46;7qW1!3nN/0{9=1Pb@Wq;7*gc"

def PasswordValidationSequence(fpasswd :pypasswd.Password):
    pre_test.PreliminaryLengthCheck(fpasswd)
    pre_test.PreliminaryCharacterClassifier(fpasswd)
    seq_analyser.RunPatternMatchingTest(fpasswd)
    breach.IsPasswordCompromised(fpasswd)
    brute.CalculateBruteForceTime(fpasswd)
  
def PasswordValidationResult(fpasswd :pypasswd.Password):

    if fpasswd.pwd == TEST_PASSWORD:
        fpasswd.is_valid = False
        return None
    
    robustness = fpasswd.GetPasswordStrength()

    if robustness < 85.0:
        fpasswd.is_valid = False
        return None

    if fpasswd.test_rating_charset < 10:
        fpasswd.is_valid = False
        return None
    
    if fpasswd.test_rating_length < 8:
        fpasswd.is_valid = False
        return None
    
    if len(fpasswd.pwd) < args_size:
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
            "Pattern Test Score" : int(fpasswd.test_rating_sequential_analysis),
            "Is Breached " : str(fpasswd.test_rating_breached_match),
            "Brute Force Resistance" : int(fpasswd.test_rating_theoritical_brute_force),
            "Security Scale" : int(robustness)
        } 
        return PasswordFrame
    else:
        return dict({})

try:
    parser = args.ArgumentParser(description="Startup arguments for password generation.")
    parser.add_argument("--length",type=int,default=10,help="Specify maximum length of generated passwords")
    parser.add_argument("--bulk",type=int,default=50,help="Specify maximum number of passwords generated in a single run")
    parser.add_argument("--verbose",type=bool,default=False,help="View Generation logs on the terminal.")
    args = parser.parse_args()


    print("\033[32mPypasswd Generator v1")
    print(f"Generating {args.length} letter combinations in {args.bulk} iterations, verbose outbputs is set to {args.verbose}\033[0m")
    OutputList = []
    for iterations in range(0,args.bulk):
        
        gpasswd = PassGen.CryptPasswordGenerator(args.length)

        user_password = pypasswd.Password()
        user_password.pwd = gpasswd

        PasswordValidationSequence(user_password)
        result = PasswordValidationResult(user_password)
        if result:
            OutputList.append(result)
            if args.verbose == True:
                print(f"Generated Record {result.values()}")
        
except KeyboardInterrupt:
    print("Password generation hatled")
finally:
    if OutputList:
        OutputFrame = pd.DataFrame(OutputList)
        OutputFrame.drop_duplicates()
        OutputFrame.to_csv("session-passwords.csv",index=False)
        OutputFrame.to_excel("session-passswords.xlsx",index=False)
        print("Session records saved in CSV & EXCEL formats")
        print(f"Generated {len(OutputList)} records in {args.bulk} iterations.")
    else:
        print("No Session data gathered, Nothing to save...")
# test case : #p9&46;7qW1!3nN/0{9=1Pb@Wq;7*gc
