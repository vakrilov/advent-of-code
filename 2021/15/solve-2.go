package main

import (
	"fmt"
	"math"
	"os"
	"strings"
	"time"
)

func elapsed(what string) func() {
	start := time.Now()
	return func() {
		fmt.Printf("%s took %v\n", what, time.Since(start))
	}
}

const N = 100
const file = "input.txt"

// const N = 10
// const file = "input-test.txt"

type Node struct {
	cost int
	x    int
	y    int
}

type NodeHeap []Node

func (h NodeHeap) Len() int           { return len(h) }
func (h NodeHeap) Less(i, j int) bool { return h[i].cost < h[j].cost }
func (h NodeHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *NodeHeap) Push(x interface{}) {
	*h = append(*h, x.(Node))
}

func (h *NodeHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func main() {
	dat, _ := os.ReadFile(file)
	lines := strings.Split(string(dat), "\n")

	var board [N * 5][N * 5]int
	var costs [N * 5][N * 5]int
	var visited [N * 5][N * 5]bool
	for row := 0; row < N; row++ {
		for col := 0; col < N; col++ {
			val := int(lines[row][col]) - '0'

			for i := 0; i < 5; i++ {
				for j := 0; j < 5; j++ {
					board[row+i*N][col+j*N] = 1 + (val+i+j-1)%9
					costs[row+i*N][col+j*N] = math.MaxInt64
				}
			}
		}
	}
	costs[0][0] = 0

	defer elapsed("run")()

	update := func(row int, col int, cost int) {
		if row < 0 || col < 0 || row >= N*5 || col >= N*5 || visited[row][col] {
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

		if cRow == N*5-1 && cCol == N*5-1 {
			break
		}

		bestCost := math.MaxInt64
		for row := 0; row < N*5; row++ {
			for col := 0; col < N*5; col++ {
				if !visited[row][col] && bestCost > costs[row][col] {
					cRow, cCol, bestCost = row, col, costs[row][col]
				}
			}
		}
	}

	fmt.Println(costs[N*5-1][N*5-1])
}
