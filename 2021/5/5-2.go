package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func LineToInts(line string) (x1 int, y1 int, x2 int, y2 int) {
	nums := strings.Split(strings.ReplaceAll(line, " -> ", ","), ",")
	x1, _ = strconv.Atoi(nums[0])
	y1, _ = strconv.Atoi(nums[1])
	x2, _ = strconv.Atoi(nums[2])
	y2, _ = strconv.Atoi(nums[3])
	return
}

func main() {

	// dat, _ := os.ReadFile("input-test.txt")
	// N := 10
	// var board [10][10]int

	dat, _ := os.ReadFile("input.txt")
	N := 1000
	var board [1000][1000]int

	for _, line := range strings.Split(string(dat), "\n") {
		y1, x1, y2, x2 := LineToInts(line)

		xStep := 0
		if x1 < x2 {
			xStep = 1
		} else if x1 > x2 {
			xStep = -1
		}

		yStep := 0
		if y1 < y2 {
			yStep = 1
		} else if y1 > y2 {
			yStep = -1
		}

		for x, y := x1, y1; x != x2 || y != y2; x, y = x+xStep, y+yStep {
			board[x][y]++
		}
		board[x2][y2]++
	}

	count := 0
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			if board[i][j] > 1 {
				count++
			}
		}
	}

	fmt.Println(count)

}
