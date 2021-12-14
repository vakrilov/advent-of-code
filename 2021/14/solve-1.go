package main

import (
	"fmt"
	"math"
	"os"
	"strings"
)

// const file = "input.txt"

const file = "input-test.txt"

type node struct {
	next  *node
	value string
}

func insertAfter(current *node, newNode *node) *node {
	newNode.next = current.next
	current.next = newNode
	return newNode
}

func main() {
	dat, _ := os.ReadFile(file)

	lines := strings.Split(string(dat), "\n")

	start := node{value: lines[0][0:1]}
	current := &start
	for _, r := range lines[0][1:] {
		new := node{value: string(r)}
		current = insertAfter(current, &new)
	}

	pairs := make(map[string]string)
	for _, line := range lines[2:] {
		pairs[line[0:2]] = string(line[6:7])
	}

	for i := 0; i < 10; i++ {
		fmt.Println("Step", i)
		for current = &start; current.next != nil; current = current.next {
			key := current.value + current.next.value
			val, contains := pairs[key]
			if contains {
				new := node{value: string(val)}
				current = insertAfter(current, &new)
			}
		}
	}

	counts := make(map[string]int)
	for current = &start; current != nil; current = current.next {
		counts[current.value] = counts[current.value] + 1
	}

	min := math.MaxInt64
	max := math.MinInt64

	for _, val := range counts {
		if val < min {
			min = val
		}
		if val > max {
			max = val
		}
	}

	fmt.Println(max - min)
}
