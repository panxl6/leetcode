/*
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
Example 2:

Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
 

Constraints:

1 <= n <= 10^5
*/

package main

import (
	"fmt"
)

func main() {
	fmt.Println(subtractProductAndSum(4421))
}

func subtractProductAndSum(n int) int {
	bitArray := extractBitOfNum(n)
	return productArray(bitArray) - sumArray(bitArray)
}

func extractBitOfNum(num int) []int {
	bitArray := []int{}

	for num != 0 {
		n := num / 10
		digit := num - n*10
		num = n

		bitArray = append(bitArray, digit)
	}

	return bitArray
}

func sumArray(array []int) int {
	result := 0
	for _, value := range array {
		result += value
	}
	return result
}

func productArray(array []int) int {
	result := 1
	for _, value := range array {
		result *= value
	}
	return result
}

