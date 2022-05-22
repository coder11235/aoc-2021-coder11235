use std::{vec, collections::BinaryHeap};

pub fn parse(input: &String) -> Vec<Vec<i8>> {
    input.lines().map(|row| {
        row.chars().map(|pos|
            pos.to_digit(10).expect(&pos.to_string()) as i8
        ).collect()
    }).collect()
}

pub fn check_if_lowest(i: i8, j: i8, map: &Vec<Vec<i8>>, adj: &[(i8, i8); 4]) -> bool {
    let pos = map[i as usize][j as usize];
    if pos == 9 {
        return false;
    }
    let adj: Vec<(i8, i8)> = adj.iter()
        .map(|(h, v)| (*h+i,*v+j))
        .filter(|(i, j)| 
            *i >= 0 && *j >= 0 && *i < 100 && *j < 100
        ).collect();
    for (h, t) in adj {
        if map[h as usize][t as usize] < pos {
            return false;
        }
    }
    true
}

pub fn part1(input: &String) -> isize{
    let mut count = 0;
    let adj: [(i8, i8); 4] = [(0,1), (1,0), (-1,0), (0, -1)];
    let parsed = parse(input);
    for i in 0..parsed.len() {
        for j in 0..parsed[0].len() {
            if check_if_lowest(i as i8, j as i8, &parsed, &adj) {
                count += (parsed[i][j] as isize)+1;
            }
        }
    }
    count
}

pub fn dfs(i: usize, j: usize, visited: &mut Vec<Vec<bool>>, map: &Vec<Vec<i8>>) -> usize {
    if map[i][j] == 9 || visited[i][j] {
        return 0
    }

    visited[i][j] = true;
    
    let mut count = 1;

    let directions: Vec<(i32, i32)> = vec![(1,0), (-1,0), (0,1), (0,-1)];

    let nearby:Vec<(usize, usize)> = directions.iter()
    .map(|(ni, nj)| (ni+i as i32, nj+j as i32))
    .filter(|(ni, nj)| 0 <= *ni && *ni < (map.len() as i32) && 0 <= *nj && *nj < (map[0].len() as i32))
    .map(|(ni, nj)| (ni as usize, nj as usize))
    .collect();

    for (ni, nj) in nearby {
        count += dfs(ni, nj, visited, map);
    }
    return count;
}

pub fn part2(input: &String) -> usize {
    let map = parse(input);
    let mut visited = vec![vec![false; map[0].len()]; map.len()];
    let mut heap = BinaryHeap::new();
    for i in 0..map.len() {
        for j in 0..map[0].len() {
            if !visited[i][j] && map[i][j] != 9 {
                heap.push(dfs(i, j, &mut visited, &map));
            }
        }
    }
    let mut top3 = 1;
    for _ in 0..3 {
        top3 *= heap.pop().unwrap();
    }
    return top3
}