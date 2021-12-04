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

	filtered := make([]string, len(lines))
	ones := make([]string, len(lines))
	zeros := make([]string, len(lines))

	buffer0 := &zeros
	buffer1 := &ones
	current := &filtered

	defer elapsed("run")()
	calculateMetric := func(mostCommon bool) int64 {
		*current = (*current)[:len(lines)] // change len
		copy(*current, lines)              // copy elements

		pos := 0
		for {
			*buffer0 = (*buffer0)[:0] // 1) Reusing slices will not allocate new memory ... right
			*buffer1 = (*buffer1)[:0]

			for _, line := range *current {
				if line[pos] == '1' { // 2) Is there a easier way to do a single rune check
					*buffer1 = append(*buffer1, line)
				} else {
					*buffer0 = append(*buffer0, line)
				}
			}

			tmp := current
			if (len(*buffer1) >= len(*buffer0)) == mostCommon {
				current = buffer1
				buffer1 = tmp

			} else {
				current = buffer0
				buffer0 = tmp
			}

			if len(*current) == 1 { // 3) This is basically a while (len(filtered) == 1) loop. No while loop in go though..
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
