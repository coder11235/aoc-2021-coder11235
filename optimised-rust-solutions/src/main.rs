mod day1;
mod utils;
mod day2;
mod day3;
mod day4;
mod day5;
mod day6;

use std::fs;

fn main() {
    let content = fs::read_to_string("inputs/day21.txt")
        .expect("could not read file");
    let time = std::time::Instant::now();
    let ans = day2::part2(&content);
    println!("day 6 soln: {} finished in: {:?}", ans, time.elapsed());
}
