package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	// Parse
	dat, err := os.ReadFile("1.txt")
	if err != nil {
		panic(err)
	}

	nums := make([]int, 0, 2000)
	for _, line := range strings.Split(string(dat), "\n") {
		num, _ := strconv.Atoi(line)
		nums = append(nums, num)
	}

	count := 0
	// Part 1
	// for idx, next := range nums[1:] {

	// Part 2
	for idx, next := range nums[3:] {
		if nums[idx] < next {
			count++
		}
	}
	fmt.Print(count)
}
