package main

import (
	"fmt"
	"os"
	"strings"
)

// const file = "input-test.txt"
const file = "input.txt"

func print(board *[][]rune) {
	for _, row := range *board {
		for _, r := range row {
			fmt.Printf("%c", r)
		}
		fmt.Println()
	}
}

func main() {
	dat, _ := os.ReadFile(file)
	lines := strings.Split(string(dat), "\n")
	// fmt.Println(memory)

	ROWS, COLS := len(lines), len(lines[0])
	board := make([][]rune, ROWS)

	for row, line := range lines {
		board[row] = make([]rune, COLS)
		for col, r := range line {
			board[row][col] = r
		}
	}

	each := func(cb func(row, col int)) {
		for i := 0; i < ROWS; i++ {
			for j := 0; j < COLS; j++ {
				cb(i, j)
			}
		}
	}

	eastIsEmpty := func(row, col int) bool {
		return board[row][(col+1)%COLS] == '.'
	}

	southIsEmpty := func(row, col int) bool {
		return board[(row+1)%ROWS][col] == '.'
	}

	fmt.Println("INITIAL")
	print(&board)

	count := 0
	moveRow := make([]int, ROWS*COLS)
	moveCol := make([]int, ROWS*COLS)
	step := 0
	moved := true
	for moved {
		step++
		moved = false

		each(func(row, col int) {
			if board[row][col] == '>' && eastIsEmpty(row, col) {
				moveCol[count] = col
				moveRow[count] = row
				count++
			}
		})

		if count > 0 {
			moved = true
			for i := 0; i < count; i++ {
				row := moveRow[i]
				col := moveCol[i]
				nextCol := (col + 1) % COLS
				board[row][col], board[row][nextCol] = board[row][nextCol], board[row][col]
			}
			count = 0
		}

		each(func(row, col int) {
			if board[row][col] == 'v' && southIsEmpty(row, col) {
				moveCol[count] = col
				moveRow[count] = row
				count++
			}
		})

		if count > 0 {
			moved = true
			for i := 0; i < count; i++ {
				row := moveRow[i]
				col := moveCol[i]
				nextRow := (row + 1) % ROWS
				board[row][col], board[nextRow][col] = board[nextRow][col], board[row][col]
			}
			count = 0
		}
	}
	fmt.Println()
	fmt.Println()
	fmt.Println()
	fmt.Println("Step", step)
	print(&board)
}
