#Password Data Structure. Wrapping the password and its respective strengths in a 5 tier validation sequence

class Password:
    pwd = None
    test_rating_length_check = None
    test_rating_charset = None
    test_rating_sequential_analysis = None
    test_rating_breached_match = None
    test_rating_theoritical_brute_force = None
    test_rating_length = None

    is_valid = None
  

    def __init__(self):
        self.pwd = str(" ")
        self.test_rating_length_check = False
        self.test_rating_length = 0
        self.test_rating_charset = 0
        self.test_rating_sequential_analysis = 0
        self.test_rating_theoritical_brute_force = 0
        self.test_rating_breached_match = False
        self.is_valid = False
     

    def GetPasswordStrength(self):
        password_strength =  (self.test_rating_length +
                             self.test_rating_charset +
                             self.test_rating_theoritical_brute_force +
                             self.test_rating_sequential_analysis) / 40
        return password_strength * 100 