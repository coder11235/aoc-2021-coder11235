use std::collections::{HashMap, VecDeque, BinaryHeap};

pub fn part1(input: &String) -> usize {
    let values = HashMap::from([
        (')', 3),
        (']', 57),
        ('}', 1197),
        ('>', 25137)
    ]);
    let matches = HashMap::from([
        ('(', ')'),
        ('[',']'),
        ('{','}'),
        ('<','>'),
    ]);
    
    let mut score = 0;
    for line in input.lines() {
        let mut queue: VecDeque<char> = VecDeque::new();
        for chr in line.chars() {
            if values.contains_key(&chr) {
                // ending bracket, check queue
                let latest = queue.pop_back().unwrap();
                if matches.get(&latest).unwrap() != &chr {
                    score += values.get(&chr).unwrap();
                    break;
                }
            }
            else {
                // starting bracket, add to queue
                queue.push_back(chr);
            }
        }
    }
    score
}

pub fn part2(input: &String) -> usize {
    let values = HashMap::from([
        ('(', 1),
        ('[', 2),
        ('{', 3),
        ('<', 4)
    ]);
    let matches = HashMap::from([
        ('(', ')'),
        ('[',']'),
        ('{','}'),
        ('<','>'),
    ]);
    let mut total_scores: BinaryHeap<usize> = BinaryHeap::new();
    for line in input.lines() {
        let mut queue: VecDeque<char> = VecDeque::new();
        let mut corrupt = false;
        for chr in line.chars() {
            if !values.contains_key(&chr) {
                // ending bracket, check queue
                let latest = queue.pop_back().unwrap();
                if matches.get(&latest).unwrap() != &chr {
                    corrupt = true;
                    break;
                }
            }
            else {
                // starting bracket, add to queue
                queue.push_back(chr);
            }
        }
        if !corrupt {
            let mut line_score = 0;
            for chr in queue.iter().rev() {
                line_score = line_score*5 + values.get(chr).unwrap();
            }
            total_scores.push(line_score);
        }
    }
    let middle_index = (total_scores.len()-1)/2;
    total_scores.into_sorted_vec()[middle_index]
}