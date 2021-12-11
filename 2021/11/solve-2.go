package main

import (
	"fmt"
	"os"
	"strings"
)

const N = 10

const file = "input.txt"

// const file = "input-test.txt"

func main() {
	dat, _ := os.ReadFile(file)
	var board [N][N]int

	lines := strings.Split(string(dat), "\n")
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[i]); j++ {
			board[i][j] = int(lines[i][j]) - 48
		}
	}

	flashes := 0
	queue := make(chan [2]int, 1000)

	iterateAll := func(cb func(row int, col int)) {
		for r := 0; r < N; r++ {
			for c := 0; c < N; c++ {
				cb(r, c)
			}
		}
	}

	increase := func(r int, c int) {
		if r < 0 || c < 0 || r >= N || c >= N {
			return
		}

		board[r][c] = board[r][c] + 1
		if board[r][c] == 10 {
			flashes++
			queue <- [2]int{r - 1, c - 1}
			queue <- [2]int{r - 1, c}
			queue <- [2]int{r - 1, c + 1}
			queue <- [2]int{r, c - 1}
			queue <- [2]int{r, c + 1}
			queue <- [2]int{r + 1, c - 1}
			queue <- [2]int{r + 1, c}
			queue <- [2]int{r + 1, c + 1}
		}
	}
	for i := 0; ; i++ {
		flashes = 0
		iterateAll(increase)

		for len(queue) > 0 {
			pop := <-queue
			increase(pop[0], pop[1])
		}

		iterateAll(func(r int, c int) {
			if board[r][c] > 9 {
				board[r][c] = 0
			}
		})

		if flashes == 100 {
			fmt.Println("All flashed on step: ", i+1)
			break
		}
	}
}
