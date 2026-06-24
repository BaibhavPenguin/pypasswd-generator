use fancy_regex::Regex;

pub struct DatabaseFields {
    pub password : String,
    pub length : u16,
    pub has_lowercase : bool,
    pub has_uppercase : bool ,
    pub has_digits : bool ,
    pub has_symbols : bool,
    pub validation_score : u16,
    pub crack_resistance : u16,
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
            pattern_pass_e : Regex::new(r"(?:012|123|234|345|456|567|678|789|987|876|765|654|543|432|321|qwe|wer|ert|rty|tyu|iop|asd|sdf|dfg|fgh|ghj|hjk|jkl|zxc|xcv|cvb|vbn|bnm
            |abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|opq|pqr|rst|stu|tuv|uvw|vwx|wxy|xyz)").unwrap()
        }
    }
}