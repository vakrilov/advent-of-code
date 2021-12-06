package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

var mem [9][257]int

func calc(timeTillProd int, daysLeft int) int {
	if mem[timeTillProd][daysLeft] != 0 {
		return mem[timeTillProd][daysLeft]
	}

	if daysLeft <= timeTillProd {
		return 1
	}

	prodDay := daysLeft - timeTillProd - 1
	result := calc(6, prodDay) + calc(8, prodDay)
	mem[timeTillProd][daysLeft] = result
	return result

}

func main() {
	// dat, _ := os.ReadFile("input-test.txt")
	dat, _ := os.ReadFile("input.txt")
	var fishes []int

	for _, numstr := range strings.Split(string(dat), ",") {
		num, _ := strconv.Atoi(numstr)
		fishes = append(fishes, num)
	}

	sum := 0
	for _, fish := range fishes {
		sum += calc(fish, 256)
	}

	fmt.Println(sum)
}
