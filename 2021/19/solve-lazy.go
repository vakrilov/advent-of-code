package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

// const file = "input-test.txt"

const file = "input.txt"

type Transform = [3][3]int
type Point struct {
	x, y, z int
}

func readPoint(line string) *Point {
	split := strings.Split(line, ",")
	x, _ := strconv.Atoi(split[0])
	y, _ := strconv.Atoi(split[1])
	z, _ := strconv.Atoi(split[2])
	return &Point{x: x, y: y, z: z}
}

func dist(a, b *Point) int {
	dx, dy, dz := a.x-b.x, a.y-b.y, a.z-b.z
	return dx*dx + dy*dy + dz*dz
}

func manhattanDist(a, b *Point) int {
	dx, dy, dz := a.x-b.x, a.y-b.y, a.z-b.z
	if dx < 0 {
		dx = -dx
	}
	if dy < 0 {
		dy = -dy
	}
	if dx < 0 {
		dz = -dz
	}
	return dx + dy + dz
}

func (p Point) String() string {
	return fmt.Sprintf("(%d, %d, %d)", p.x, p.y, p.z)
}

func tryMatch(sc1, sc2 []*Point) bool {
	distances := make(map[int]int)
	for i := 0; i < len(sc1)-1; i++ {
		for j := i + 1; j < len(sc1); j++ {
			d := dist(sc1[i], sc1[j])
			distances[d]++
		}
	}
	matched := 0
	for i := 0; i < len(sc2)-1; i++ {
		for j := i + 1; j < len(sc2); j++ {
			d := dist(sc2[i], sc2[j])
			if distances[d] > 0 {
				matched++
				distances[d]--
			}
		}
	}
	if matched >= 66 {
		fmt.Println("Found matches:", matched)
		return true
	}
	return false
}

func main() {
	dat, _ := os.ReadFile(file)
	lines := strings.Split(string(dat), "\n")

	var scanners [][]*Point
	for _, line := range lines {
		if len(line) == 0 {
			continue
		} else if line[0:3] == "---" {
			scanners = append(scanners, make([]*Point, 0, 100))
		} else {
			scanners[len(scanners)-1] = append(scanners[len(scanners)-1], readPoint(line))
		}
	}

	matchedScanners := make(map[int]bool)
	matchedScanners[0] = true

	for len(matchedScanners) < len(scanners) {
		for i := 0; i < len(scanners); i++ {
			if !matchedScanners[i] {
				for matchedIdx := range matchedScanners {
					matched := tryMatch(scanners[matchedIdx], scanners[i])
					if matched {
						matchedScanners[i] = true
						fmt.Println("Matched", i, "with", matchedIdx)
						break
					}
				}
			}
		}
	}

	points := make(map[Point]bool)
	for _, sc := range scanners {
		for _, p := range sc {
			points[*p] = true
		}
	}

	fmt.Println("Part 1:", len(points))

}
