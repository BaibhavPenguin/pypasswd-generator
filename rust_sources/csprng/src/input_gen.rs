use rand::{RngExt};

pub fn generate_csprng_input(length :usize) -> String {
    let mut character_diversity = Vec::new();
    character_diversity.extend(b'a'..=b'z');            // lowercase a-z
    character_diversity.extend(b'A'..=b'Z');            // uppercase A-Z
    character_diversity.extend(b'0'..=b'9');           // digits
    character_diversity.extend(b"!@#$%^&*()_+-=[]{}|;:,.<>?~/");

    let mut rng = rand::rng();
    let mut return_value = String::with_capacity(length);

    for _ in 0..length {
        let idx = rng.random_range(0..character_diversity.len());
       return_value.push(character_diversity[idx] as char);
    };

    return return_value;
}