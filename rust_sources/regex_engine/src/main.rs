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


    return Ok(());
}
