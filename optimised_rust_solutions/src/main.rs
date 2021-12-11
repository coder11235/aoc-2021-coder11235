mod day1;
mod utils;
mod day2;

use std::fs;

fn main() {
    let content = fs::read_to_string("inputs/day2.txt")
        .expect("could not read file");
    let time = std::time::Instant::now();
    let ans = day2::part2(&content);
    println!("day 2 soln: {} finished in: {:?}", ans, time.elapsed());
}
