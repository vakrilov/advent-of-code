package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	dat, _ := os.ReadFile("input.txt")
	count := 0
	for _, line := range strings.Split(string(dat), "\n") {
		output := strings.Split(line, "|")[1]
		digits := strings.Split(output[1:], " ")

		for _, digit := range digits {
			l := len(digit)
			if l == 2 || l == 3 || l == 4 || l == 7 {
				count++
			}
		}
	}

	fmt.Println(count)

}
