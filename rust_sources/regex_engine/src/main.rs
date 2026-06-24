mod validation_engine;
mod data_structure;
mod database;


use std::env;
use validation_engine as validator;
use data_structure::RegexMatchPatterns;
use data_structure::RegexValidationPatterns;
use data_structure::DatabaseFields;
use database as db;



fn main() -> Result<(),rusqlite::Error> {
    let args : Vec<String> = env::args().collect();
    let db_path : String = args[1].clone();
    
    let mut local_database_records : Vec<DatabaseFields> = Vec::new();
    db::get_database_fields(&db_path , &mut local_database_records)?;
    validator::character_classification_test(&mut local_database_records);
    validator::pattern_matching_test(&mut local_database_records);
    
    for record in local_database_records {
        println!("Password : {} , Lowercase : {} , Uppercase : {} , Digits : {} , Symbols : {} , Validation Score : {}",
        record.password,
        record.has_lowercase.to_string(),
        record.has_uppercase.to_string(),
        record.has_digits.to_string(),
        record.has_symbols.to_string(),
        record.validation_score.to_string()
        );
    };

    return Ok(());
}
