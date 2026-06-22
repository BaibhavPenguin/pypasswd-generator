use fancy_regex::Regex;

pub struct DatabaseFields {
    pub password : String,
    pub length : u16,
    pub classification_score : f32,
    pub validation_score : f32,
    pub crack_resistance : f32,
    pub is_valid : String,
    pub password_strength : f32
}

pub struct RegexMatchPatterns {
    pub lowercase_test : Regex,
    pub uppercase_test : Regex,
    pub digit_test : Regex,
    pub symbol_test : Regex
}

impl RegexMatchPatterns {
    pub fn new() -> Self {
        Self {
            lowercase_test : Regex::new(r"[a-z]").unwrap(), 
            uppercase_test :  Regex::new(r"[A-Z]").unwrap(),
            digit_test : Regex::new(r"\d").unwrap(),  
            symbol_test: Regex::new(r"[^\d\sA-Za-z]").unwrap()

        }
    }
}


pub struct RegexValidationPatterns {
    pub pattern_pass_a : Regex,
    pub pattern_pass_b : Regex,
    pub pattern_pass_c : Regex,
    pub pattern_pass_d : Regex,
    pub pattern_pass_e : Regex
}

impl RegexValidationPatterns {
    pub fn new() -> Self {
        Self {
            pattern_pass_a : Regex::new(r"\d{3,}").unwrap(),
            pattern_pass_b : Regex::new(r#"[!@#$%^&*(),.?\":{}|<>_+\-=\[\]\\\/]{2,}"#).unwrap(), 
            pattern_pass_c : Regex::new(r"[A-Z]{3,}").unwrap(),
            pattern_pass_d : Regex::new( r"(.)\1\1").unwrap(),
            pattern_pass_e : Regex::new(r"(?:012|123|234|345|qwerty|asdfgh)").unwrap()
        }
    }
}