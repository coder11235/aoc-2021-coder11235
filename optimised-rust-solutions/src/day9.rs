pub fn parse(input: &String) -> Vec<Vec<i8>> {
    input.lines().map(|row| {
        row.chars().map(|pos|
            pos.to_digit(10).expect(&pos.to_string()) as i8
        ).collect()
    }).collect()
}

pub fn check_if_lowest(i: i8, j: i8, map: &Vec<Vec<i8>>, adj: &[(i8, i8); 4]) -> bool {
    let pos = map[i as usize][j as usize];
    if pos == 9 {
        return false;
    }
    let adj: Vec<(i8, i8)> = adj.iter()
        .map(|(h, v)| (*h+i,*v+j))
        .filter(|(i, j)| 
            *i >= 0 && *j >= 0 && *i < 100 && *j < 100
        ).collect();
    for (h, t) in adj {
        if map[h as usize][t as usize] < pos {
            return false;
        } 
    }
    true
}

pub fn part1(input: &String) -> isize{
    let mut count = 0;
    let adj: [(i8, i8); 4] = [(0,1), (1,0), (-1,0), (0, -1)];
    let parsed = parse(input);
    for i in 0..parsed.len() {
        for j in 0..parsed[0].len() {
            if check_if_lowest(i as i8, j as i8, &parsed, &adj) {
                count += (parsed[i][j] as isize)+1;
            }
        }
    }
    count
}