#Password Data Structure. Wrapping the password and its respective strengths in a 5 tier validation sequence

class Password:
    pwd = None
    test_rating_length_check = None
    test_rating_charset = None
    test_rating_sequential_analysis = None
    test_rating_breached_match = None
    test_rating_theoritical_brute_force = None

    def __init__(self):
        self.pwd = str(" ")
        self.test_rating_length_check = 0
        self.test_rating_charset = 0
        self.test_rating_sequential_analysis = 0
        self.test_rating_theoritical_brute_force = 0
        self.test_rating_breached_match = 0
    
    def GetPasswordStrength(self):
        password_strength =  (1/50) * (self.test_rating_breached_match +
                             self.test_rating_length_check +
                             self.test_rating_charset +
                             self.test_rating_theoritical_brute_force +
                             self.test_rating_sequential_analysis) 
        return password_strength * 100 