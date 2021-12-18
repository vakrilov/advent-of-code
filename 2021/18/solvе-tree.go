package main

import (
	"fmt"
	"os"
	"strings"
)

// const file = "input-test.txt"

const file = "input.txt"

type TreeNode struct {
	// level int
	value int
	left  *TreeNode
	right *TreeNode
}

func makeNum(line string) (*TreeNode, int) {
	if line[0] == '[' {
		left, lenL := makeNum(line[1:])
		right, lenR := makeNum(line[1+lenL+1:])

		return &TreeNode{
			left:  left,
			right: right,
		}, lenL + lenR + 3
	} else {
		return &TreeNode{
			value: int(line[0]) - '0',
		}, 1
	}
}

func (tree *TreeNode) dfs(cb func(*TreeNode, *TreeNode, int), parent *TreeNode, lvl int) {
	if tree.left != nil {
		tree.left.dfs(cb, tree, lvl+1)
		tree.right.dfs(cb, tree, lvl+1)
	} else {
		cb(tree, parent, lvl)
	}
}

func (tree *TreeNode) clone() *TreeNode {
	if tree.left != nil {
		return &TreeNode{left: tree.left.clone(), right: tree.right.clone()}
	} else {
		return &TreeNode{value: tree.value}
	}
}

func (tree *TreeNode) reduce() bool {
	var list []*TreeNode
	var explodeIdx int
	var explodeParent *TreeNode
	count := 0
	tree.dfs(func(node *TreeNode, parent *TreeNode, lvl int) {
		list = append(list, node)
		if lvl == 5 && explodeParent == nil {
			explodeIdx = count
			explodeParent = parent
		}
		count++
	}, nil, 0)

	if explodeParent != nil {
		leftVal, rightVal := list[explodeIdx].value, list[explodeIdx+1].value
		explodeParent.left, explodeParent.right = nil, nil
		explodeParent.value = 0
		if explodeIdx > 0 {
			list[explodeIdx-1].value += leftVal
		}

		if explodeIdx < len(list)-2 {
			list[explodeIdx+2].value += rightVal
		}
		return true
	}

	hasSplit := false
	tree.dfs(func(node *TreeNode, _ *TreeNode, _ int) {
		v := node.value
		if !hasSplit && v > 9 {
			node.value = 0
			node.left = &TreeNode{value: v / 2}
			node.right = &TreeNode{value: v/2 + v%2}
			hasSplit = true
		}
	}, nil, 0)

	return hasSplit
}

func (tree *TreeNode) reduceAll() *TreeNode {
	hasReduced := tree.reduce()
	for hasReduced {
		hasReduced = tree.reduce()
	}
	return tree
}

func (tree *TreeNode) magnitude() int {
	if tree.left != nil {
		return 3*tree.left.magnitude() + 2*tree.right.magnitude()
	} else {
		return tree.value
	}
}

func add(x, y *TreeNode) *TreeNode {
	return (&TreeNode{
		left:  x.clone(),
		right: y.clone(),
	}).reduceAll()
}

func main() {
	dat, _ := os.ReadFile(file)
	lines := strings.Split(string(dat), "\n")

	var nums []*TreeNode
	for _, line := range lines {
		num, _ := makeNum(line)
		nums = append(nums, num)
	}

	num := nums[0]
	for _, next := range nums[1:] {
		num = add(num, next)
	}

	fmt.Println("Part 1:", num.magnitude())

	max := 0
	for idx, x := range nums[:len(nums)-1] {
		for _, y := range nums[idx+1:] {
			if val := add(x, y).magnitude(); val > max {
				max = val
			}
			if val := add(y, x).magnitude(); val > max {
				max = val
			}
		}
	}

	fmt.Println("Part 2:", max)
}
