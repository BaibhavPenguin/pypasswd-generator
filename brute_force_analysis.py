import preliminary_tests as classifer
import password 
import re as parser


TIER_8_LIMIT  = 59873693923837890625 #95 ** 10
TIER_9_LIMIT  = 540360087662636718750 #95 ** 12
TIER_10_LIMIT = 46329123015911865234375 #95 ** 15 

def CalculateBruteForceTime(candidate :password.Password):
    pool_size = 0
    if bool(parser.search(classifer.CharacterClassificationArgs["UpperCaseTest"],candidate.pwd)):
        pool_size+= 26
    if bool(parser.search(classifer.CharacterClassificationArgs["LowerCaseTest"],candidate.pwd)):
        pool_size+= 26
    if bool(parser.search(classifer.CharacterClassificationArgs["DigitTest"],candidate.pwd)):
        pool_size+= 10
    if bool(parser.search(classifer.CharacterClassificationArgs["SymbolTest"],candidate.pwd)):
        pool_size+= 33

    total_combinations = pool_size ** len(candidate.pwd)
    candidate.test_rating_theoritical_brute_force

    match total_combinations:
        
        case _ if total_combinations >= TIER_10_LIMIT:
            candidate.test_rating_theoritical_brute_force = 10
        
        case _ if total_combinations >= TIER_9_LIMIT:
           candidate.test_rating_theoritical_brute_force = 9

        case _ if total_combinations >= TIER_9_LIMIT:
           candidate.test_rating_theoritical_brute_force = 9
            
        case _ if total_combinations >= TIER_8_LIMIT:
          candidate.test_rating_theoritical_brute_force = 8
        
        case _:
           candidate.test_rating_theoritical_brute_force = 7