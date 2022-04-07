use itertools::Itertools;
use std::{collections::HashSet, iter::FromIterator};

pub fn part1(input: &String) -> isize{
    let mut total = 0;
    for line in input.lines() {
        for num in line.split(" | ").nth(1).unwrap()
        .split_whitespace() {
            let le = num.len();
            if le == 2 || le == 3 || le == 4 || le == 7 {
                total += 1;
            } 
        }
    }
    total
}

type Digit = HashSet<char>;

fn parse(input: &String) -> Vec<(Vec<Digit>,Vec<Digit>)> {
    input.lines().map(|line| {
        line.split(" | ").map(|coll| {
            coll.split_whitespace()
                .map(|num| {
                    HashSet::from_iter(num.chars())
                })
                .collect()
        }).collect_tuple().unwrap()
    }).collect()
}

fn check_if_fits_inside(small: &Digit, large: &Digit) -> bool {
    small.difference(large).next().is_none()
}

fn with_small_find_big(small: &Digit, remaining: &mut Vec<Digit>) -> Digit {
    for dig_num in 0..remaining.len() {
        if check_if_fits_inside(small, &remaining[dig_num]) {
            return remaining.remove(dig_num);
        }
    }
    panic!("messed up")
}

fn with_big_find_small(big: &Digit, remaining: &mut Vec<Digit>) -> Digit {
    for dig_num in 0..remaining.len() {
        if check_if_fits_inside(&remaining[dig_num], big) {
            return remaining.remove(dig_num);
        }
    }
    panic!("messed up")
}

fn find_values(coll: Vec<Digit>) -> Vec<Option<HashSet<char>>> {
    let mut order_arr: Vec<Option<Digit>> = vec![Option::None; 10];
    let mut remaining: Vec<Digit> = Vec::new();

    for dig in coll {
        match dig.len() {
            2 => order_arr[1] = Some(dig),
            3 => order_arr[7] = Some(dig),
            4 => order_arr[4] = Some(dig),
            7 => order_arr[8] = Some(dig),
            _ => remaining.push(dig)
        }
    }

    order_arr[9] = Some(with_small_find_big(order_arr[4].as_ref().unwrap(), &mut remaining));
    order_arr[6] = Some(with_small_find_big(
        &HashSet::from_iter(order_arr[8].as_ref().unwrap().difference(order_arr[7].as_ref().unwrap()).map(|x| *x)),
        &mut remaining));
    order_arr[5] = Some(with_big_find_small(order_arr[6].as_ref().unwrap(), &mut remaining));
    order_arr[3] = Some(with_big_find_small(order_arr[9].as_ref().unwrap(), &mut remaining));
    order_arr[0] = Some(with_small_find_big(order_arr[1].as_ref().unwrap(), &mut remaining));
    order_arr[2] = Some(remaining[0].clone());
    order_arr
}

pub fn part2(input: &String) -> usize {
    let mut sum = 0;
    let input = parse(input);
    for (inp, out) in input {
        let order = find_values(inp);
        let mut num = 0;
        for dig in out {
            for j in 0..order.len() {
                if dig.is_subset(order[j].as_ref().unwrap()) && dig.is_superset(order[j].as_ref().unwrap()) {
                    num = num*10 + j;
                }
            }
        }
        sum += num;
    }
    sum
}