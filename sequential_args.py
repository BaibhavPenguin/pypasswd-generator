#Pattern Matching, Using regex heavylifting for pattern matching and filtering repetitive and predictable combinations
import re as parser
import password as passwd

CommonPasswordPatterns = {
    "Pattern1" : r"\d{3,}",
    "Pattern2" : r"[!@#$%^&*(),.?\":{}|<>_+\-=\[\]\\\/]{2,}",                                                         
    "Pattern4" : r"[A-Z]{3,}",                                                             
    "Pattern5" : r"(.)\1\1",                                                                                      
    "Pattern6" : r"(?:012|123|234|345|qwerty|asdfgh)"                                         
}

def MatchRegexPatterns(rules :str , data :str):
    match = parser.search(rules,data)
    if match:
        return 1
    else:
        return 0

def RunPatternMatchingTest(pswd :passwd.Password):
    pswd.test_rating_sequential_analysis = 10
    for pattern in CommonPasswordPatterns.keys():
        pattern_occurence = MatchRegexPatterns(CommonPasswordPatterns[pattern],pswd.pwd)
        if pattern_occurence == 1:
            pswd.test_rating_sequential_analysis -= 2

        
   