pub fn part1(input: &String) -> usize {
    let data: Vec<Vec<i8>> = input.lines().map(|x: &str|{
        x.chars().map(|y| y as i8).collect()
    }).collect();
    let mut gamma = 0;
    let mut epsilon = 0;
    let mut ans = 0;
    for i in [0..12] {
        let mut sum = 0;
        let sum = data.into_iter().map(|x| {x[i]}).
    }
    5
}
