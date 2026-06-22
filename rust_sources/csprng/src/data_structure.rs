pub struct PasswordCandidate {
    pub string : String,
    pub length : u16,
    pub classification_score : u16,
    pub validation_score : u16,
    pub brute_force_resistance : u16,
    pub is_valid : bool,
    pub is_breached : bool,
    pub password_strength : u16,
    pub prefix : String,
    pub suffix : String
}

impl PasswordCandidate {

    pub fn new(string_args : String , length_args : u16) -> Self {
        Self{
            string : string_args,
            length : length_args,
            classification_score : 0,
            validation_score : 0,
            brute_force_resistance : 0,
            is_valid : false,
            is_breached : false,
            password_strength : 0,
            prefix : " ".to_string(),
            suffix : " ".to_string()
        }
    }
}