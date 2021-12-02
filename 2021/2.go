package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	// Parse
	dat, err := os.ReadFile("2.txt")
	if err != nil {
		panic(err)
	}

	// Part 1
	// forward := 0
	// depth := 0
	// for _, line := range strings.Split(string(dat), "\n") {
	// 	strs := strings.Split(line, " ")

	// 	num, _ := strconv.Atoi(strs[1])
	// 	if strs[0] == "up" {
	// 		depth -= num
	// 	} else if strs[0] == "down" {
	// 		depth += num

	// 	} else {
	// 		forward += num
	// 	}
	// }

	// Part 2
	forward := 0
	depth := 0
	aim := 0
	for _, line := range strings.Split(string(dat), "\n") {
		strs := strings.Split(line, " ")

		num, _ := strconv.Atoi(strs[1])
		if strs[0] == "up" {
			aim -= num
		} else if strs[0] == "down" {
			aim += num

		} else {
			forward += num
			depth += num * aim
		}
	}

	fmt.Println(depth * forward)
}
