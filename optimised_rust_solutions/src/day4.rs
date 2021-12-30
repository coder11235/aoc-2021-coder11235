pub fn part1(input: &String) -> usize {
    parse(input);
    5
}

pub fn parse(input: &String) -> () {
    let mut boards = input.split("\n\n");
    let numbers: Vec<i32> = boards.next().unwrap()
    .split(',').map(|chr| chr.parse().unwrap()).collect();
    let boards: Vec<&str> = boards
    .map(|board| {
        board.lines().map(|row| {
            row.replace("  ", " ").split(" ")
        })
    })
    .collect();
    println!("{:?}\n{:?}", boards, numbers);
}

pub fn construct_checked_array(len: usize) -> Vec<Vec<Vec<bool>>> {
    let mut boardslist = Vec::new();
    for _ in 0..len {
        let mut board = Vec::new();
        for _ in 0..5 {
            board.push(vec![false; 5]);
        }
        boardslist.push(board);
    }
    return boardslist;
}

pub fn check_number(board: &Vec<Vec<i32>>, number: i32, checked_array: &mut Vec<Vec<bool>>) {
    for i in 0..5 {
        for j in 0..5 {
            if board[i][j] == number {
                checked_array[i][j] = true;
                return;
            }
        }
    }
}

pub fn check_for_horizontal_win(checked_array: Vec<Vec<bool>>) -> bool {
    for i in checked_array {
        for j in i {
            if !j {
                return false;
            }
        }
    }
    return true;
}

pub fn check_for_vertical_win(checked_array: Vec<Vec<bool>>) -> bool {
    for i in 0..5 {
        let mut won = true;
        for j in 0..5 {
            if !checked_array[j][i] {
                won = false
            }
        }
        if won {
            return true;
        }
    }
    return false;
}