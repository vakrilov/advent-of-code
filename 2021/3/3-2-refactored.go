package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func elapsed(what string) func() {
	start := time.Now()
	return func() {
		fmt.Printf("%s took %v\n", what, time.Since(start))
	}
}

func main() {
	// Parse
	dat, err := os.ReadFile("3.txt")
	if err != nil {
		panic(err)
	}

	lines := strings.Split(string(dat), "\n")
	defer elapsed("run")()

	filtered := make([]string, len(lines))
	ones := make([]string, len(lines))
	zeros := make([]string, len(lines))

	rewriteFiltered := func(from []string) {
		filtered = filtered[:len(from)] // change len
		copy(filtered, from)            // copy elements
	}

	calculateMetric := func(mostCommon bool) int64 {
		rewriteFiltered(lines)
		pos := 0
		for {
			ones = ones[:0] // 1) Reusing slices will not allocate new memory ... right
			zeros = zeros[:0]

			for _, line := range filtered {
				if line[pos] == '1' { // 2) Is there a easier way to do a single rune check
					ones = append(ones, line)
				} else {
					zeros = append(zeros, line)
				}
			}

			if (len(ones) >= len(zeros)) == mostCommon {
				rewriteFiltered(ones)
			} else {
				rewriteFiltered(zeros)
			}

			if len(filtered) == 1 { // 3) This is basically a while (len(filtered) == 1) loop. No while loop in go though..
				break
			}
			pos++
		}

		ox, _ := strconv.ParseInt(filtered[0], 2, 64)
		return ox
	}

	ox := calculateMetric(true)
	c02 := calculateMetric(false)

	fmt.Println(ox)
	fmt.Println(c02)
	fmt.Println(c02 * ox)
}
