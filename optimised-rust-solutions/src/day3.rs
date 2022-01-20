use std::str::Lines;

pub fn part1(input: &String) -> usize{
    let mut lines= input.lines();
    let (gm, eps) = get_bits_mode(&mut lines);
    usize::from_str_radix(&gm, 2).unwrap() * usize::from_str_radix(&eps, 2).unwrap()
}

fn get_bits_mode(lines: &mut Lines) -> (String, String) {
    let mut numarr = [0; 12];
    let mut cnt = 0;
    lines.for_each(|ln| {
        ln.chars().enumerate().for_each(|(i, val)| {
            if val == '1' {
                numarr[i] += 1;
            }
        });
        cnt += 1;
    });
    let half = cnt/2;
    let mut gm = String::new();
    let mut eps = String::new();
    for i in numarr {
        gm.push(if i < half {'0'} else {'1'});
        eps.push(if i < half {'1'} else {'0'});
    };
    (gm, eps)
}

fn get_dig_max(lines: &Vec<&str>, digit: usize) -> char {
    let mut cnt = 0.0;
    for i in lines {
        if i.chars().nth(digit).unwrap() == '1' {
            cnt += 1.0;
        }
    }
    if cnt >= lines.len() as f64/2.0 {'1'} else {'0'}
}

pub fn part2(input: &String) -> usize {
    let mut lines: Vec<&str> = input.lines().collect();
    let mut oglines = lines.clone();
    let mut oxygen_rating: usize = 1;
    let mut co2_rating: usize = 1;
    for i in 0..lines[0].len() {
        let common = get_dig_max(&lines, i);
        let mut newln: Vec<&str> = Vec::new();
        for ln in &lines {
            if ln.chars().nth(i).unwrap() == common {
                newln.push(ln);
            }
        }
        lines = newln;
        if lines.len() == 2 {
            let ln = if lines[0].chars().nth(i+1).unwrap() == '1' {lines[0]} else {lines[1]};
            oxygen_rating = usize::from_str_radix(&ln, 2).unwrap();
            break;
        }
        else if lines.len() == 1 {
            oxygen_rating = usize::from_str_radix(&lines[0], 2).unwrap();
            break;
        }
    }
    for i in 0..oglines[0].len() {
        let common = get_dig_max(&oglines, i);
        let mut newln: Vec<&str> = Vec::new();
        for ln in &oglines {
            if ln.chars().nth(i).unwrap() != common {
                newln.push(ln);
            }
        }
        oglines = newln;
        if oglines.len() == 2 {
            let ln = if oglines[0].chars().nth(i+1).unwrap() == '0' {oglines[0]} else {oglines[1]};
            co2_rating = usize::from_str_radix(&ln, 2).unwrap();
            break;
        }
        else if oglines.len() == 1 {
            co2_rating = usize::from_str_radix(&oglines[0], 2).unwrap();
            break;
        }
    }
    oxygen_rating * co2_rating
}