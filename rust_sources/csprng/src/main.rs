mod data_structure;
mod input_gen;
mod hasher;

use std::env;
use rusqlite::{Connection,Result};
use data_structure::PasswordCandidate;
use input_gen as csprng;

fn main() -> Result<()> {
    let args : Vec<String> = env::args().collect();

    let length = match args[1].parse::<u16>() {
        Ok(num) => num,
        Err(_num) => 0
    };

    let bulk = match args[2].parse::<u128>() {
        Ok(num) => num,
        Err(_num) => 0
    };

    let path :&String = &args[3];

    let mut database = Connection::open(path)?;

    database.pragma_update(None, "busy_timeout", "5000")?;
    database.pragma_update(None, "journal_mode", "WAL")?;
    database.pragma_update(None, "synchronous" , "NORMAL")?;

    database.execute(
        "CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            password TEXT NOT NULL,
            length INTEGER NOT NULL,
            has_lowercase BOOLEAN,
            has_uppercase BOOOLEAN,
            has_digits BOOLEAN,
            has_symbols BOOLEAN,
            validation_score REAL,
            crack_resistance REAL,
            is_breached BOOLEAN,
            password_strength REAL,
            prefix TEXT NOT NULL,
            suffix TEXT NOT NULL
        );",
        (), // Empty tuple for no parameters
    )?;

    let transaction = database.transaction()?;
    
    let mut statement = transaction.prepare("INSERT INTO data (password,length,has_lowercase,has_uppercase,has_digits,has_symbols,validation_score,crack_resistance,is_breached,password_strength,prefix,suffix) VALUES (?1,?2,?3,?4,?5,?6,?7,?8,?9,?10,?11,?12)")?;
    for _ in 0..bulk {
        let passwd : String = csprng::generate_csprng_input(length as usize);
        let mut password : PasswordCandidate = PasswordCandidate::new(passwd,length);
        hasher::get_sha1_hashed_records(&mut password).expect("NoneType");
        statement.execute((password.string.clone(),
        password.string.chars().count() as u16,
        password.has_lowercase,
        password.has_uppercase,
        password.has_digits,
        password.has_symbols,
        password.validation_score,
        password.brute_force_resistance,
        password.is_breached,
        password.password_strength,
        password.prefix,
        password.suffix
        ))?;
    }
    drop(statement);            //transaction is borrowed by statement hence it needs to be dropped before using transaction again - Self note dont do ts 
    transaction.commit()?;
    



    Ok(())
}
