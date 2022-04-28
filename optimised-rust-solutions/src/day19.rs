use std::{collections::{HashSet, HashMap}, iter::FromIterator};

use itertools::Itertools;

pub fn part1(input: &String) -> isize {
    let soln_obj = Solution::new();
    let (_sscd, cscd) = soln_obj.parse(input);
    let conn = soln_obj.find_connections(&cscd);
    let mut abs: HashMap<usize, Vec<usize>> = HashMap::new();
    abs.insert(0, vec![0]);
    Solution::find_abs_orientations(&conn, &mut abs);
    // println!("{:?}", &abs);
    5
}

type Position = (i32,i32,i32);
type SimpleScannerData = Vec<Vec<Position>>;
type ComplexScannerIndiv = Vec<Vec<HashSet<Position>>>;

struct Solution {
    transforms: Vec<fn(&Position) -> Position>,
    reverse_trans: Vec<usize>,
    simple_scanner_data: Option<SimpleScannerData>,
    complex_scanner_data: Option<Vec<ComplexScannerIndiv>>
}

impl Solution {
    fn new() -> Solution {
        Solution {
            transforms: vec![
                |a| ( a.0,  a.1,  a.2),
                |a| ( a.1,  a.2,  a.0),
                |a| ( a.2,  a.0,  a.1),
                |a| (-a.0,  a.2,  a.1),
                |a| ( a.2,  a.1, -a.0),
                |a| ( a.1, -a.0,  a.2),
                |a| ( a.0,  a.2, -a.1),
                |a| ( a.2, -a.1,  a.0),
                |a| (-a.1,  a.0,  a.2),
                |a| ( a.0, -a.2,  a.1),
                |a| (-a.2,  a.1,  a.0),
                |a| ( a.1,  a.0, -a.2),
                |a| (-a.0, -a.1,  a.2),
                |a| (-a.1,  a.2, -a.0),
                |a| ( a.2, -a.0, -a.1),
                |a| (-a.0,  a.1, -a.2),
                |a| ( a.1, -a.2, -a.0),
                |a| (-a.2, -a.0,  a.1),
                |a| ( a.0, -a.1, -a.2),
                |a| (-a.1, -a.2,  a.0),
                |a| (-a.2,  a.0, -a.1),
                |a| (-a.0, -a.2, -a.1),
                |a| (-a.2, -a.1, -a.0),
                |a| (-a.1, -a.0, -a.2),
            ],
            reverse_trans: vec![0,2,1,3,10,8,9,7,5,6,4,11,12,17,19,15,20,13,18,14,16,21,22,23],
            simple_scanner_data: Option::None,
            complex_scanner_data: Option::None
        }
    }

    fn subtract(a: Position, b: Position) -> Position {
        return (a.0-b.0, a.1-b.1, a.2-b.2)
    }
    fn add(a: Position, b: Position) -> Position {
        return (a.0+b.0, a.1+b.1, a.2+b.2)
    }

    fn parse(&self, input: &String) -> (SimpleScannerData, Vec<ComplexScannerIndiv>) {
        let mut simple_scanner_data: Vec<Vec<Position>> = Vec::new();
        let complex_scanner_data = input.split("\n\n").map(|raw_scan| {
            let proc_scan: Vec<Position> = raw_scan.lines().skip(1).map(|beacon| {
                beacon.split(",").map(|val| val.parse().unwrap()).collect_tuple().unwrap()
            }).collect();
            let complex = (0..24).map(|orientation_index| {
                let beacon_trans: Vec<Position> = proc_scan.iter().map(|bea| self.transforms[orientation_index](bea)).collect();
                beacon_trans[..beacon_trans.len()-11].iter().map(|main| {
                    HashSet::from_iter(beacon_trans.iter().map(|secondary| {
                        Solution::subtract(*secondary, *main)
                    }))
                }).collect()
            }).collect();
            let _ = &simple_scanner_data.push(proc_scan);
            complex
        }).collect();
        (simple_scanner_data, complex_scanner_data)
    }

    // type Scanner = Vec<Vec<HashSet<Position>>>;
    fn check_if_scanners_match(main: &ComplexScannerIndiv, secondary: &ComplexScannerIndiv) -> Option<usize> {
        let main_beacons = &main[0];
        for (orientation_index, secondary_beacons) in secondary.iter().enumerate() {
            for main_bea in main_beacons {
                for sec_bea in secondary_beacons {
                    if main_bea.intersection(sec_bea).count() >= 12 {
                        return  Option::Some(orientation_index);
                    }
                }
            }
        }
        Option::None
    }

    fn find_connections(&self, scanners: &Vec<ComplexScannerIndiv>) -> HashMap<(usize, usize), usize>{
        let mut relative_scanner_orientations = HashMap::new();
        for (main_index, main) in scanners.iter().enumerate() {
            // println!("{}",main_index);
            for (secondary_index, secondary) in scanners[..main_index].iter().enumerate() {
                if main_index == secondary_index {continue}
                if let Some(check_res) = Solution::check_if_scanners_match(main, secondary) {
                    relative_scanner_orientations.insert((main_index, secondary_index), check_res);
                    relative_scanner_orientations.insert((secondary_index, main_index), self.reverse_trans[check_res]);
                }
            }
        }
        relative_scanner_orientations
    }

    fn check_if_all_found(absolute_orientations: &HashMap<usize, Vec<usize>>) -> bool{
        (0..30).all(|num| absolute_orientations.contains_key(&num))
    }

    fn find_abs_orientations(connections: &HashMap<(usize, usize), usize>, absolute_orientations: &mut HashMap<usize, Vec<usize>>) {
        for ((main, sec), val) in connections.iter() {
            if (!absolute_orientations.contains_key(main)) && absolute_orientations.contains_key(sec) {
                let mut cloned = absolute_orientations.get(sec).unwrap().clone();
                cloned.push(*val);
                absolute_orientations.insert(*main, cloned);
            }
        }
        if !Solution::check_if_all_found(absolute_orientations) {
            Solution::find_abs_orientations(connections, absolute_orientations);
        }
    }

    fn find_final_rev(&self,tr_funcs: &Vec<usize>) -> usize {
        let original_tup = (0,1,2);
        let mut mutated = original_tup.clone();
        for func in tr_funcs.iter().rev() {
            mutated = self.transforms[*func](&mutated);
        }
        for (i,f) in self.transforms.iter().enumerate() {
            if f(&original_tup) == mutated {
                return i;
            }
        }
        panic!("no match found?");
    }
    fn reset_orientation(&self, abs_orientation_fns: HashMap<usize, Vec<usize>>, simple_scanner_data: SimpleScannerData) {
        simple_scanner_data.iter().enumerate().map(| (scan_num, beacon) | {
            let final_fn = self.find_final_rev(&abs_orientation_fns[&scan_num]);

        });
    }
}