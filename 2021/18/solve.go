package main

import (
	"container/list"
	"fmt"
	"os"
	"strings"
)

const file = "input-test.txt"

// const file = "input.txt"

type node struct {
	level int
	value int
}

func explode(num *list.List, left *list.Element) {
	right := left.Next()

	new := num.InsertBefore(&node{value: 0, level: 4}, left)
	num.Remove(left)
	num.Remove(right)

	if prev := new.Prev(); prev != nil {
		prev.Value.(*node).value += left.Value.(*node).value
	}

	if next := new.Next(); next != nil {
		next.Value.(*node).value += right.Value.(*node).value
	}
}

func split(num *list.List, e *list.Element) {
	v := e.Value.(*node)
	v1 := v.value / 2
	v2 := v.value/2 + v.value%2

	num.InsertAfter(&node{
		value: v2,
		level: v.level + 1,
	}, e)
	num.InsertAfter(&node{
		value: v1,
		level: v.level + 1,
	}, e)
	num.Remove(e)
}

func reduce(num *list.List) bool {
	hasReduced := false
	// check explodes
	for e := num.Front(); e != nil; e = e.Next() {
		v := e.Value.(*node)
		if v.level == 5 {
			explode(num, e)
			hasReduced = true
			break
		}
	}

	if !hasReduced {
		for e := num.Front(); e != nil; e = e.Next() {
			v := e.Value.(*node)
			if v.value >= 10 {
				split(num, e)
				hasReduced = true
				break
			}
		}
	}

	return hasReduced
}

func print(num *list.List) {
	// for e := num.Front(); e != nil; e = e.Next() {
	// 	v := e.Value.(*node)
	// 	fmt.Println(strings.Repeat("  ", v.level-1), v.value)
	// }
	lastLvl := 0
	for e := num.Front(); e != nil; e = e.Next() {
		v := e.Value.(*node)
		if lastLvl < v.level {
			fmt.Print(strings.Repeat("[", v.level-lastLvl))
		} else if lastLvl > v.level {
			fmt.Print(strings.Repeat("]", lastLvl-v.level))
		} else {
			fmt.Print(",")
		}
		fmt.Print(v.value)

		lastLvl = v.level
	}
	fmt.Println(strings.Repeat("]", lastLvl))

}

func makeNum(line string) *list.List {
	num := list.New()

	lvl := 0
	for _, r := range line {
		switch r {
		case '[':
			lvl++
		case ']':
			lvl--
		case ',':
			// noop
		default:
			n := node{
				value: int(r - '0'),
				level: lvl,
			}
			num.PushBack(&n)
		}
	}
	return num
}

func add(x, y *list.List) *list.List {
	num := list.New()
	for e := x.Front(); e != nil; e = e.Next() {
		v := e.Value.(*node)
		num.PushBack(&node{
			level: v.level + 1,
			value: v.value,
		})
	}

	for e := y.Front(); e != nil; e = e.Next() {
		v := e.Value.(*node)
		num.PushBack(&node{
			level: v.level + 1,
			value: v.value,
		})
	}

	reduceAll(num)

	return num
}

func reduceAll(num *list.List) *list.List {
	hasReduced := reduce(num)
	for hasReduced {
		hasReduced = reduce(num)
	}
	return num
}

func main() {
	dat, _ := os.ReadFile(file)
	lines := strings.Split(string(dat), "\n")
	num := makeNum(lines[0])

	for _, nextLine := range lines[1:] {
		num = add(num, makeNum(nextLine))
	}

	// // line := "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"
	// line := "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"
	// num := makeNum(line)

	// fmt.Println(num)
	print(num)
}
