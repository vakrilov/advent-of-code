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

var transforms = make([]Transform, 0, 24)

var id = &Transform{
	{1, 0, 0},
	{0, 1, 0},
	{0, 0, 1},
}

var rotateX = &Transform{
	{1, 0, 0},
	{0, 0, -1},
	{0, 1, 0},
}
var rotateY = &Transform{
	{0, 0, 1},
	{0, 1, 0},
	{-1, 0, 0},
}

var rotateZ = &Transform{
	{0, -1, 0},
	{1, 0, 0},
	{0, 0, 1},
}

func rotX(a *Transform) *Transform {
	return mul(a, rotateX)
}
func rotY(a *Transform) *Transform {
	return mul(a, rotateY)
}
func rotZ(a *Transform) *Transform {
	return mul(a, rotateZ)
}

func print(a *Transform) {
	fmt.Println()
	fmt.Println(a[0])
	fmt.Println(a[1])
	fmt.Println(a[2])
}

func mul(a, b *Transform) *Transform {
	var r Transform
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			r[i][j] = a[i][0]*b[0][j] + a[i][1]*b[1][j] + a[i][2]*b[2][j]
		}
	}
	return &r
}

func createTransforms() {
	var tranMap = make(map[Transform]bool)
	var mat = id
	tranMap[*mat] = true

	for z := 0; z < 4; z++ {
		mat = rotZ(mat)
		tranMap[*mat] = true
		for x := 0; x < 4; x++ {
			mat = rotX(mat)
			tranMap[*mat] = true
		}
	}

	mat = rotY(id)
	tranMap[*mat] = true
	for x := 0; x < 4; x++ {
		mat = rotX(mat)
		tranMap[*mat] = true
	}

	mat = rotY(rotY(rotY(id)))
	tranMap[*mat] = true
	for x := 0; x < 4; x++ {
		mat = rotX(mat)
		tranMap[*mat] = true
	}

	for k, _ := range tranMap {
		// print(&k)
		transforms = append(transforms, k)
	}
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

func (p *Point) transform(t *Transform) *Point {
	return &Point{
		x: p.x*t[0][0] + p.y*t[0][1] + p.z*t[0][2],
		y: p.x*t[1][0] + p.y*t[1][1] + p.z*t[1][2],
		z: p.x*t[2][0] + p.y*t[2][1] + p.z*t[2][2],
	}
}

func (p Point) String() string {
	return fmt.Sprintf("(%d, %d, %d)", p.x, p.y, p.z)
}

func matchWithTransform(sc1, sc2 []*Point, t *Transform) *Point {
	distances := make(map[Point]int)
	for _, p1 := range sc1 {
		for _, p2 := range sc2 {
			distances[*p1.sub(p2.transform(t))]++
		}
	}

	for k, v := range distances {
		if v >= 12 {
			fmt.Println("FOUND: matches", v, "distance", k)
			return &k
		}
	}

	return nil
}

func tryMatch(sc1, sc2 []*Point) bool {
	var rotateTransform *Transform
	var translateTransform *Point
	for _, t := range transforms {
		translateTransform = matchWithTransform(sc1, sc2, &t)
		if translateTransform != nil {
			rotateTransform = &t
			break
		}
	}

	if translateTransform == nil {
		return false
	}

	// find tranlate and do translate
	for idx, p := range sc2 {
		sc2[idx] = p.transform(rotateTransform).add(translateTransform)
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
	createTransforms()

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
				for matchedIdx, _ := range matchedScanners {
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
