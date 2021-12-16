package main

import (
	"fmt"
	"os"
	"strconv"
)

const file = "input.txt"

// const file = "input-test.txt"
// const file = "input-test2.txt"

var versionSum int

var hex2bin = map[rune]string{
	'0': "0000",
	'1': "0001",
	'2': "0010",
	'3': "0011",
	'4': "0100",
	'5': "0101",
	'6': "0110",
	'7': "0111",
	'8': "1000",
	'9': "1001",
	'A': "1010",
	'B': "1011",
	'C': "1100",
	'D': "1101",
	'E': "1110",
	'F': "1111",
}

var type2func = map[int]func(a int, b int) int{
	0: func(a int, b int) int { return a + b },
	1: func(a int, b int) int { return a * b },
	2: func(a int, b int) int {
		if a < b {
			return a
		}
		return b
	},
	3: func(a int, b int) int {
		if a > b {
			return a
		}
		return b
	},
	5: func(a int, b int) int {
		if a > b {
			return 1
		}
		return 0
	},
	6: func(a int, b int) int {
		if a < b {
			return 1
		}
		return 0
	},
	7: func(a int, b int) int {
		if a == b {
			return 1
		}
		return 0
	},
}

type Packet struct {
	version int
	id      int
	length  int
	value   int
	sub     *[]Packet
}

func readBits(in string) int {
	r, _ := strconv.ParseInt(in, 2, 64)
	return int(r)
}

func readLiteral(in string) (int, int) {
	idx := 0
	value := 0
	for {
		value = value << 4
		value += readBits(in[idx+1 : idx+5])
		idx += 5
		if in[idx-5] == '0' {
			break
		}
	}
	return value, idx
}

func readOperator(in string) (*[]Packet, int) {
	subPackets := make([]Packet, 0, 2)

	if in[0] == '0' {
		subLength := readBits(in[1:16])

		idx := 0
		for idx < subLength {
			p := readPacket(in[idx+16:])
			subPackets = append(subPackets, p)
			idx += p.length
		}

		return &subPackets, 16 + subLength
	} else {
		packetCount := readBits(in[1:12])
		idx := 12
		for i := 0; i < packetCount; i++ {
			p := readPacket(in[idx:])
			subPackets = append(subPackets, p)
			idx += p.length
		}
		return &subPackets, idx
	}
}

func readPacket(in string) Packet {
	version := readBits(in[0:3])
	id := readBits(in[3:6])

	versionSum += version
	result := Packet{
		version: version,
		id:      id,
	}

	if id == 4 {
		value, literalLen := readLiteral(in[6:])
		result.length, result.value = literalLen+6, value
	} else {
		result.sub, result.length = readOperator(in[6:])
	}
	return result
}

func eval(p *Packet) int {
	if p.id == 4 {
		return p.value
	}

	f := type2func[p.id]

	// Poor man's reduce
	acc := eval(&(*p.sub)[0])
	for i := 1; i < len(*p.sub); i++ {
		next := eval(&(*p.sub)[i])
		acc = f(acc, next)
	}

	return acc
}

func main() {
	dat, _ := os.ReadFile(file)
	input := string(dat)
	inputBin := ""
	for _, r := range input {
		inputBin += hex2bin[r]
	}

	p := readPacket(inputBin)
	fmt.Println(p)
	fmt.Println("Part 1:", versionSum)
	fmt.Println("Part 2:", eval(&p))
}
