class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        let left = 0;
        let right = numbers.length - 1;
        let sum;
        while(numbers[left] + numbers[right] != target) {
            sum = numbers[left] + numbers[right];
            if(sum < target) {
                left++;
            } else if (sum > target) {
                right--;
            }
        }
        return [left+1, right+1];
    }
}
