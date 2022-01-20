pub fn part1(input: &String) -> u32 {
    let mut hor = 0;
    let mut depth = 0;
    for line in input.lines() {
        let mut iter = line.chars();
        let cmd = iter.next().unwrap();
        let mag = iter.last().unwrap().to_digit(10).unwrap();
        if cmd == 'f' {
            hor += mag;
        }
        else if cmd == 'd' {
            depth += mag;
        }
        else {
            depth -= mag;
        }
    }
    depth * hor 
}

pub fn part2(input: &String) -> u32 {
    let mut hor = 0;
    let mut depth = 0;
    let mut aim = 0;
    for line in input.lines() {
        let mut iter = line.chars();
        let cmd = iter.next().unwrap();
        let mag = iter.last().unwrap().to_digit(10).unwrap();
        if cmd == 'f' {
            hor += mag;
            depth += aim * mag;
        }
        else if cmd == 'd' {
            aim += mag;
        }
        else {
            aim -= mag;
        }
    }
    depth * hor
}
