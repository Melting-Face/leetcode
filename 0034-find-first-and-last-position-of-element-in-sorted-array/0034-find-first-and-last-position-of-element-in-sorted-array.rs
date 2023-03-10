impl Solution {
    pub fn search_range(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut answer: Vec<i32> = [-1, -1].to_vec();
        let mut find_target: bool = false;
        if nums.len() > 0 {
            for (idx, num) in nums.iter().enumerate() {
                if *num == target && find_target == false {
                    answer[0] = idx as i32;
                    find_target = true;
                } else if *num != target && find_target == true {
                    answer[1] = (idx - 1) as i32;
                    break;
                }
            }
        }

        if answer[0] != -1 && answer[1] == -1 {
            answer[1] = (nums.len() - 1) as i32;
        }

        return answer;
    }
}