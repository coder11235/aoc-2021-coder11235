use std::collections::HashMap;

use itertools::Itertools;

pub fn part1(input: &String) -> usize {
    let points: HashMap<(u16, u16), u8> = HashMap::new();
    for ln in input.lines() {
        let mut splt = ln.split(" -> ");
        let (lx, ly) = splt.next().unwrap().split(',').map(|x| x.parse::<u16>().unwrap()).next_tuple().unwrap();
        let (rx, ry) = splt.next().unwrap().split(',').map(|x| x.parse::<u16>().unwrap()).next_tuple().unwrap();
        if lx == rx {
            if ly <= ry {
                for i in ly..(ry+1) {
                    
                }
            }
        }
    }
    5
}

fn ins(a: u16, b: u16, hash: &mut HashMap<(u16, u16), u8>) {
    match hash.get(&(a, b)) {
        Ok(num) => hash.insert(k, v)
    }
}