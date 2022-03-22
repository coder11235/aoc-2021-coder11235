use std::{fs, u8};
use serde::{Serialize, Deserialize};

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
        &fs::read_to_string("sample_parsed_1.json").unwrap()
    ).unwrap();

    let mut logs: Vec<String> = Vec::new();

    let mut overlapping_scanners: Vec<((u8, u8),(u8, u8))> = Vec::new();

    for (indexi, si) in scanner_data.iter().enumerate() {
        println!("scanner: {}", indexi);
        logs.push(format!("base scanner: {}", indexi));
        for (indexj, sj) in scanner_data.iter().enumerate() {
            logs.push(format!("\tsecondary scanner: {}", indexj));
            if indexi == indexj {
                continue;
            }
            let comp_res = compare_scanners(&si, &sj, &mut logs);
            match comp_res {
                None => {},
                Some(res) => overlapping_scanners.push(((indexi as u8, indexj as u8), res))
            }
        }
    }

    fs::write(
        "sample_parsed_2.json",
        serde_json::to_string(&overlapping_scanners).unwrap()
    ).unwrap();

    fs::write(
        "logs.txt", logs.join("\n")).unwrap()
}

type Scanner<'a> = &'a Vec<OrientationData>;
fn compare_scanners(a: Scanner, b: Scanner, logs: &mut Vec<String>) -> Option<(u8, u8)> {
    for (index, j) in b.iter().enumerate() {
        logs.push(format!("\t\torientation: {}", index));
        if compare_beacons(&a[0].beacons, &j.beacons, logs) {
            return Option::Some(j.orientation)
        }
    }
    return Option::None
}

type BeaconData = Vec<Vec<(i16, i16, i16)>>;
fn compare_beacons(a: &BeaconData, b: &BeaconData, logs: &mut Vec<String>) -> bool {
    for (a,i) in a.iter().enumerate() {
        for (b, j) in b.iter().enumerate() {
            let v = compare_lists(i, j);
            if v >= 2 {
                logs.push(format!("\t\t\t{} -> {} = {}", a, b, &v));
            }
            if v >= 12 {
                return true
            }
        }
    }
    false
}

fn compare_lists(a: &Vec<(i16, i16, i16)>, b: &Vec<(i16, i16, i16)>) -> u8
{
    let mut count: u8 = 0;
    for i in a {
        for j in b {
            if i == j {
                count += 1;
            }
        }
    }
    return count
}