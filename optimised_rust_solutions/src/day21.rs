use itertools::Itertools;

pub fn part2(input: &String) -> usize {
    let (p1, p2) = input.lines().map(|ln| {
        ln.split(": ").nth(1).unwrap().parse::<u8>().unwrap()
    }).next_tuple().unwrap();
    let mut c1: u64 = 0;
    let mut c2: u64 = 0;
    for i in 1..4 {
        for j in 1..4 {
            for k in 1..4 {
                play1(p1, p2, 0, 0, i+j+k, &mut c1, &mut c2);
            }
        }
    }
    5
}

fn play1(p1: u8, p2: u8, scp1: u8, scp2: u8, mv: u8, c1: &mut u64, c2: &mut u64) {
    let mut p1 = p1;
    p1 += mv;
    if p1 > 10 {
        p1 -= 10;
    }
    let mut scp1 = scp1;
    scp1 += p1;
    if scp1 >= 3 {
        *c1 += 1;
        println!("{},{}", &c1, &c2);
    }
    else {
        for i in 1..4 {
            for j in 1..4 {
                for k in 1..4 {
                    play2(p1, p2, scp1, scp2, i+j+k, c1, c2);
                }
            }
        }
    }
}

fn play2(p1: u8, p2: u8, scp1: u8, scp2: u8, mv: u8, c1: &mut u64, c2: &mut u64) {
    let mut p2 = p2;
    p2 += mv;
    if p2 > 10 {
        p2 -= 10;
    }
    let mut scp2 = scp2;
    scp2 += p2;
    if scp2 >= 3 {
        *c2 += 1;
        println!("{},{}", &c1, &c2);
    }
    else {
        for i in 1..4 {
            for j in 1..4 {
                for k in 1..4 {
                    play1(p1, p2, scp1, scp2, i+j+k, c1, c2);
                }
            }
        }
    }
}