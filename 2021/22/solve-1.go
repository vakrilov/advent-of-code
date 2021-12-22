package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

// const file = "input-test.txt"

const file = "input.txt"
const N = 101

type Cube = struct {
	x1, x2 int
	y1, y2 int
	z1, z2 int
}

func readLine(line string) (bool, *Cube) {
	idx := 0
	setTo := false
	if line[0:2] == "on" {
		setTo = true
		idx = 3
	} else {
		setTo = false
		idx = 4
	}

	ranges := strings.Split(line[idx:], ",")

	x1, _ := strconv.Atoi(strings.Split(ranges[0], "..")[0][2:])
	x2, _ := strconv.Atoi(strings.Split(ranges[0], "..")[1])
	y1, _ := strconv.Atoi(strings.Split(ranges[1], "..")[0][2:])
	y2, _ := strconv.Atoi(strings.Split(ranges[1], "..")[1])
	z1, _ := strconv.Atoi(strings.Split(ranges[2], "..")[0][2:])
	z2, _ := strconv.Atoi(strings.Split(ranges[2], "..")[1])

	res := Cube{
		x1: x1 + 50,
		x2: x2 + 50,
		y1: y1 + 50,
		y2: y2 + 50,
		z1: z1 + 50,
		z2: z2 + 50,
	}
	return setTo, &res
}

func main() {
	dat, _ := os.ReadFile(file)
	lines := strings.Split(string(dat), "\n")

	var board [N][N][N]bool

	for _, line := range lines[:20] {
		setTo, cube := readLine(line)

		for i := cube.x1; i <= cube.x2; i++ {
			for j := cube.y1; j <= cube.y2; j++ {
				for k := cube.z1; k <= cube.z2; k++ {
					board[i][j][k] = setTo
				}
			}
		}
	}

	count := 0
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			for k := 0; k < N; k++ {
				if board[i][j][k] {
					count++
				}
			}
		}
	}
	fmt.Println(count)
}
