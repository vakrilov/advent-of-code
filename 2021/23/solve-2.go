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

type Rooms = [4][4]rune
type Halls = [7]rune

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

func isWin(rooms *Rooms) bool {
	return rooms[0][0] == 'a' && rooms[0][1] == 'a' && rooms[0][2] == 'a' && rooms[0][3] == 'a' &&
		rooms[1][0] == 'b' && rooms[1][1] == 'b' && rooms[1][2] == 'b' && rooms[1][3] == 'b' &&
		rooms[2][0] == 'c' && rooms[2][1] == 'c' && rooms[2][2] == 'c' && rooms[2][3] == 'c' &&
		rooms[3][0] == 'd' && rooms[3][1] == 'd' && rooms[3][2] == 'd' && rooms[3][3] == 'd'
}

func moveFromRoomToHall(fromRoom, toHall int, rooms Rooms, halls Halls, currentCost int, trace []Step) (bool, int) {
	// print(rooms, halls)
	room := &rooms[fromRoom]
	depth := 0
	for depth < 4 && room[depth] == '.' {
		depth++
	}

	if depth == 4 {
		return false, 0
	}

	aType := room[depth]
	isSameTypeAsRoom := int(aType-'a') == fromRoom

	if isSameTypeAsRoom {
		// don't leave the correct room unless there are different fishes underneath
		hasDifferent := false
		for i := depth + 1; i < 4; i++ {
			if room[i] != aType {
				hasDifferent = true
			}
		}
		if !hasDifferent {
			return false, 0
		}
	}

	route := roomToHallMap[strconv.Itoa(fromRoom)+"|"+strconv.Itoa(toHall)]
	for _, hallPos := range route.path {
		if halls[hallPos] != '.' {
			// path is blocked
			return false, 0
		}
	}

	pathLength := route.cost + depth
	room[depth] = '.'
	halls[toHall] = aType
	cost := typeToCost[aType] * pathLength
	// print(rooms, halls)
	return move(rooms, halls, currentCost+cost, append(trace, Step{room: fromRoom, hall: toHall, isRoomToHall: true}))
}

func moveFromHallToRoom(fromHall, toRoom int, rooms Rooms, halls Halls, currentCost int, trace []Step) (bool, int) {
	// print(rooms, halls)

	aType := halls[fromHall]
	room := &rooms[toRoom]

	if aType == '.' {
		return false, 0
	}

	if int(aType-'a') != toRoom {
		// not the correct room type
		return false, 0
	}

	if room[0] != '.' {
		// room is full
		return false, 0
	}

	depth := 0
	for i := 0; i < 4; i++ {
		if room[i] == '.' {
			depth++
		} else if room[i] != aType {
			// cannot go to a room occupied with a wrong type fish
			return false, 0
		}
	}
	depth--

	route := hallToRoomMap[strconv.Itoa(fromHall)+"|"+strconv.Itoa(toRoom)]
	for _, hallPos := range route.path {
		if halls[hallPos] != '.' {
			return false, 0
		}
	}

	pathLength := route.cost + depth
	room[depth] = aType
	halls[fromHall] = '.'
	cost := typeToCost[aType] * pathLength
	// print(rooms, halls)
	return move(rooms, halls, currentCost+cost, append(trace, Step{room: toRoom, hall: fromHall, isRoomToHall: false}))
}

var count = 0

func move(rooms Rooms, halls Halls, cost int, trace []Step) (bool, int) {
	count++
	if count%1000000 == 0 {
		fmt.Println("move: ", cost, trace)
	}

	if len(trace) > 32 {
		print(rooms, halls)
		fmt.Println("Trace: ", trace)
		panic("Trace too long")
	}

	if isWin(&rooms) {
		count++
		if count%1000 == 0 {
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

func print(rooms Rooms, halls Halls) {
	fmt.Println()
	fmt.Printf("|%c%c.%c.%c.%c.%c%c|\n", halls[0], halls[1], halls[2], halls[3], halls[4], halls[5], halls[6])
	fmt.Printf("  |%c|%c|%c|%c|\n", rooms[0][0], rooms[1][0], rooms[2][0], rooms[3][0])
	fmt.Printf("  |%c|%c|%c|%c|\n", rooms[0][1], rooms[1][1], rooms[2][1], rooms[3][1])
	fmt.Printf("  |%c|%c|%c|%c|\n", rooms[0][2], rooms[1][2], rooms[2][2], rooms[3][2])
	fmt.Printf("  |%c|%c|%c|%c|\n", rooms[0][3], rooms[1][3], rooms[2][3], rooms[3][3])
	fmt.Println()
}

func main() {
	//input
	// rooms := Rooms{
	// 	{'c', 'd', 'd', 'b'},
	// 	{'a', 'c', 'b', 'a'},
	// 	{'d', 'b', 'а', 'b'},
	// 	{'d', 'a', 'c', 'c'},
	// }

	// test
	// rooms := Rooms{
	// 	{'b', 'd', 'd', 'a'},
	// 	{'c', 'c', 'b', 'd'},
	// 	{'b', 'b', 'а', 'c'},
	// 	{'d', 'a', 'c', 'a'},
	// }

	// test
	rooms := Rooms{
		{'b', 'a', 'a', 'a'},
		{'a', 'b', 'b', 'b'},
		{'d', 'c', 'c', 'c'},
		{'c', 'd', 'd', 'd'},
	}

	halls := Halls{'.', '.', '.', '.', '.', '.', '.'}
	print(rooms, halls)
	fmt.Println(move(rooms, halls, 0, nil))
}
