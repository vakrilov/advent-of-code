package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	// Parse
	dat, err := os.ReadFile("3.txt")
	if err != nil {
		panic(err)
	}

	var positions [12]int
	for _, line := range strings.Split(string(dat), "\n") {
		for pos, ch := range line {
			if ch == '1' {
				positions[pos] += 1
			} else {
				positions[pos] -= 1
			}
		}
	}

	gamma := 0
	epsilon := 0
	for _, num := range positions {
		gamma *= 2
		epsilon *= 2
		if num > 0 {
			gamma += 1
		} else {
			epsilon += 1
		}
	}

	fmt.Println(gamma)
	fmt.Println(epsilon)
	fmt.Println(gamma * epsilon)
}
