use log::info;

pub fn add(a: i32, b: i32) -> i32 {
    info!("adding {a} and {b}");
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(add(2, 3), 5);
    }
}
