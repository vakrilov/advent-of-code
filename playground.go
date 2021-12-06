package main

import "fmt"

func main() {
	arr := [7]int{0, 1, 2, 3, 4, 5, 6}
	slice := arr[0:3]

	for i := 0; i < 10; i++ {
		slice = append(slice, i+100)
		slice[0]++

		if slice[0] == arr[0] {
			fmt.Println("Slice and array point to the same memory")
		} else {
			fmt.Println("...and now they don't")
		}
	}

	fmt.Println("DONE")
}
