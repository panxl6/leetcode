/*
Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.



Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
Example 2:

Input: s = "1326#"
Output: "acz"
Example 3:

Input: s = "25#"
Output: "y"
Example 4:

Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
Output: "abcdefghijklmnopqrstuvwxyz"

*/

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
package main

import (
	"fmt"
	"strconv"
)

func main() {
	fmt.Println(freqAlphabets("1326#"))
}

func freqAlphabets(t string) string {
	s := []byte(t)
	flagStr := "#"
	flag := []byte(flagStr)
	var alphaArray []string
	for i := len(s) - 1; i >= 0; i-- {
		if s[i] == flag[0] {
			alphaArray = append(alphaArray, string(s[i-2:i+1]))
			i -= 2
		} else {
			alphaArray = append(alphaArray, string(s[i]))
		}
	}

	var result string
	dataMap := genDigitToAlphaMap()
	for i := len(alphaArray) - 1; i >= 0; i-- {
		result += dataMap[alphaArray[i]]
	}
	return result
}

const ALPHA_SIZE = 26

func genDigitToAlphaMap() map[string]string {
	dataMap := make(map[string]string)
	for i := 1; i <= ALPHA_SIZE; i++ {
		if i < 10 {
			key := strconv.Itoa(i)
			dataMap[key] = fmt.Sprintf("%c", i+96)
		} else {
			key := strconv.Itoa(i) + "#"
			dataMap[key] = fmt.Sprintf("%c", i+96)
		}
	}
	return dataMap
}
