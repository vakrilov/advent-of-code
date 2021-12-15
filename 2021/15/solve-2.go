package main

import (
	"container/heap"
	"fmt"
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
	col  int
	row  int
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
	var visited [N * 5][N * 5]bool
	for row := 0; row < N; row++ {
		for col := 0; col < N; col++ {
			val := int(lines[row][col]) - '0'
			for i := 0; i < 5; i++ {
				for j := 0; j < 5; j++ {
					board[row+i*N][col+j*N] = 1 + (val+i+j-1)%9
				}
			}
		}
	}

	defer elapsed("run")()

	h := &NodeHeap{Node{col: 0, row: 0, cost: 0}}
	heap.Init(h)

	update := func(row int, col int, cost int) {
		if row < 0 || col < 0 || row >= N*5 || col >= N*5 || visited[row][col] {
			return
		}

		heap.Push(h, Node{col: col, row: row, cost: cost + board[row][col]})
	}

	visit := func(n *Node) {
		visited[n.row][n.col] = true
		update(n.row-1, n.col, n.cost)
		update(n.row+1, n.col, n.cost)
		update(n.row, n.col-1, n.cost)
		update(n.row, n.col+1, n.cost)
	}

	for h.Len() > 0 {
		current := heap.Pop(h).(Node)
		if visited[current.row][current.col] {
			continue
		}
		if current.row == N*5-1 && current.col == N*5-1 {
			fmt.Println(current.cost)
			break
		}

		visit(&current)
	}
}
