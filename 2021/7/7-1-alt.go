package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func AbsDiff(x, y int) int {
	if x < y {
		return y - x
	}
	return x - y
}

func Min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func cost(positions []int, x int) int {
	result := 0
	for _, num := range positions {
		result += AbsDiff(num, x)
	}
	return result
}

func main() {
	// dat, _ := os.ReadFile("input-test.txt")
	dat, _ := os.ReadFile("input.txt")
	var positions []int

	for _, numstr := range strings.Split(string(dat), ",") {
		num, _ := strconv.Atoi(numstr)
		positions = append(positions, num)
	}

	sort.Ints(positions)

	result := cost(positions, positions[len(positions)/2])
	fmt.Println(result)
}
