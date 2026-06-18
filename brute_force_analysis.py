import preliminary_tests as classifer
import password 
import re as parser

def CalculateBruteForceTime(candidate :password.Password):
    pool_diversity = 0
    if bool(parser.search(classifer.CharacterClassificationArgs["UpperCaseTest"],candidate.pwd)):
        pool_diversity+= 1
    if bool(parser.search(classifer.CharacterClassificationArgs["LowerCaseTest"],candidate.pwd)):
        pool_diversity+= 1
    if bool(parser.search(classifer.CharacterClassificationArgs["DigitTest"],candidate.pwd)):
        pool_diversity+= 1
    if bool(parser.search(classifer.CharacterClassificationArgs["SymbolTest"],candidate.pwd)):
        pool_diversity+= 1

    length = len(candidate.pwd)

    theoritical_rating = length * pool_diversity
    
    if theoritical_rating >= 64:
        candidate.test_rating_theoritical_brute_force = 10
        return
    
    if theoritical_rating >= 48:
        candidate.test_rating_theoritical_brute_force = 9
        return

    if theoritical_rating >= 32:
        candidate.test_rating_theoritical_brute_force = 8
        return
    
    if theoritical_rating >= 24:
        candidate.test_rating_theoritical_brute_force = 7
        return

   
    
        
   