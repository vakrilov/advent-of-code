package main

import (
	"fmt"
	"os"
	"strings"
	"unicode"
)

// const file = "input-test.txt"

// const file = "input-test2.txt"

// const file = "input-test3.txt"

const file = "input.txt"

func main() {
	dat, _ := os.ReadFile(file)

	lines := strings.Split(string(dat), "\n")

	nodes := make(map[string][]string)

	for _, line := range lines {
		caves := strings.Split(line, "-")

		if _, ok := nodes[caves[0]]; !ok {
			nodes[caves[0]] = make([]string, 0)
		}
		nodes[caves[0]] = append(nodes[caves[0]], caves[1])

		if _, ok := nodes[caves[1]]; !ok {
			nodes[caves[1]] = make([]string, 0)
		}
		nodes[caves[1]] = append(nodes[caves[1]], caves[0])
	}

	isSmall := func(node string) bool {
		return unicode.IsLower(rune(node[0]))
	}

	visited := make(map[string]bool)
	pathCount := 0
	smallCaveTwice := false
	var visit func(string, []string)
	visit = func(node string, path []string) {
		if node == "start" && path != nil {
			return
		}

		if node == "end" {
			pathCount++
			fmt.Println(append(path, node))
			return
		}

		if isSmall(node) && visited[node] && smallCaveTwice {
			return
		}

		shouldReset := false
		if isSmall(node) && visited[node] {
			smallCaveTwice = true
			shouldReset = true
		}

		visited[node] = true
		for _, next := range nodes[node] {
			visit(next, append(path, node))
		}
		if shouldReset {
			smallCaveTwice = false
		} else {
			visited[node] = false
		}
	}

	visit("start", nil)

	fmt.Println(pathCount)
}
