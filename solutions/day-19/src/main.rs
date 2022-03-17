use std::{fs, u8, fs::OpenOptions};
use serde::{Serialize, Deserialize};
use std::io::prelude::*;

static mut LOGS: Vec<String> = Vec::new();

#[derive(Serialize, Deserialize, Debug)]
struct OrientationData {
    pub orientation: (u8, u8), // the orientation index
    pub beacons: Vec< //primary beacon
        Vec< // relative beacon
            (i16, i16, i16)
    >>
}

type Scanners = Vec<Vec<OrientationData>>;
fn main() {
    let scanner_data: Scanners = serde_json::from_str(
        &fs::read_to_string("parsed_scanners.json").unwrap()
    ).unwrap();

    let mut overlapping_scanners: Vec<((u8, u8),(u8, u8))> = Vec::new();

    for (indexi, si) in scanner_data.iter().enumerate() {
        unsafe{
            LOGS.push(format!("main scanner: {}", indexi));
        }
        for (indexj, sj) in scanner_data.iter().enumerate() {
            unsafe {
                LOGS.push(format!("\ttarget scanner: {}", indexj));
            }
            if indexi == indexj {
                continue;
            }
            let comp_res = compare_scanners(&si, &sj);
            match comp_res {
                None => {},
                Some(res) => overlapping_scanners.push(((indexi as u8, indexj as u8), res))
            }
            unsafe {
                if LOGS.last().unwrap().contains("ori") {
                    LOGS.pop();
                }
            }
        }
        unsafe {
            fs::write("logs.txt", "").unwrap();
            let mut file = OpenOptions::new()
                .write(true)
                .append(true)
                .open("logs.txt")
                .unwrap();
            for i in &LOGS {
                if let Err(e) = writeln!(file, "{}", &i) {
                    eprintln!("Couldn't write to file: {}", e);
                }
            }
        }
    }

    fs::write(
        "parsed2.json",
        serde_json::to_string(&overlapping_scanners).unwrap()
    ).unwrap();
}

type Scanner<'a> = &'a Vec<OrientationData>;
fn compare_scanners(a: Scanner, b: Scanner) -> Option<(u8, u8)> {
    for (i, j) in b.iter().enumerate() {
        unsafe {
            if LOGS.last().unwrap().contains("or") {
                LOGS.pop();
            }
            LOGS.push(format!("\t\torientation: {}", i));
        }
        if compare_beacons(&a[0].beacons, &j.beacons) {
            return Option::Some(j.orientation)
        }
    }
    return Option::None
}

type BeaconData = Vec<Vec<(i16, i16, i16)>>;
fn compare_beacons(a: &BeaconData, b: &BeaconData) -> bool {
    for (indexi, i) in a.iter().enumerate() {
        for (indexj, j) in b.iter().enumerate() {
            if compare_lists(i, j, indexi, indexj) {
                return true;
            }
        }
    }
    false
}

fn compare_lists(a: &Vec<(i16, i16, i16)>, b: &Vec<(i16, i16, i16)>, indexi: usize, indexj: usize) -> bool
{
    let mut count: u8 = 0;
    for i in a {
        for j in b {
            if i == j {
                count += 1;
            }
        }
    }
    if count > 1 {
        unsafe {
            LOGS.push(format!("\t\t\t{} -> {} = {}", indexi, indexj, count));
        }
    }
    if count >= 12 {
        return true
    }
    false
}