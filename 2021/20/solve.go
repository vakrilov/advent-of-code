package main

import (
	"fmt"
	"os"
	"strings"
)

// const file = "input-test.txt"
// const N = 5
// const OFF = 150

const file = "input.txt"
const N = 100
const OFF = 150

func get(plane [N + 2*OFF][N + 2*OFF]bool, row, col int) int {
	res := 0
	for i := row - 1; i <= row+1; i++ {
		for j := col - 1; j <= col+1; j++ {
			res *= 2
			if plane[i][j] {
				res += 1
			}
		}
	}
	return res
}
func main() {
	dat, _ := os.ReadFile(file)
	lines := strings.Split(string(dat), "\n")

	var enh [512]bool
	var currentPlane [N + 2*OFF][N + 2*OFF]bool
	var nextPlane [N + 2*OFF][N + 2*OFF]bool

	for i := 0; i < len(lines[0]); i++ {
		if lines[0][i] == '#' {
			enh[i] = true
		}
	}

	for row, line := range lines[2:] {
		for col, r := range line {
			if r == '#' {
				currentPlane[row+OFF][col+OFF] = true
			}
		}
	}

	for step := 1; step <= 50; step++ {
		// var next [N + 2*OFF][N + 2*OFF]bool
		count := 0
		for i := step; i < N+2*OFF-2*step; i++ {
			for j := step; j < N+2*OFF-2*step; j++ {
				val := get(currentPlane, i, j)
				nextPlane[i][j] = enh[val]
				if enh[val] {
					count++
				}
			}
		}
		fmt.Println("Step", step, ":", count)
		currentPlane, nextPlane = nextPlane, currentPlane
	}
}
