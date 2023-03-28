use std::collections::HashMap;

// enum for each position
#[derive(PartialEq, Debug, Clone, Copy, Eq, Hash)]
enum Amhipod {
    A,
    B,
    C,
    D,
    Dot
}

// order of amhipods
static ORDER: [Amhipod; 4] = [Amhipod::A,Amhipod::B,Amhipod::C,Amhipod::D];

type Hallway = Vec<Amhipod>;
type Rows = Vec<Vec<Amhipod>>;

// checks if you can move into ths spot in the hallway
fn check_hall_spot(x: usize) -> bool {
    if x == 0 || x == 10 {
        return true
    }
    return x%2==1
}

// convert row and opposite hallway positions
fn rows_to_hallway(x: usize) -> usize {(x+1)*2}
fn hallway_to_rows(x: usize) -> usize {(x/2)+1}

// finds the row column of the amhipods home
fn find_amhipod_home(amp: Amhipod) -> usize {
    ORDER.iter().position(|&x| x == amp).unwrap()
}
// find the amhipod whose home is the given row
fn find_home_amp_in_row(row: usize) -> Amhipod { ORDER[row] }
// find the move cost of the amhipod
fn find_amp_cost(amp: Amhipod) -> usize {
    (10 as usize).pow(find_amhipod_home(amp) as u32)
}
fn char_to_amp(chr: char) -> Amhipod {
    if chr == 'A'{
        return Amhipod::A
    }
    else if chr == 'B' {
        return Amhipod::B
    }
    else if chr == 'C' {
        return Amhipod::C
    }
    else if chr == 'D' {
        return Amhipod::D
    }
    else {
        panic!("no such amphipod");
    }
}

// each state of the thingi
#[derive(Debug, Hash, PartialEq, Eq, Clone)]
struct StateParts {
    pub rows: Rows,
    pub hallway: Hallway
}
impl StateParts {
    pub fn new(rows: Rows, hallway: Hallway) -> Self {
        StateParts {
            rows,
            hallway
        }
    }
}

// states hashmap used for memoization
struct States {
    states: HashMap<StateParts, Option<i32>>
}
impl States {
    fn get_state(&self, state: &StateParts) -> Option<i32> {
        *self.states.get(state).unwrap()
    }
    fn check_state(&self, state: &StateParts) -> bool {
        self.states.contains_key(state)
    }
    fn mark_state(&mut self, state: &StateParts) {
        self.states.insert(state.clone(), None);
    }
    fn update_state(&mut self, state: &StateParts, min_cost: i32) {
        self.states.insert(state.clone(), Some(min_cost));
    }
    pub fn new() -> Self {
        States { states: HashMap::new() }
    }
}

pub fn part2(input: &String) -> i32 {
    let (init_rows, init_hallway) = parse(&input);
    let init_state = StateParts::new(init_rows, init_hallway);
    println!("{:?}", init_state);
    move_amp(&mut States::new(), init_state, 0)
}

// return the position the amhipod must move into in the home row or None if it shouldnt
fn home_occupance(amp: Amhipod, rows: &Rows) -> Option<usize> {
    let amp_home = find_amhipod_home(amp);
    for (index, row) in rows.iter().enumerate().rev() {
        if row[amp_home] == amp {
            continue;
        }
        else if row[amp_home] == Amhipod::Dot {
            return Some(index)
        }
        else {
            return None
        }
    }
    panic!()
}

fn check_path(opp_hallway_pos: usize, h_num: usize, hallway_ref: &Hallway) -> bool {
    if opp_hallway_pos > h_num {
        for i in h_num+1..opp_hallway_pos {
            if hallway_ref[i] != Amhipod::Dot {
                return false;
            }
        }
        return true
    }
    else {
        for i in (h_num+1..opp_hallway_pos).rev() {
            if hallway_ref[i] != Amhipod::Dot {
                return false;
            }
        }
        return true
    }
}

// checks if amhipods in this column should be moved out
fn col_check(rows: &Rows, col_num: usize) -> Option<i32> {
    let mut topmost_amp_index: i32 = -1;
    // first find topmost amp
    for (i, amp_row) in rows.iter().enumerate() {
        if amp_row[col_num] == Amhipod::Dot {
            continue;
        } 
        else {
            topmost_amp_index = i as i32;
            break;
        }
    }
    if topmost_amp_index < 0 {
        return None;
    }
    // then find if its in incorrect order
    let home_amp = find_home_amp_in_row(col_num);
    for amp_row in rows.iter().rev() {
        if amp_row[col_num] == home_amp {
            continue;
        }
        else if amp_row[col_num] == Amhipod::Dot {
            break;
        }
        else {
            return Some(topmost_amp_index);
        }
    }
    None
}

fn move_amp(states_mem: &mut States, state: StateParts, cost_so_far: i32) -> i32 {
    // impl memoization
    if states_mem.check_state(&state) {
        match states_mem.get_state(&state) {
            None => return f64::INFINITY as i32,
            Some(val) => return val
        }
    }
    else {
        states_mem.mark_state(&state)
    }

    let mut least_costs: Vec<i32> = Vec::new();
    
    // move the amhipods out of the hallway
    let hallway_ref = &state.hallway;
    let rows_ref = &state.rows;
    for (h_num, amp) in hallway_ref.iter().enumerate() {
        if *amp == Amhipod::Dot {
            continue;
        }
        if let Some(amp_home_row) = home_occupance(*amp, rows_ref) {
            let amp_home_col = find_amhipod_home(*amp);
            let opp_hallway_pos = rows_to_hallway(amp_home_col);
            if !check_path(opp_hallway_pos, h_num, hallway_ref) {
                continue;
            }
            let cost = (opp_hallway_pos.abs_diff(h_num)+amp_home_row+1)*find_amp_cost(*amp);
            let mut cloned_state = state.clone();
            cloned_state.rows[amp_home_row][amp_home_col] = *amp;
            cloned_state.hallway[h_num] = Amhipod::Dot;
            least_costs.push(move_amp(states_mem, cloned_state, cost_so_far + cost as i32))
        }
    }

    // move the amhipods out of the rows
    for col_num in 0..4 {
        let topmost_amp = col_check(rows_ref, col_num);
        if topmost_amp == None {
            continue;
        }
        let amp_row_num = topmost_amp.unwrap();
        let opp_hallway_pos = rows_to_hallway(col_num);
        least_costs.append(&mut move_into_hall(cost_so_far, opp_hallway_pos+1..11, amp_row_num as usize, col_num, &state, states_mem));
        least_costs.append(&mut move_into_hall(cost_so_far, (0..opp_hallway_pos).rev(), amp_row_num as usize, col_num, &state, states_mem));
    }

    let minimum_cost = *least_costs.iter().min().unwrap_or(&(f64::INFINITY as i32));

    states_mem.update_state(&state, minimum_cost);
    return minimum_cost
}

fn move_into_hall(cost_so_far: i32, rng: impl Iterator<Item = usize>, amp_row_num: usize, amp_col_num: usize, state: &StateParts, states_mem: &mut States) -> Vec<i32>{
    let mut least_costs = Vec::new();
    let start_pos = rows_to_hallway(amp_col_num);
    for pos in rng {
        if !check_hall_spot(pos) {
            continue;
        }
        let row_amp = state.rows[amp_row_num][amp_col_num];
        if state.hallway[pos] != Amhipod::Dot {
            return least_costs;
        }
        let mut cloned_state = state.clone();
        cloned_state.hallway[pos] = row_amp;
        cloned_state.rows[amp_row_num][amp_col_num] = Amhipod::Dot;
        let cost = (pos.abs_diff(start_pos)+amp_row_num+1)*find_amp_cost(row_amp);
        least_costs.push(move_amp(states_mem, cloned_state, cost_so_far + cost as i32));
    }
    return least_costs
}

// parses input into usable format
fn parse(text: &String) -> (Rows, Hallway) {
    let rows: Rows = text.lines().skip(2).take(4)
        .map(|line| {
            line.chars().filter(|chr| {chr.is_alphabetic()}).map(|c| char_to_amp(c)).collect()
        }).collect();
    let hallway = vec![Amhipod::Dot; 11];
    (rows, hallway)
}
