use rusqlite::{Connection,Result};
use crate::data_structure::DatabaseFields;

pub fn get_database_fields(db_path: &String , local_storage: &mut Vec<DatabaseFields>) -> Result<(),rusqlite::Error> {

    let  dbs = Connection::open(db_path)?;
    let mut statement = dbs.prepare("SELECT password,length,has_lowercase,has_uppercase,has_digits,has_symbols,validation_score,crack_resistance,password_strength  FROM data")?;

     let extracted_data = statement.query_map([], |row| {
        Ok(DatabaseFields {
            password: row.get(0)?,
            length: row.get(1)?,
            has_lowercase : row.get(2)?,
            has_uppercase : row.get(3)?,
            has_digits : row.get(4)?,
            has_symbols : row.get(5)?,
            validation_score : row.get(6)?,
            crack_resistance : row.get(7)?,
            password_strength : row.get(8)?
        })
    })?;

    for data in extracted_data {
        let _data = data?;
        local_storage.push(_data);
    }

    return Ok(())
}