package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func Map(str []string, f func(string) int) []int {
	res := make([]int, len(str))
	for i, v := range str {
		res[i] = f(v)
	}
	return res
}

func LineToInts(line string, sep rune) []int {
	splitFn := func(c rune) bool {
		return c == sep
	}

	return Map(
		strings.FieldsFunc(line, splitFn),
		func(s string) int {
			num, _ := strconv.Atoi(s)
			return num
		})
}

var wins = [10][5][2]int{
	{{0, 0}, {0, 1}, {0, 2}, {0, 3}, {0, 4}},
	{{1, 0}, {1, 1}, {1, 2}, {1, 3}, {1, 4}},
	{{2, 0}, {2, 1}, {2, 2}, {2, 3}, {2, 4}},
	{{3, 0}, {3, 1}, {3, 2}, {3, 3}, {3, 4}},
	{{4, 0}, {4, 1}, {4, 2}, {4, 3}, {4, 4}},

	{{0, 0}, {1, 0}, {2, 0}, {3, 0}, {4, 0}},
	{{0, 1}, {1, 1}, {2, 1}, {3, 1}, {4, 1}},
	{{0, 2}, {1, 2}, {2, 2}, {3, 2}, {4, 2}},
	{{0, 3}, {1, 3}, {2, 3}, {3, 3}, {4, 3}},
	{{0, 4}, {1, 4}, {2, 4}, {3, 4}, {4, 4}},
}

func sumUnmarked(board [][]int, set map[int]bool) int {
	sum := 0
	for i := 0; i < 5; i++ {
		for j := 0; j < 5; j++ {
			num := board[i][j]
			if !set[num] {
				sum += num
			}
		}
	}

	return sum
}
func check(board [][]int, set map[int]bool) (bool, int) {
	for _, win := range wins {
		if set[board[win[0][0]][win[0][1]]] &&
			set[board[win[1][0]][win[1][1]]] &&
			set[board[win[2][0]][win[2][1]]] &&
			set[board[win[3][0]][win[3][1]]] &&
			set[board[win[4][0]][win[4][1]]] {

			return true, sumUnmarked(board, set)
		}
	}

	return false, 0
}

func main() {
	dat, _ := os.ReadFile("input.txt")
	boards := make([][][]int, 100)

	// dat, _ := os.ReadFile("input-test.txt")
	// boards := make([][][]int, 3)

	lines := strings.Split(string(dat), "\n")
	nums := LineToInts(lines[0], ',')
	for i := 2; i < len(lines); i += 6 {
		idx := i / 6
		boards[idx] = make([][]int, 5)
		boards[idx][0] = LineToInts(lines[i], ' ')
		boards[idx][1] = LineToInts(lines[i+1], ' ')
		boards[idx][2] = LineToInts(lines[i+2], ' ')
		boards[idx][3] = LineToInts(lines[i+3], ' ')
		boards[idx][4] = LineToInts(lines[i+4], ' ')
	}

	// // Part 1
	// set := make(map[int]bool)
	// result := 0
	// idx := 0
	// num := 0
	// for ; idx < len(nums) && result == 0; idx++ {
	// 	num = nums[idx]
	// 	set[num] = true
	// 	for boardIdx := 0; boardIdx < len(boards) && result == 0; boardIdx++ {
	// 		result = check(boards[boardIdx], set)
	// 	}
	// }

	// Part 2
	set := make(map[int]bool)
	result := 0
	idx := 0
	num := 0

	for _, num := range nums {
		set[num] = true
	}

	for idx = len(nums) - 1; idx > 0 && result == 0; idx-- {
		num = nums[idx]
		set[num] = false
		for boardIdx := 0; boardIdx < len(boards) && result == 0; boardIdx++ {
			isWin, _ := check(boards[boardIdx], set)
			if !isWin {
				set[num] = true
				isWin, result = check(boards[boardIdx], set)
			}
		}
	}

	fmt.Println(result * num)

}
