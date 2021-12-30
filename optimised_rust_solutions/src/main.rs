mod day1;
mod utils;
mod day2;
mod day3;

use std::fs;

fn main() {
    let content = fs::read_to_string("inputs/day3.txt")
        .expect("could not read file");
    let time = std::time::Instant::now();
    let ans = day3::part2(&content);
    println!("day 3 soln: {} finished in: {:?}", ans, time.elapsed());
}
