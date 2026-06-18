#Preliminary Tests like Password Length , Contains Letters , Characters and Special Symbols
import password as passwd
import sequential_args as seq_analysis

CharacterClassificationArgs = {
    "UpperCaseTest" : r"[A-Z]",
    "LowerCaseTest" : r"[a-z]",
    "DigitTest" : r"\d",
    "SymbolTest" : r"[^\d\sA-Za-z]"
}

def PreliminaryLengthCheck(PasswordObject : passwd.Password):
    if len(PasswordObject.pwd) <= 7:
        PasswordObject.test_rating_length_check = False
        return
    
    if len(PasswordObject.pwd) >= 8 and len(PasswordObject.pwd) <= 127:
        PasswordObject.test_rating_length_check = True
    else:
         PasswordObject.test_rating_length_check = False
    
    match len(PasswordObject.pwd):
        case x if x in range (0,8):
            PasswordObject.test_rating_length = 0
        case x if x in range(8,12):
            PasswordObject.test_rating_length = 8
        case x if x in range (12,21):
            PasswordObject.test_rating_length = 9
        case x if x in range(21,128):
            PasswordObject.test_rating_length = 10
        case _:
            PasswordObject.test_rating_length = None



def PreliminaryCharacterClassifier(PasswordObject : passwd.Password):
    CharacterClass = []

    #Check 1 : Upper Case Characters
    #Check 2 : Lower case Characters
    #Check 3 : Digits
    #Check 4 : Special Symbols
  
    for pattern in CharacterClassificationArgs.values():
        PasswordObject.test_rating_charset = 0.0
        if seq_analysis.MatchRegexPatterns(pattern,PasswordObject.pwd):
            CharacterClass.append(True)
        else:
             CharacterClass.append(False)

    for result in CharacterClass:
        if result == True:
            PasswordObject.test_rating_charset += 2.5

    PasswordObject.test_rating_charset = int(PasswordObject.test_rating_charset)
   

