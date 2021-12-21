package main

import (
	"fmt"
	"strconv"
)

var mul = [10]int{0, 0, 0, 1, 3, 6, 7, 6, 3, 1}
var memo = make(map[string][2]int)
var limit = 21

func turn(pos, score, diceValue int) (nextPos, nextScore int) {
	nextPos = (pos+diceValue-1)%10 + 1
	nextScore += score + nextPos
	return
}

func solve(pos1, score1, pos2, score2 int) (int, int) {
	key := strconv.Itoa(pos1) + "|" + strconv.Itoa(pos2) + "|" + strconv.Itoa(score1) + "|" + strconv.Itoa(score2)
	if mem, contains := memo[key]; contains {
		return mem[0], mem[1]
	}
	if score1 >= limit {
		return 1, 0
	}
	if score2 >= limit {
		return 0, 1
	}

	totalPl1Wins, totalPl2Wins := 0, 0
	for diceVal := 3; diceVal <= 9; diceVal++ {
		nextPos1, nextScore1 := turn(pos1, score1, diceVal)
		pl2Wins, pl1Wins := solve(pos2, score2, nextPos1, nextScore1)

		totalPl1Wins += pl1Wins * mul[diceVal]
		totalPl2Wins += pl2Wins * mul[diceVal]
	}

	memo[key] = [2]int{totalPl1Wins, totalPl2Wins}
	return totalPl1Wins, totalPl2Wins
}

func main() {
	// pl1Wins, pl2Wins := solve(4, 0, 8, 0)
	pl1Wins, pl2Wins := solve(8, 0, 5, 0)
	fmt.Println("Player 1 wins in:", pl1Wins)
	fmt.Println("Player 2 wins in:", pl2Wins)
}
