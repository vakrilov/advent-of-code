package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

const file = "input.txt"

// const file = "input-test.txt"

func merge(left [26]int, right [26]int) [26]int {
	var result [26]int
	for i := 0; i < len(result); i++ {
		result[i] = left[i] + right[i]
	}
	return result

}

func main() {
	dat, _ := os.ReadFile(file)

	lines := strings.Split(string(dat), "\n")

	start := lines[0]
	pairs := make(map[string]string)
	for _, line := range lines[2:] {
		pairs[line[0:2]] = string(line[6:7])
	}

	memo := make(map[string][26]int)

	var calc func(pair string, lvl int) [26]int
	calc = func(pair string, lvl int) [26]int {
		key := pair + strconv.Itoa(lvl)
		if mem, contains := memo[key]; contains {
			return mem
		}

		if lvl == 0 {
			var result [26]int
			return result
		}

		val, contains := pairs[pair]
		if !contains {
			var result [26]int
			return result
		}

		left := calc(pair[0:1]+val, lvl-1)
		right := calc(val+pair[1:2], lvl-1)

		result := merge(left, right)
		result[val[0]-'A']++

		memo[key] = result

		return result
	}

	var result [26]int
	steps := 40
	for i := 0; i < len(start)-1; i++ {
		next := calc(start[i:i+2], steps)
		result = merge(result, next)
	}

	for i := 0; i < len(start); i++ {
		result[start[i]-'A']++
	}

	fmt.Println(result)
	min := math.MaxInt64
	max := math.MinInt64
	for _, val := range result {
		if val == 0 {
			continue
		}

		if val < min {
			min = val
		}
		if val > max {
			max = val
		}
	}
	fmt.Println(max - min)

}
