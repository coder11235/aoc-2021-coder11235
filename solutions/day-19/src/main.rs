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

type Scanners = Vec< // array of scanners
    Vec< // array of orientations
        OrientationData // each orientation
>>;
fn main() {
    let scanner_data: Scanners = serde_json::from_str(
        &fs::read_to_string("parsed_scanners.json").unwrap()
    ).unwrap();

    let mut overlapping_scanners: Vec<((u8, u8), ((u8, u8), (u8, u8)))> = Vec::new();

    for (indexi, si) in scanner_data.iter().enumerate() {
        println!("{}", indexi);
        for (indexj, sj) in scanner_data.iter().enumerate() {
            if indexi == indexj {
                continue;
            }
            let comp_res = compare_vectors(&si, &sj);
            match comp_res {
                None => {},
                Some(res) => overlapping_scanners.push(((indexi as u8, indexj as u8), res))
            }
        }
    }

    fs::write(
        "parsed2.json",
        serde_json::to_string(&overlapping_scanners).unwrap()
    ).unwrap();
}

type Scanner<'a> = &'a Vec<OrientationData>;
fn compare_vectors(a: Scanner, b: Scanner) -> Option<((u8, u8),(u8, u8))> {
    for i in a {
        for j in b {
            if compare_beacons(&i.beacons, &j.beacons) {
                return Option::Some((i.orientation, j.orientation))
            }
        }
    }
    return Option::None
}

type BeaconData = Vec<Vec<(i16, i16, i16)>>;
fn compare_beacons(a: &BeaconData, b: &BeaconData) -> bool {
    for i in a {
        for j in b {
            if compare_lists(i, j) {
                return true;
            }
        }
    }
    false
}

fn compare_lists(a: &Vec<(i16, i16, i16)>, b: &Vec<(i16, i16, i16)>) -> bool
{
    let mut count: u8 = 0;
    for i in a {
        for j in b {
            if i == j {
                count += 1;
                if count >= 12 {
                    return true
                }
            }
        }
    }
    false
}