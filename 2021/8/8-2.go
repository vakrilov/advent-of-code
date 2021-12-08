package main

import (
	"fmt"
	"os"
	"strings"
)

func containsCount(digit string, from string) int {
	count := 0
	for _, r := range from {
		if strings.ContainsRune(digit, r) {
			count++
		}
	}
	return count
}
func containsAll(digit string, from string) bool {
	return containsCount(digit, from) == len(from)
}

func matchLen5(digit string, one string, four string) int {
	if containsAll(digit, one) {
		return 3
	}

	countFour := containsCount(digit, four)

	if countFour == 2 {
		return 2
	} else if countFour == 3 {
		return 5
	} else {
		fmt.Println("ERROR")
		return -1
	}
}

func matchLen6(digit string, one string, four string) int {
	containsOne := containsAll(digit, one)
	containsFour := containsAll(digit, four)

	if containsOne && containsFour {
		return 9
	} else if containsOne {
		return 0
	} else {
		return 6
	}
}

func main() {
	dat, _ := os.ReadFile("input.txt")
	sum := 0
	for _, line := range strings.Split(string(dat), "\n") {
		split := strings.Split(line, "|")
		inputs := strings.Split(split[0], " ")
		outputs := strings.Split(split[1][1:], " ")

		var one string
		var four string

		for _, digit := range inputs {
			if len(digit) == 2 {
				one = digit
			}
			if len(digit) == 4 {
				four = digit
			}
		}

		localValue := 0
		for _, digit := range outputs {
			localValue *= 10
			l := len(digit)

			var value int
			switch l {
			case 2:
				value = 1
			case 3:
				value = 7
			case 4:
				value = 4
			case 7:
				value = 8
			case 5:
				value = matchLen5(digit, one, four)
			case 6:
				value = matchLen6(digit, one, four)
			}

			localValue += value
		}
		sum += localValue
	}

	fmt.Println(sum)

}
