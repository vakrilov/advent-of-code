package main

import "fmt"

func main() {
	limit := 1000
	// pos1, pos2 := 4, 8
	pos1, pos2 := 8, 5
	score1, score2 := 0, 0

	dieRolls := 0
	roll := func() int {
		result := dieRolls%100 + 1
		dieRolls++
		return result
	}

	takeTurn := func(pos, score int) (nextPos, nextScore int) {
		nextPos = (pos+roll()+roll()+roll()-1)%10 + 1
		nextScore += score + nextPos
		return
	}

	for {
		pos1, score1 = takeTurn(pos1, score1)
		if score1 >= limit {
			break
		}

		pos2, score2 = takeTurn(pos2, score2)
		if score2 >= limit {
			break
		}
	}

	if score1 > score2 {
		fmt.Println("Part 1:", score2*dieRolls)
	} else {
		fmt.Println("Part 1:", score1*dieRolls)
	}
}
