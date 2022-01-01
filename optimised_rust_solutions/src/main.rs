mod day1;
mod utils;
mod day2;
mod day3;
mod day4;

use std::fs;

fn main() {
    let content = fs::read_to_string("inputs/day4.txt")
        .expect("could not read file");
    let time = std::time::Instant::now();
    let ans = day4::part2(&content);
    println!("day 4 soln: {} finished in: {:?}", ans, time.elapsed());
}
