pub fn part1(input: &String) -> usize {
    let (numbers, boards) = parse(input);
    let mut checking_array = construct_checked_array(boards.len());
    for number in numbers {
        for bnum in 0..boards.len() {
            check_number(&boards[bnum], number, &mut checking_array[bnum]);
            if check_for_horizontal_win(&checking_array[bnum]) || check_for_vertical_win(&checking_array[bnum]) {
                return find_sum(&boards[bnum], &checking_array[bnum], number);
            }
        }
    }
    return 5;
}

pub fn part2(input: &String) -> usize {
    let (numbers, boards) = parse(input);
    let mut board_won_array = vec![false; boards.len()];
    let mut checking_array = construct_checked_array(boards.len());
    for number in numbers {
        for bnum in 0..boards.len() {
            check_number(&boards[bnum], number, &mut checking_array[bnum]);
            if check_for_horizontal_win(&checking_array[bnum]) || check_for_vertical_win(&checking_array[bnum]) {
                board_won_array[bnum] = true;
                let mut has_everyone_else_won = true;
                for i in &board_won_array {
                    if *i == false {
                        has_everyone_else_won = false;
                        break;
                    }
                }
                if has_everyone_else_won {
                    return find_sum(&boards[bnum], &checking_array[bnum], number);
                }
            }
        }
    }
    return 5;
}

fn parse(input: &String) -> (Vec<u8>, Vec<Vec<Vec<u8>>>) {
    let mut boards = input.split("\n\n");
    let numbers: Vec<u8> = boards.next().unwrap()
    .split(',').map(|chr| chr.parse::<u8>().unwrap()).collect();
    let boards = boards.map(|board| {
        board.lines().map(|row| {
            row.split(" ").filter(|x | *x != "").map(|x| x.parse::<u8>().unwrap()).collect::<Vec<u8>>()
        }).collect::<Vec<Vec<u8>>>()
    }).collect::<Vec<Vec<Vec<u8>>>>();
    return (numbers, boards)
}

fn construct_checked_array(len: usize) -> Vec<Vec<Vec<bool>>> {
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

fn check_number(board: &Vec<Vec<u8>>, number: u8, checked_array: &mut Vec<Vec<bool>>) {
    for i in 0..5 {
        for j in 0..5 {
            if board[i][j] == number {
                checked_array[i][j] = true;
                return;
            }
        }
    }
}

fn check_for_horizontal_win(checked_array: &Vec<Vec<bool>>) -> bool {
    for i in checked_array {
        for j in i {
            if !j {
                return false;
            }
        }
    }
    return true;
}

fn check_for_vertical_win(checked_array: &Vec<Vec<bool>>) -> bool {
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

fn find_sum(board: &Vec<Vec<u8>>, checking_array: &Vec<Vec<bool>>, number: u8) -> usize {
    let mut sum = 0;
    for i in 0..5 {
        for j in 0..5 {
            if checking_array[i][j] == false {
                sum += board[i][j] as usize;
            }
        }
    }
    return sum * number as usize;
}