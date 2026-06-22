use crate::data_structure::RegexMatchPatterns;
use crate::data_structure::RegexValidationPatterns;
use crate::data_structure::DatabaseFields;
use fancy_regex::Regex;

fn match_regex_pattern(rules : &Regex , data : &String) -> bool {
    return rules.is_match(&data).unwrap_or(false)
}

//pub fn character_classification_test() -> () { }

//pub fn pattern_matching_test() -> () { }