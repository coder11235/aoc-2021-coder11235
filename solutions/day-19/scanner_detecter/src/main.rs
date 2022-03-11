use serde_json::{Value};
use std::fs;

fn main() {
    let scanner_data: Value = serde_json::from_str(
        &fs::read_to_string("parsed_scanners.json").unwrap()
    ).unwrap();

    let overlapping_scanners:Vec<Vec<u8>> = Vec::new();

    for (indexi, scannersi) in scanner_data.as_array().iter().enumerate() {
        for (indexj, scannersj) in scanner_data.as_array().iter().enumerate() {
            if indexi == indexj {continue;}

        }
    }
}