package main

import (
	"container/list"
	"fmt"
	"os"
	"strings"
)

// const file = "input-test.txt"

const file = "input.txt"

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

	// check split
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
	for e := num.Front(); e != nil; e = e.Next() {
		v := e.Value.(*node)
		fmt.Println(strings.Repeat("  ", v.level), v.value)
	}
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

func eval(num *list.List) int {
	for lvl := 4; lvl > 0; lvl-- {
		for e := num.Front(); e != nil; e = e.Next() {
			v := e.Value.(*node)
			if v.level == lvl {
				vn := e.Next().Value.(*node)
				sum := v.value*3 + vn.value*2
				new := num.InsertBefore(&node{
					level: lvl - 1,
					value: sum,
				}, e)
				num.Remove(e.Next())
				num.Remove(e)
				e = new
			}
		}
	}

	return num.Front().Value.(*node).value
}

func main() {
	dat, _ := os.ReadFile(file)
	lines := strings.Split(string(dat), "\n")
	num := makeNum(lines[0])

	for _, nextLine := range lines[1:] {
		num = add(num, makeNum(nextLine))
	}

	fmt.Println("Part 1", eval(num))

	max := 0
	for i := 0; i < len(lines)-1; i++ {
		for j := 1; j < len(lines); j++ {
			a := lines[i]
			b := lines[j]

			sum1 := eval(add(makeNum(a), makeNum(b)))
			sum2 := eval(add(makeNum(b), makeNum(a)))
			if max < sum1 {
				max = sum1
			}
			if max < sum2 {
				max = sum2
			}
		}
	}
	fmt.Println("Part 2", max)
}
