impl Solution {
    pub fn smallest_range_i(nums: Vec<i32>, k: i32) -> i32 {
        let min_value = nums.iter().min().unwrap() + k;
        let mut max_value = nums.iter().max().unwrap() - k;
        if max_value < min_value {
            max_value = min_value;
        }
        max_value - min_value
    }
}