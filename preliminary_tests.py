#Preliminary Tests like Password Length , Contains Letters , Characters and Special Symbols
import password as passwd

def PreliminaryLengthCheck(PasswordObject : passwd.Password):
    if len(PasswordObject.pwd) < 6:
        PasswordObject.test_rating_length_check = 0
        return
    
    if len(PasswordObject.pwd) >= 8 and len(PasswordObject.pwd) <= 11:
        PasswordObject.test_rating_length_check = 8
        return
    
    if len(PasswordObject.pwd) >= 12 and len(PasswordObject.pwd) <= 25:
        PasswordObject.test_rating_length_check = 9
        return
    
    if len(PasswordObject.pwd) >= 26 and len(PasswordObject.pwd) <= 127:
        PasswordObject.test_rating_length_check = 10
        return


def PreliminaryCharacterClassifier(PasswordObject : passwd.Password):
    pass
