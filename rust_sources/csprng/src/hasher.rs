use sha1::{Digest,Sha1};
use hex;
use crate::data_structure::PasswordCandidate;

pub fn get_sha1_hashed_records(password :&mut PasswordCandidate)-> std::io::Result<()> {
    let _hasher = Sha1::digest(password.string.as_bytes());
    let hashed_password = hex::encode_upper(_hasher);
    password.prefix = hashed_password[0..5].to_string();
    password.suffix = hashed_password[5..].to_string();
    
    Ok(())
}