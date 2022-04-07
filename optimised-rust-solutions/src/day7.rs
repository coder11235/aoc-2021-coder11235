pub fn part1(input: &String) -> i32{
    let positions: Vec<u16> = input.split(',')
        .map(|x| x.parse().unwrap()).collect();
    let max = *positions.iter().max().unwrap() as i32;
    let mut min_energy = f64::INFINITY as i32;
    for target in 0..max {
        let mut energy_consumed = 0;
        for crab in &positions {
            energy_consumed += (target-(*crab as i32)).abs();
        }
        if energy_consumed < min_energy {
            min_energy = energy_consumed;
        }
    }
    min_energy
}

pub fn part2(input: &String) -> i32{
    let positions: Vec<u16> = input.split(',')
        .map(|x| x.parse().unwrap()).collect();
    let max = *positions.iter().max().unwrap() as i32;
    let mut min_energy = f64::INFINITY as i32;
    for target in 0..max {
        let mut energy_consumed = 0;
        for crab in &positions {
            let dist = (target-(*crab as i32)).abs();
            energy_consumed += (dist*(dist+1))/2;
        }
        if energy_consumed < min_energy {
            min_energy = energy_consumed;
        }
    }
    min_energy
}