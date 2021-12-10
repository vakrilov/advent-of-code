package main

import (
	"fmt"
	"os"
	"sort"
	"strings"
)

const file = "input.txt"

// const file = "input-test.txt"

func main() {
	dat, _ := os.ReadFile(file)

	lines := strings.Split(string(dat), "\n")

	points := map[rune]int{
		')': 1,
		']': 2,
		'}': 3,
		'>': 4,
	}

	var scores []int

	for _, line := range lines {

		var expected []rune
		corrupted := false
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
					corrupted = true
					break
				}
			}
		}

		if len(expected) > 0 && !corrupted {
			fmt.Println("Line: ", line, "complete", string(expected))

			score := 0
			for i := len(expected) - 1; i >= 0; i-- {
				score *= 5
				score += points[expected[i]]
			}

			scores = append(scores, score)

		}
	}

	sort.Ints(scores)
	fmt.Println(scores[len(scores)/2])
}
