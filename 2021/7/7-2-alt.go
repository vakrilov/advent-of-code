package main

import (
	"fmt"
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

func cost(positions []int, x int) int {
	result := 0
	for _, num := range positions {
		diff := AbsDiff(num, x)
		result += (diff * (diff + 1)) / 2
	}
	return result
}

func main() {
	// dat, _ := os.ReadFile("input-test.txt")
	dat, _ := os.ReadFile("input.txt")
	var positions []int

	sum := 0
	for _, numstr := range strings.Split(string(dat), ",") {
		num, _ := strconv.Atoi(numstr)
		positions = append(positions, num)
		sum += num
	}

	cost1 := cost(positions, sum/len(positions))
	cost2 := cost(positions, sum/len(positions)+1)
	result := Min(cost1, cost2)
	fmt.Println(result)
}
