pub fn part1(input: &String) -> isize{
    let mut prev = f64::INFINITY as i32;
    let mut count = 0;
    for line in input.lines() {
        let cur: i32 = line.parse().expect("couldnt be parsed");
        if cur > prev {
            count += 1;
        }
        prev = cur;
    }
    count
}

pub fn part2(input: &String) -> isize {
    let parsed: Vec<&str> = input.lines().collect();
    let mut count = 0;
    for linenum in 3..parsed.len() {
        if parsed[linenum] > parsed[linenum - 3] {
            count += 1;
        }
    }
    count
}
