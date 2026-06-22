use rusqlite::{Connection,Result};
use crate::data_structure::DatabaseFields;

pub fn get_database_fields(db_path: &String , local_storage: &mut Vec<DatabaseFields>) -> Result<(),rusqlite::Error> {

    let  dbs = Connection::open(db_path)?;
    let mut statement = dbs.prepare("SELECT password,length,classification_score,validation_score,crack_resistance,is_valid,password_strength  FROM data")?;

     let extracted_data = statement.query_map([], |row| {
        Ok(DatabaseFields {
            password: row.get(0)?,
            length: row.get(1)?,
            classification_score: row.get(2)?,
            validation_score : row.get(3)?,
            crack_resistance : row.get(4)?,
            is_valid : row.get(5)? ,
            password_strength : row.get(6)?
        })
    })?;

    for data in extracted_data {
        let _data = data?;
        println!("{}",_data.password);
        local_storage.push(_data);
    }

    return Ok(())
}