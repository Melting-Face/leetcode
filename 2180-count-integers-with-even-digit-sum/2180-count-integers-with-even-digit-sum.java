import java.util.Arrays;
import java.util.stream.IntStream;

class Solution {
    public int countEven(int num) {
        int answer = 0;
        int numDividedByTen = num / 10;
        if (numDividedByTen == 0) {
          answer = IntStream.rangeClosed(1, num).map(n -> n % 2 == 0 ? 1 : 0).sum();
        } else if(numDividedByTen > 0) {
          answer = 4;
          int sumOfDigits = Arrays.stream(Integer.toString(numDividedByTen).split("")).mapToInt(Integer::parseInt).sum();
          answer += IntStream.range(1, numDividedByTen).parallel().map(n -> 5).sum();
          answer += IntStream.rangeClosed(numDividedByTen * 10, num)
            .parallel()
            .map(n -> (sumOfDigits + n) % 2 == 0 ? 1 : 0)
            .sum();
        } 
        
        return answer;
    }
}