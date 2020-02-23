# leetcode的解题方案

## 数字的位操作
大数加减是一个典型的入门题。当一个超级大的数，远超过编程语言能表达的数时，我们需要把这个大数保存成字符串数组。然后对这个字符串数组的每一位逐位运算。针对字符串的位做不同的运算，会衍生出一系列题型。将一个数字，按为分解成一个数字数组是一个基本操作。当然，也有些语言支持将数字转换为字符串的内置函数(atoi、itoa)。

```go
// 将一个整数按位分解为数字数组
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

// 将数字数组组装为一个整数
func getNumberFromBitArray(array []int) int {
	num, plus := 0, 1
	for i := 0; i < len(array); i++ {
		num += plus * array[i]
		plus *= 10
	}
	return num
}
```

| 题目　| 介绍 |
|---|---|
| [1281. Subtract the Product and Sum of Digits of an Integer](https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/)| 求一个数的诸位之积和诸位之和的差值 |
| [1323. Maximum 69 Number](https://leetcode.com/problems/maximum-69-number)| 将只有6和9组成的整数，只调整一个数字，求最大的结果 |

