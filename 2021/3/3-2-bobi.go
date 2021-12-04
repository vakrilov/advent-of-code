package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	dat, err := os.ReadFile("3.txt")
	if err != nil {
		panic(err)
	}

	lines := strings.Split(string(dat), "\n")

	linesI := make([]int64, 0, 1000)
	for _, x := range lines {
		xI, _ := strconv.ParseInt(x, 2, 64)
		linesI = append(linesI, xI)
	}

	ox := calcFilter(linesI, func(i int64) bool { return i >= 0 })
	co2 := calcFilter(linesI, func(i int64) bool { return i < 0 })
	fmt.Printf("%#b * %#b = %d\n", ox, co2, ox*co2)
}

func calcFilter(lines []int64, cmp func(int64) bool) int64 {
	selection := make([]int64, 0, 1000)
	var mask int64
	var mcb int64
	pos := 12

	for len(lines) > 1 {
		if pos == 0 {
			return mask
		}

		selection = selection[:0]
		mcb = 0
		for _, v := range lines {
			if v>>pos != mask {
				continue
			}
			if (v>>(pos-1))%2 == 1 {
				mcb++
			} else {
				mcb--
			}
			selection = append(selection, v)
		}
		mask = mask << 1
		if cmp(mcb) {
			mask++
		}
		pos--
		lines = selection
	}
	return lines[0]
}
