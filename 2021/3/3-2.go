package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func elapsed(what string) func() {
	start := time.Now()
	return func() {
		fmt.Printf("%s took %v\n", what, time.Since(start))
	}
}

func main() {
	// Parse
	dat, err := os.ReadFile("3.txt")
	if err != nil {
		panic(err)
	}

	lines := strings.Split(string(dat), "\n")
	defer elapsed("run")()

	filtered := lines
	pos := 0

	for {
		var ones []string
		var zeros []string

		for _, line := range filtered {
			if line[pos:pos+1] == "1" {
				ones = append(ones, line)
			} else {
				zeros = append(zeros, line)
			}
		}

		if len(ones) >= len(zeros) {
			filtered = ones
		} else {
			filtered = zeros
		}

		if len(filtered) == 1 {
			break
		}
		pos++
	}

	ox, _ := strconv.ParseInt(filtered[0], 2, 64)
	fmt.Println(ox)

	filtered = lines
	pos = 0

	for {
		var ones []string
		var zeros []string

		for _, line := range filtered {
			if line[pos:pos+1] == "1" {
				ones = append(ones, line)
			} else {
				zeros = append(zeros, line)
			}
		}

		if len(zeros) <= len(ones) {
			filtered = zeros
		} else {
			filtered = ones
		}

		if len(filtered) == 1 {
			break
		}
		pos++
	}

	co2, _ := strconv.ParseInt(filtered[0], 2, 64)
	fmt.Println(co2)

	fmt.Println(ox * co2)

}
