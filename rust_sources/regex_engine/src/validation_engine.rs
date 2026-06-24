use crate::data_structure::RegexMatchPatterns;
use crate::data_structure::RegexValidationPatterns;
use crate::data_structure::DatabaseFields;
use fancy_regex::Regex;

fn match_regex_pattern(rules : &Regex , data : &String) -> bool {
    return rules.is_match(&data).unwrap_or(false)
}

pub fn character_classification_test(database_records : &mut Vec<DatabaseFields>) -> () { 
    
    let test_cases : RegexMatchPatterns = RegexMatchPatterns::new();

    for record in database_records {

        if  match_regex_pattern(&test_cases.uppercase_test , &record.password)== true {
            record.has_uppercase = true;
        }
        else{
            record.has_uppercase = false;
        };

        if match_regex_pattern(&test_cases.lowercase_test, &record.password) == true{
            record.has_lowercase = true;
        }
        else{
            record.has_lowercase = false;
        };

        if match_regex_pattern(&test_cases.digit_test, &record.password) == true {
            record.has_digits = true;
        }
        else {
            record.has_digits = false;
        };

        if match_regex_pattern(&test_cases.symbol_test, &record.password) == true {
            record.has_symbols = true;
        }
        else {
            record.has_symbols = false;
        }

    }

    return ();
}

pub fn pattern_matching_test(database_records : &mut Vec<DatabaseFields>) -> () {

    let test_cases : RegexValidationPatterns = RegexValidationPatterns::new();
    
    for record in database_records {
        record.validation_score = 0;
        if match_regex_pattern(&test_cases.pattern_pass_a , &record.password) == false {
           record.validation_score += 2;
        };
        if match_regex_pattern(&test_cases.pattern_pass_b , &record.password) == false {
           record.validation_score += 2;
        };
        if match_regex_pattern(&test_cases.pattern_pass_c , &record.password) == false {
            record.validation_score += 2;
        };
        if match_regex_pattern(&test_cases.pattern_pass_d , &record.password) == false {
            record.validation_score += 2;
        };
        if match_regex_pattern(&test_cases.pattern_pass_e , &record.password) == false {
           record.validation_score += 2;
        };

        if record.validation_score <= 6 {
            match record.length {
            0..8 => record.validation_score += 0,
            8..12 => record.validation_score += 1,
            12..26 => record.validation_score += 2,
            26..31 => record.validation_score += 3,
            31..128 => record.validation_score += 4,
            _ => record.validation_score += 4
            };
        };
       

    }
    return ();

 }
