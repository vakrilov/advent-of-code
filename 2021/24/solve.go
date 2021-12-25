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

func createFunc(step4, step5, step15 int) func(z, in int) int {
	return func(z, in int) int {
		x := z%26 + step5 //
		z = z / step4     // 1 or 26

		if x == in {
			return z
		} else {
			return z*26 + (in + step15)
		}
	}
}

func backtrace(pos, target int, prog []func(z, in int) int, nums []int) {
	if pos == -1 {
		fmt.Println("solution", nums)
	}

	fn := prog[pos]
	for in := 1; in < 10; in++ {
		for z := 0; z < 300; z++ {
			res := fn(z, in)

			if res == target {
				backtrace(pos-1, z, prog, append(nums, in))
			}
		}
	}
}

func main() {
	dat, _ := os.ReadFile(file)
	lines := strings.Split(string(dat), "\n")
	instr := make([]*Instruction, len(lines))
	for idx, line := range lines {
		instr[idx] = readLine(line)
	}

	prog := make([]func(z, in int) int, 14)
	fmt.Printf(" a4  a5 a15\n")

	for i := 0; i < 14; i++ {

		program := instr[i*18 : (i+1)*18]
		step4, _ := strconv.Atoi(program[4].arg2)
		step5, _ := strconv.Atoi(program[5].arg2)
		step15, _ := strconv.Atoi(program[15].arg2)
		fmt.Printf("%3d %3d %3d\n", step4, step5, step15)
		prog[i] = createFunc(step4, step5, step15)

	}

	backtrace(13, 0, prog, nil)

	input := []int{1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9}
	z := 0
	for idx, sym := range prog {
		z = sym(z, input[idx])
		fmt.Println(z)
	}

	// for progIdx := 13; progIdx >= 13; progIdx-- {
	// 	fn := prog[progIdx]
	// 	for in := 1; in < 10; in++ {
	// 		for z := 0; z < 26; z++ {
	// 			res := fn(z, in)

	// 			if res == 0 {
	// 				fmt.Println("Z:", z, "IN:", in)
	// 			}
	// 		}
	// 	}
	// }

	// for in := 1; in < 10; in++ {
	// 	z := prog[0](0, in)

	// 	// if res == 0 {
	// 	fmt.Println("Z:", z, "IN:", in)
	// 	// }
	// }

	// fmt.Println(memory)

}
