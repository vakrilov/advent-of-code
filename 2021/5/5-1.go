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
		x1, y1, x2, y2 := LineToInts(line)

		if x1 == x2 {
			if y1 > y2 {
				y1, y2 = y2, y1
			}

			for i := y1; i <= y2; i++ {
				board[x1][i] += 1
			}
		} else if y1 == y2 {
			if x1 > x2 {
				x1, x2 = x2, x1
			}

			for i := x1; i <= x2; i++ {
				board[i][y1] += 1
			}
		}
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
