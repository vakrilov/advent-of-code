package main

import (
	"fmt"
	"os"
	"strconv"
)

// const file = "input.txt"
// const file = "input-test.txt"
const file = "input-test2.txt"

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

type Packet struct {
	version int
	id      int
	length  int
	value   int
	sub     *[]Packet
}

func parseBits(in string) int {
	r, _ := strconv.ParseInt(in, 2, 64)
	return int(r)
}

func readLiteral(in string) (int, int) {
	idx := 0
	value := 0
	for {
		value = value << 4
		value += parseBits(in[idx+1 : idx+5])
		idx += 5
		if in[idx-5] == '0' {
			break
		}
	}
	return value, idx
}

func readOperator(in string) (*[]Packet, int) {
	subPackets := make([]Packet, 0)

	if in[0] == '0' {
		subLength := parseBits(in[1:16])

		idx := 0
		for idx < subLength {
			p := readPacket(in[idx+16:])
			subPackets = append(subPackets, p)
			idx += p.length
		}

		return &subPackets, 16 + subLength
	} else {
		packetCount := parseBits(in[1:12])
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
	version := parseBits(in[0:3])
	id := parseBits(in[3:6])

	versionSum += version

	if id == 4 {
		value, literalLen := readLiteral(in[6:])

		return Packet{
			version: version,
			id:      id,
			length:  literalLen + 6,
			value:   value,
			sub:     nil,
		}
	} else {
		sub, length := readOperator(in[6:])
		return Packet{
			version: version,
			id:      id,
			length:  length + 6,
			value:   0,
			sub:     sub,
		}
	}
}

func eval(p *Packet) int {
	if p.id == 4 {
		return p.value
	}

	values := make([]int, len(*p.sub))
	for i := 0; i < len(values); i++ {
		values[i] = eval(&(*p.sub)[i])
	}

	switch p.id {
	case 5:
		if values[0] > values[1] {
			return 1
		} else {
			return 0
		}
	case 6:
		if values[0] < values[1] {
			return 1
		} else {
			return 0
		}
	case 7:
		if values[0] == values[1] {
			return 1
		} else {
			return 0
		}
	case 0:
		res := 0
		for _, v := range values {
			res += v
		}
		return res
	case 1:
		res := 1
		for _, v := range values {
			res *= v
		}
		return res
	case 2:
		res := values[0]
		for _, v := range values[1:] {
			if res > v {
				res = v
			}
		}
		return res
	case 3:
		res := values[0]
		for _, v := range values[1:] {
			if res < v {
				res = v
			}
		}
		return res
	}
	return 0
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
