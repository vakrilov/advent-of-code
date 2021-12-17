package main

import (
	"fmt"
	"math"
)

func main() {

	//target area: x=20..30, y=-10..-5
	// x1, x2, y1, y2 := 20, 30, -10, -5

	// target area: x=257..286, y=-101..-57
	x1, x2, y1, y2 := 257, 286, -101, -57

	fmt.Println("Part 1:", y1*(y1+1)/2)

	isIn := func(x, y int) bool {
		return x1 <= x && x <= x2 && y1 <= y && y <= y2
	}

	minY, maxY := y1, -y1
	minX, maxX := int(math.Floor(math.Sqrt(float64(2*x1)))), x2

	count := 0
	for x := minX; x <= maxX; x++ {
		for y := minY; y <= maxY; y++ {

			cx, cy := 0, 0
			vx, vy := x, y
			for cx <= x2 && cy >= y1 {
				if isIn(cx, cy) {
					count++
					break
				}
				cx += vx
				cy += vy
				vy--
				vx--
				if vx < 0 {
					vx = 0
				}
			}
		}
	}

	fmt.Println("Part 2:", count)
}
