use std::collections::HashMap;

use itertools::Itertools;

pub fn part1(input: &String) -> usize {
    let mut points: HashMap<(u16, u16), u8> = HashMap::new();
    for ln in input.lines() {
        let mut splt = ln.split(" -> ");
        let (lx, ly) = splt.next().unwrap().split(',').map(|x| x.parse::<u16>().unwrap()).next_tuple().unwrap();
        let (rx, ry) = splt.next().unwrap().split(',').map(|x| x.parse::<u16>().unwrap()).next_tuple().unwrap();
        if lx == rx {
            if ly <= ry {
                for i in ly..(ry+1) {
                    ins(rx, i, &mut points);
                }
            }
            else {
                for i in ry..(ly+1) {
                    ins(rx, i, &mut points);
                }
            }
        }
        else if ly == ry {
            if lx <= rx {
                for i in lx..(rx+1) {
                    ins(i, ry, &mut points)
                }
            }
            else {
                for i in rx..(lx+1) {
                    ins(i, ry, &mut points)
                }
            }
        }
    }
    let mut count: u16 = 0;
    for value in points.values() {
        if *value >= 2 {
            count += 1;
        }
    }
    count as usize
}

fn ins(x: u16, y: u16, hash: &mut HashMap<(u16, u16), u8>) {
    let count = hash.entry((x,y)).or_insert(0);
    *count += 1;
}