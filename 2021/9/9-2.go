package main

import (
	"fmt"
	"os"
	"sort"
	"strings"
)

const COL = 100
const ROW = 100
const file = "input.txt"

// const COL = 10
// const ROW = 5
// const file = "input-test.txt"

func isLocalMin(board [ROW][COL]int, i int, j int) bool {
	val := board[i][j]
	if i > 0 && board[i-1][j] <= val {
		return false
	}
	if j > 0 && board[i][j-1] <= val {
		return false
	}
	if (i < ROW-1) && board[i+1][j] <= val {
		return false
	}
	if (j < COL-1) && board[i][j+1] <= val {
		return false
	}
	return true
}

func expand(board *[ROW][COL]int, i int, j int) int {
	if i < 0 || j < 0 || i >= ROW || j >= COL || board[i][j] == 9 {
		return 0
	}

	board[i][j] = 9

	return 1 +
		expand(board, i-1, j) +
		expand(board, i+1, j) +
		expand(board, i, j-1) +
		expand(board, i, j+1)
}

func main() {
	dat, _ := os.ReadFile(file)
	var board [ROW][COL]int

	lines := strings.Split(string(dat), "\n")
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[i]); j++ {
			board[i][j] = int(lines[i][j]) - 48
		}
	}

	var basins []int
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[i]); j++ {
			if isLocalMin(board, i, j) {
				basins = append(basins, expand(&board, i, j))
			}
		}
	}

	sort.Ints(basins)
	fmt.Println(basins[len(basins)-1] * basins[len(basins)-2] * basins[len(basins)-3])
}
