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
mod day10;
mod day23;

use std::fs;
use std::time::{Instant, Duration};

fn main() {
    let content = fs::read_to_string("inputs/day23.txt")
         .expect("could not read file");
    let time = std::time::Instant::now();
    let ans = day23::part2(&content);
    println!("day soln: {:?} finished in: {:?}", ans, time.elapsed());
    //benchmark()
}

macro_rules! day_solving_macro {
    ($($day: ident,)*) => {{
        let mut speeds: Vec<(Duration, Duration)> = Vec::new();
        $(
            let data = fs::read_to_string(format!("inputs/{}.txt", stringify!($day))).unwrap();
            let start1 = Instant::now();
            $day::part1(&data);
            let time1 = start1.elapsed();
            let start2 = Instant::now();
            $day::part2(&data);
            let time2 = start2.elapsed();
            speeds.push((time1, time2));
        )*
        speeds
    }};
}


fn benchmark() {
    let speeds = day_solving_macro!(
        day1,
        day2,
        day3,
        day4,
        day5,
        day6,
        day7,
        day8,
        day9,
        day10,
    );

    // i dont wanna install serde just for this
    let mut final_out = String::from("[");
    for sp in speeds {
        final_out.push_str(format!("[\"{:?}\", \"{:?}\"],", sp.0, sp.1).as_str());
    }
    final_out.push_str("]");

    fs::write("benchmark.json", final_out).unwrap();
}
