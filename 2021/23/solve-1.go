package main

import (
	"fmt"
	"strconv"
)

type Route = struct {
	path []int
	cost int
}

type Step = struct {
	room         int
	hall         int
	isRoomToHall bool
}

var typeToCost = map[rune]int{
	'a': 1,
	'b': 10,
	'c': 100,
	'd': 1000,
}

var bestSolutionSoFar = 100000000

var roomToHallMap = map[string]Route{
	"0|0": {path: []int{1, 0}, cost: 3},
	"0|1": {path: []int{1}, cost: 2},
	"0|2": {path: []int{2}, cost: 2},
	"0|3": {path: []int{2, 3}, cost: 4},
	"0|4": {path: []int{2, 3, 4}, cost: 6},
	"0|5": {path: []int{2, 3, 4, 5}, cost: 8},
	"0|6": {path: []int{2, 3, 4, 5, 6}, cost: 9},
	"1|0": {path: []int{2, 1, 0}, cost: 5},
	"1|1": {path: []int{2, 1}, cost: 4},
	"1|2": {path: []int{2}, cost: 2},
	"1|3": {path: []int{3}, cost: 2},
	"1|4": {path: []int{3, 4}, cost: 4},
	"1|5": {path: []int{3, 4, 5}, cost: 6},
	"1|6": {path: []int{3, 4, 5, 6}, cost: 7},
	"2|0": {path: []int{3, 2, 1, 0}, cost: 7},
	"2|1": {path: []int{3, 2, 1}, cost: 6},
	"2|2": {path: []int{3, 2}, cost: 4},
	"2|3": {path: []int{3}, cost: 2},
	"2|4": {path: []int{4}, cost: 2},
	"2|5": {path: []int{4, 5}, cost: 4},
	"2|6": {path: []int{4, 5, 6}, cost: 5},
	"3|0": {path: []int{4, 3, 2, 1, 0}, cost: 9},
	"3|1": {path: []int{4, 3, 2, 1}, cost: 8},
	"3|2": {path: []int{4, 3, 2}, cost: 6},
	"3|3": {path: []int{4, 3}, cost: 4},
	"3|4": {path: []int{4}, cost: 2},
	"3|5": {path: []int{5}, cost: 2},
	"3|6": {path: []int{5, 6}, cost: 3},
}

var hallToRoomMap = map[string]Route{
	"0|0": {path: []int{1}, cost: 3},
	"0|1": {path: []int{1, 2}, cost: 5},
	"0|2": {path: []int{1, 2, 3}, cost: 7},
	"0|3": {path: []int{1, 2, 3, 4}, cost: 9},
	"1|0": {path: []int{}, cost: 2},
	"1|1": {path: []int{2}, cost: 4},
	"1|2": {path: []int{2, 3}, cost: 6},
	"1|3": {path: []int{2, 3, 4}, cost: 8},
	"2|0": {path: []int{}, cost: 2},
	"2|1": {path: []int{}, cost: 2},
	"2|2": {path: []int{3}, cost: 4},
	"2|3": {path: []int{3, 4}, cost: 6},
	"3|0": {path: []int{2}, cost: 4},
	"3|1": {path: []int{}, cost: 2},
	"3|2": {path: []int{}, cost: 2},
	"3|3": {path: []int{4}, cost: 4},
	"4|0": {path: []int{3, 2}, cost: 6},
	"4|1": {path: []int{3}, cost: 4},
	"4|2": {path: []int{}, cost: 2},
	"4|3": {path: []int{}, cost: 2},
	"5|0": {path: []int{4, 3, 2}, cost: 8},
	"5|1": {path: []int{4, 3}, cost: 6},
	"5|2": {path: []int{2}, cost: 4},
	"5|3": {path: []int{}, cost: 2},
	"6|0": {path: []int{5, 4, 3, 2}, cost: 9},
	"6|1": {path: []int{5, 4, 3}, cost: 7},
	"6|2": {path: []int{5, 4}, cost: 5},
	"6|3": {path: []int{5}, cost: 3},
}

func moveFromRoomToHall(fromRoom, toHall int, rooms [4][2]rune, halls [7]rune, currentCost int, trace []Step) (bool, int) {
	if rooms[fromRoom][0] == '.' && rooms[fromRoom][1] == '.' {
		return false, 0
	}

	aType := rooms[fromRoom][0]
	if aType == '.' {
		aType = rooms[fromRoom][1]
	}

	isOne := rooms[fromRoom][0] == '.'
	isSameType := int(aType-'a') == fromRoom

	if isOne && isSameType {
		// dont leave the room if it is the correct room, and we are the only fish
		return false, 0
	}

	if isSameType && rooms[fromRoom][1] == aType {
		// don't leave room if it is the correct room or there is incorrect fish underneath
		return false, 0
	}

	route := roomToHallMap[strconv.Itoa(fromRoom)+"|"+strconv.Itoa(toHall)]
	for _, hallPos := range route.path {
		if halls[hallPos] != '.' {
			// path is blocked
			return false, 0
		}
	}

	pathLength := route.cost
	if rooms[fromRoom][0] != '.' {
		rooms[fromRoom][0] = '.'
	} else if rooms[fromRoom][1] != '.' {
		rooms[fromRoom][1] = '.'
		pathLength++
	} else {
		panic("ERROR")
	}
	halls[toHall] = aType

	cost := typeToCost[aType] * pathLength
	// print(rooms, halls)

	return move(rooms, halls, currentCost+cost, append(trace, Step{room: fromRoom, hall: toHall, isRoomToHall: true}))
}

func moveFromHallToRoom(fromHall, toRoom int, rooms [4][2]rune, halls [7]rune, currentCost int, trace []Step) (bool, int) {
	aType := halls[fromHall]
	if aType == '.' {
		return false, 0
	}

	if int(aType-'a') != toRoom {
		// not the correct room type
		return false, 0
	}

	if rooms[toRoom][0] != '.' {
		// room is full
		return false, 0
	}

	if rooms[toRoom][1] != '.' && rooms[toRoom][1] != aType {
		// cannot go to a room occupied with a wrong type fish
		return false, 0
	}

	route := hallToRoomMap[strconv.Itoa(fromHall)+"|"+strconv.Itoa(toRoom)]
	for _, hallPos := range route.path {
		if halls[hallPos] != '.' {
			return false, 0
		}
	}

	pathLength := route.cost
	if rooms[toRoom][1] == '.' {
		rooms[toRoom][1] = aType
		pathLength++
	} else if rooms[toRoom][0] == '.' {
		rooms[toRoom][0] = aType
	} else {
		panic("ERROR 2")
	}

	halls[fromHall] = '.'
	cost := typeToCost[aType] * pathLength
	// print(rooms, halls)
	return move(rooms, halls, currentCost+cost, append(trace, Step{room: toRoom, hall: fromHall, isRoomToHall: false}))
}

var count = 0

func move(rooms [4][2]rune, halls [7]rune, cost int, trace []Step) (bool, int) {
	if len(trace) > 40 {
		print(rooms, halls)
		fmt.Println("Trace: ", trace)
		panic("Trace too long")
	}
	// print(rooms, halls)
	if rooms[0][0] == 'a' && rooms[0][1] == 'a' &&
		rooms[1][0] == 'b' && rooms[1][1] == 'b' &&
		rooms[2][0] == 'c' && rooms[2][1] == 'c' &&
		rooms[3][0] == 'd' && rooms[3][1] == 'd' {

		count++
		if count%100000 == 0 {
			fmt.Println("SOLUTION: ", cost, trace)
		}
		if cost < bestSolutionSoFar {
			bestSolutionSoFar = cost
		}
		// print(rooms, halls)
		return true, cost
	}

	if cost >= bestSolutionSoFar {
		return false, 0
	}

	best := 10000000
	for room := 0; room < 4; room++ {
		for hall := 0; hall < 7; hall++ {
			isOK, newCost := moveFromRoomToHall(room, hall, rooms, halls, cost, trace)
			if isOK && newCost < best {
				best = newCost
			}
		}
	}

	for room := 0; room < 4; room++ {
		for hall := 0; hall < 7; hall++ {
			isOK, newCost := moveFromHallToRoom(hall, room, rooms, halls, cost, trace)
			if isOK && newCost < best {
				best = newCost
			}
		}
	}

	if best < 10000000 {
		return true, best
	}
	return false, 0
}

func print(rooms [4][2]rune, halls [7]rune) {
	fmt.Println()
	fmt.Printf("|%c%c.%c.%c.%c.%c%c|\n", halls[0], halls[1], halls[2], halls[3], halls[4], halls[5], halls[6])
	fmt.Printf("  |%c|%c|%c|%c| \n", rooms[0][0], rooms[1][0], rooms[2][0], rooms[3][0])
	fmt.Printf("  |%c|%c|%c|%c|   \n", rooms[0][1], rooms[1][1], rooms[2][1], rooms[3][1])
	fmt.Println()
}

func main() {
	//input
	rooms := [4][2]rune{
		{'c', 'b'},
		{'a', 'a'},
		{'d', 'b'},
		{'d', 'c'},
	}

	// test
	// rooms := [4][2]rune{
	// 	{'b', 'a'},
	// 	{'c', 'd'},
	// 	{'b', 'c'},
	// 	{'d', 'a'},
	// }

	// rooms := [4][2]rune{
	// 	{'b', 'b'},
	// 	{'c', 'c'},
	// 	{'a', 'a'},
	// 	{'d', 'd'},
	// }
	halls := [7]rune{'.', '.', '.', '.', '.', '.', '.'}
	print(rooms, halls)
	fmt.Println(move(rooms, halls, 0, nil))
}
