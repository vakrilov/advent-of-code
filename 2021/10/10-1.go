package main

import (
	"fmt"
	"os"
	"strings"
)

const file = "input.txt"

// const file = "input-test.txt"

func main() {
	dat, _ := os.ReadFile(file)

	lines := strings.Split(string(dat), "\n")

	result := 0
	errors := map[rune]int{
		')': 3,
		']': 57,
		'}': 1197,
		'>': 25137,
	}
	for _, line := range lines {

		var expected []rune

		for _, sym := range line {
			switch sym {
			case '(':
				expected = append(expected, ')')
			case '[':
				expected = append(expected, ']')
			case '{':
				expected = append(expected, '}')
			case '<':
				expected = append(expected, '>')
			case ')', ']', '}', '>':
				n := len(expected) - 1
				pop := expected[n]
				expected = expected[:n]
				if sym != pop {
					fmt.Println("Expected", string(pop), "but found", string(sym))
					result += errors[sym]
					break
				}
			}
		}
	}

	fmt.Println((result))
}
