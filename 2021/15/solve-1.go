package main

import (
	"fmt"
	"math"
	"os"
	"strings"
)

const N = 100
const file = "input.txt"

// const N = 10
// const file = "input-test.txt"

func main() {
	dat, _ := os.ReadFile(file)
	lines := strings.Split(string(dat), "\n")

	var board [N][N]int
	var costs [N][N]int
	var visited [N][N]bool
	for row := 0; row < N; row++ {
		for col := 0; col < N; col++ {
			board[row][col] = int(lines[row][col]) - '0'
			costs[row][col] = math.MaxInt64
		}
	}
	costs[0][0] = 0

	update := func(row int, col int, cost int) {
		if row < 0 || col < 0 || row >= N || col >= N || visited[row][col] {
			return
		}

		if costs[row][col] > cost+board[row][col] {
			costs[row][col] = cost + board[row][col]
		}
	}

	visit := func(row int, col int) {
		visited[row][col] = true
		currentCost := costs[row][col]

		update(row-1, col, currentCost)
		update(row+1, col, currentCost)
		update(row, col-1, currentCost)
		update(row, col+1, currentCost)

	}

	cRow, cCol := 0, 0

	for {
		visit(cRow, cCol)

		if cRow == N-1 && cCol == N-1 {
			break
		}

		bestCost := math.MaxInt64
		for row := 0; row < N; row++ {
			for col := 0; col < N; col++ {
				if !visited[row][col] && bestCost > costs[row][col] {
					cRow, cCol, bestCost = row, col, costs[row][col]
				}
			}
		}
	}

	fmt.Println(costs[N-1][N-1])
}
