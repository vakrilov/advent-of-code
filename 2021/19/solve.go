package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

const file = "input-test.txt"

// const file = "input.txt"

type Transform = [3][3]int

var transforms = []Transform{
	{
		{1, 0, 0},
		{0, 1, 0},
		{0, 0, 1},
	}, {
		{-1, 0, 0},
		{0, -1, 0},
		{0, 0, 1},
	}, {
		{-1, 0, 0},
		{0, 1, 0},
		{0, 0, -1},
	}, {
		{1, 0, 0},
		{0, -1, 0},
		{0, 0, -1},
	},
}

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

func (a *Point) sub(b *Point) *Point {
	return &Point{
		x: a.x - b.x,
		y: a.y - b.y,
		z: a.z - b.z,
	}
}

func (a *Point) add(b *Point) *Point {
	return &Point{
		x: a.x + b.x,
		y: a.y + b.y,
		z: a.z + b.z,
	}
}

func transform(p *Point, t *Transform) *Point {
	return &Point{
		x: p.x*t[0][0] + p.y*t[0][1] + p.z*t[0][2],
		y: p.x*t[1][0] + p.y*t[1][1] + p.z*t[1][2],
		z: p.x*t[2][0] + p.y*t[2][1] + p.z*t[2][2],
	}
}

func (p Point) String() string {
	return fmt.Sprintf("(%d, %d, %d)", p.x, p.y, p.z)
}

func matchWithTransform(sc1, sc2 []*Point, t *Transform) (bool, int) {
	distances := make(map[int]int)
	for _, p1 := range sc1 {
		for _, p2 := range sc2 {
			transfromedPoint := transform(p2, t)
			distances[dist(p1, transfromedPoint)]++
		}
	}

	for k, v := range distances {
		if v >= 12 {
			fmt.Println("FOUND: matches", v, "distance", k)
			return true, k
		}
	}

	return false, 0
}

func tryMatch(sc1, sc2 []*Point) bool {
	isMatch, targetDist := false, -1
	var trans *Transform
	for _, t := range transforms {
		isMatch, targetDist = matchWithTransform(sc1, sc2, &t)
		if isMatch {
			trans = &t
			break
		}
	}

	if !isMatch {
		return false
	}

	// rotate scanner
	for idx, p := range sc2 {
		sc2[idx] = transform(p, trans)
	}

	// find tranlate and do translate
	translate := find(sc1, sc2, targetDist)
	for idx, p := range sc2 {
		sc2[idx] = p.add(translate)
	}
	return true
}

func find(sc1, sc2 []*Point, targetargetDist int) *Point {
	for _, p1 := range sc1 {
		for _, p2 := range sc2 {
			if dist(p1, p2) == targetargetDist {
				return p1.sub(p2)
			}
		}
	}
	return nil
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

	tryMatch(scanners[0], scanners[1])

	// fmt.Println(len(distances))
}
