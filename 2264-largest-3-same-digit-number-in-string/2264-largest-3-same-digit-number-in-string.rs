impl Solution {
    pub fn largest_good_integer(num: String) -> String {
        let chars: Vec<char> = num.chars().collect();
        let mut max_val: i8 = -1;
        let mut prev_c: char = chars[0];
        let mut answer: String = String::from("");
        let mut count: u8 = 1;
        for (i, c) in chars.iter().enumerate() {
            if i != 0 {
                if prev_c == *c {
                    count += 1;
                } else {
                    if count >= 3 {
                        if prev_c as i8 > max_val { 
                            answer = format!("{}{}{}", prev_c, prev_c, prev_c);
                            max_val = prev_c as i8;
                        }
                    }
                    count = 1;
                }
            }
            prev_c = *c;
        }

        if count >= 3 {
            if prev_c as i8 > max_val { 
                answer = format!("{}{}{}", prev_c, prev_c, prev_c);
                max_val = prev_c as i8;
            }
        }

        return answer;
    }
}