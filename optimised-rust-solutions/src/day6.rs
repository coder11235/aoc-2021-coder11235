pub fn part1(input: &String) -> usize{
    let mut fishes = parse(input);
    for _ in 0..80 {
        perform_gen(&mut fishes)
    }
    fishes.iter().sum()
}

pub fn part2(input: &String) -> usize{
    let mut fishes = parse(input);
    for _ in 0..256 {
        perform_gen(&mut fishes)
    }
    fishes.iter().sum()
}

fn perform_gen(fishes: &mut Vec<usize>) {
    let newfishes = fishes.remove(0);
    fishes[6] += newfishes;
    fishes.push(newfishes);
}

fn parse(input: &String) -> Vec<usize> {
    let mut counts = vec![0; 9];
    for i in input.split(',') {
        let parsed = i.parse::<usize>().unwrap();
        counts[parsed] += 1;
    }
    counts
}