package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
	"time"
)

// const file = "input-test2.txt"

const file = "input.txt"

type Cube = struct {
	x1, x2 int
	y1, y2 int
	z1, z2 int
	setTo  bool
}

func readLine(line string) *Cube {
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

	return &Cube{
		x1:    x1,
		x2:    x2,
		y1:    y1,
		y2:    y2,
		z1:    z1,
		z2:    z2,
		setTo: setTo,
	}
}

func check(x, y, z int, cubes []*Cube) bool {
	result := false

	for _, c := range cubes {
		if c.z1 <= z && z <= c.z2 {
			result = c.setTo
		}
	}

	return result
}

func elapsed(what string) func() {
	start := time.Now()
	return func() {
		fmt.Printf("%s took %v\n", what, time.Since(start))
	}
}

func main() {
	dat, _ := os.ReadFile(file)
	lines := strings.Split(string(dat), "\n")

	defer elapsed("run")()

	cubes := make([]*Cube, len(lines))

	xMap := make(map[int]bool)
	yMap := make(map[int]bool)
	zMap := make(map[int]bool)

	for idx, line := range lines {
		cube := readLine(line)
		cubes[idx] = cube

		xMap[cube.x1] = true
		xMap[cube.x2+1] = true
		yMap[cube.y1] = true
		yMap[cube.y2+1] = true
		zMap[cube.z1] = true
		zMap[cube.z2+1] = true
	}

	xBorders := make([]int, 0, len(xMap))
	for key := range xMap {
		xBorders = append(xBorders, key)
	}

	yBorders := make([]int, 0, len(yMap))
	for key := range yMap {
		yBorders = append(yBorders, key)
	}

	zBorders := make([]int, 0, len(zMap))
	for key := range zMap {
		zBorders = append(zBorders, key)
	}

	sort.Ints(xBorders)
	sort.Ints(yBorders)
	sort.Ints(zBorders)

	result := 0
	for i := 0; i < len(xBorders)-1; i++ {
		x := xBorders[i]

		filteredCubesX := make([]*Cube, 0, len(lines))
		for _, c := range cubes {
			if c.x1 <= x && x <= c.x2 {
				filteredCubesX = append(filteredCubesX, c)
			}
		}

		for j := 0; j < len(yBorders)-1; j++ {
			y := yBorders[j]

			filteredCubesY := make([]*Cube, 0, len(filteredCubesX))
			for _, c := range filteredCubesX {
				if c.y1 <= y && y <= c.y2 {
					filteredCubesY = append(filteredCubesY, c)
				}
			}

			for k := 0; k < len(zBorders)-1; k++ {
				z := zBorders[k]

				if check(x, y, z, filteredCubesY) {
					result += (xBorders[i+1] - x) * (yBorders[j+1] - y) * (zBorders[k+1] - z)
				}
			}
		}
	}

	fmt.Println(result)
}
