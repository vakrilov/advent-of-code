package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

const file = "input.txt"

// const file = "input-test.txt"

type fold struct {
	axis  string
	value int
}

func hash(x int, y int) int {
	return x*10000 + y
}

func dehash(h int) (int, int) {
	return h / 10000, h % 10000
}

func main() {
	dat, _ := os.ReadFile(file)

	lines := strings.Split(string(dat), "\n")

	points := make(map[int]bool)
	folds := make([]fold, 0)

	for _, line := range lines {
		if line == "" {
			continue
		} else if strings.Contains(line, "x=") {
			val, _ := strconv.Atoi(line[13:])
			folds = append(folds, fold{axis: "x", value: val})
		} else if strings.Contains(line, "y=") {
			val, _ := strconv.Atoi(line[13:])
			folds = append(folds, fold{axis: "y", value: val})
		} else {
			split := strings.Split(line, ",")
			x, _ := strconv.Atoi(split[0])
			y, _ := strconv.Atoi(split[1])
			points[hash(x, y)] = true
		}
	}

	for i, currentFold := range folds {
		v := currentFold.value
		if currentFold.axis == "y" {
			for h, _ := range points {
				x, y := dehash(h)
				delete(points, h)

				if y > v {
					y = 2*v - y
				}
				points[hash(x, y)] = true
			}
		} else {
			for h, _ := range points {
				x, y := dehash(h)
				delete(points, h)

				if x > v {
					x = 2*v - x
				}
				points[hash(x, y)] = true
			}
		}
		fmt.Println("Points after fold", i, ":", len(points))
	}

	for y := 0; y < 6; y++ {
		fmt.Println()
		for x := 0; x < 40; x++ {
			if points[hash(x, y)] {
				fmt.Print("#")
			} else {
				fmt.Print(".")
			}

		}
	}
}
