package main

import (
	"fmt"
	"math"
	"os"
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

func main() {
	dat, _ := os.ReadFile("input-test.txt")
	// dat, _ := os.ReadFile("input.txt")
	var positions []int

	min, max := 5000, 0
	for _, numstr := range strings.Split(string(dat), ",") {
		num, _ := strconv.Atoi(numstr)
		positions = append(positions, num)
		min = Min(min, num)
		max = Max(max, num)
	}

	result := math.MaxInt64
	for goal := min; goal <= max; goal++ {
		sum := 0
		for _, num := range positions {
			diff := AbsDiff(num, goal)
			// Part 1
			// sum += diff

			//Part 2
			sum += (diff * (diff + 1)) / 2
		}

		result = Min(sum, result)
	}

	fmt.Println(result)
}
