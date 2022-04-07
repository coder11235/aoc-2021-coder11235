#![allow(dead_code)]

mod day1;
mod utils;
mod day2;
mod day3;
mod day4;
mod day5;
mod day6;
mod day7;
mod day8;
mod day9;

use std::fs;

fn main() {
    let content = fs::read_to_string("inputs/day9.txt")
        .expect("could not read file");
    let time = std::time::Instant::now();
    let ans = day9::part1(&content);
    println!("day soln: {} finished in: {:?}", ans, time.elapsed());
}
