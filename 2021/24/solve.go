package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

// const file = "input-test.txt"
const file = "input.txt"

const N = 101

type Instruction = struct {
	op   string
	arg1 int
	arg2 string
}

var argToMem = map[string]int{
	"w": 0,
	"x": 1,
	"y": 2,
	"z": 3,
}

var memToArg = map[int]string{
	0: "w",
	1: "x",
	2: "y",
	3: "z",
}

func readLine(line string) *Instruction {
	s := strings.Split(line, " ")

	res := Instruction{
		op:   s[0],
		arg1: argToMem[s[1]],
	}

	if len(s) == 3 {
		res.arg2 = s[2]
	}

	return &res
}

func execute(ins *Instruction, mem *[4]int, input *[]int) {

	if ins.op == "inp" {
		mem[ins.arg1] = (*input)[0]
		*input = (*input)[1:]
		return
	}

	var second int
	if val, ok := argToMem[ins.arg2]; ok {
		second = mem[val]
	} else {
		second, _ = strconv.Atoi(ins.arg2)
	}

	switch ins.op {
	case "add":
		mem[ins.arg1] += second
	case "mul":
		mem[ins.arg1] *= second
	case "div":
		mem[ins.arg1] /= second
	case "mod":
		mem[ins.arg1] %= second
	case "eql":
		if mem[ins.arg1] == second {
			mem[ins.arg1] = 1
		} else {
			mem[ins.arg1] = 0
		}
	}
}

func print(ins *Instruction, mem *[4]int, input *[]int) {
	fmt.Printf("%3s, %2s, %3s | ", ins.op, memToArg[ins.arg1], ins.arg2)
	fmt.Printf("%9d %9d %9d %9d | ", mem[0], mem[1], mem[2], mem[3])
	fmt.Print(input)
	fmt.Println()
}
func printHeader() {
	fmt.Printf("op , a1, a2 | ")
	fmt.Printf("        W         X         Y         Z | ")
	fmt.Printf("IN")
	fmt.Println()
}

func main() {
	dat, _ := os.ReadFile(file)
	lines := strings.Split(string(dat), "\n")

	// lines = lines[0:18]
	instr := make([]*Instruction, len(lines))

	for idx, line := range lines {
		instr[idx] = readLine(line)
	}

	var mem [4]int
	input := []int{9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9}
	printHeader()
	for _, ins := range instr {
		if ins.op == "inp" {
			fmt.Println()
			print(&Instruction{}, &mem, &input)

		}
		print(ins, &mem, &input)
		execute(ins, &mem, &input)
	}

	// for sub := 0; sub < 14; sub++ {
	// 	program := instr[sub*18 : (sub+1)*18]
	// 	fmt.Println("-----------", sub, "-----------")

	// 	for i := 1; i < 10; i++ {

	// 		for z := 0; z < 300; z++ {

	// 			mem := [4]int{0, 0, 0, z}
	// 			input := &[]int{i}
	// 			// printHeader()
	// 			for _, ins := range program {
	// 				// print(ins, &mem, input)
	// 				execute(ins, &mem, input)
	// 			}

	// 			if mem[3] == 0 {

	// 				fmt.Printf("I: %2d, Z: %2d R: %2d\n", i, z, mem[3])
	// 			}
	// 		}

	// 	}
	// }

	// fmt.Println(memory)
}
