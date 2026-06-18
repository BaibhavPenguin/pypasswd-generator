import hashlib
import requests
import password as passwd

#Integration of free and open source "Have I Been Pwned (HIBP) API for breach testing"

def IsPasswordCompromised(password: passwd.Password):
    

    sha1_encoder = hashlib.sha1()
    sha1_encoder.update(password.pwd.encode('utf-8'))
    full_hash = sha1_encoder.hexdigest().upper()
    
    prefix = full_hash[0:5]
    suffix = full_hash[5:]
    
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
   
    if response.status_code != 200:
        return None
        
    lines = response.text.splitlines()
    for line in lines:
        line_parts = line.split(":")
        returned_suffix = line_parts[0]
        breach_count = int(line_parts[1])
        
       
        if returned_suffix == suffix and breach_count > 0:
            password.test_rating_breached_match = True      # Is Breached
            return
            
    password.test_rating_breached_match = False         # Not Breached