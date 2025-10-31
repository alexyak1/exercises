package main

import (
	"fmt"
	"strconv"
	"strings"
	"sort"
)

func solve(s string) string {
	parts := strings.Split(s, "+")
	
	// Convert to slice of ints
	numberList := make([]int, len(parts))
	for i, p := range parts {
		n, _ := strconv.Atoi(p) // convert string to int
		numberList[i] = n
	}

	// -------------------------------------
	// Bubble Sort (your original algorithm)
	/*
	for i := 0; i < len(numberList); i++ {
		for j := 0; j < len(numberList)-i-1; j++ {
			if numberList[j] > numberList[j+1] {
				numberList[j], numberList[j+1] = numberList[j+1], numberList[j]
			}
		}
	}
	*/
	// -------------------------------------

	// Using Go's built-in sorting (preferred)
	sort.Ints(numberList)

	// Convert back to strings
	resultParts := make([]string, len(numberList))
	for i, n := range numberList {
		resultParts[i] = strconv.Itoa(n)
	}

	// Join with '+'
	return strings.Join(resultParts, "+")
}

func main() {
	input := "1+3+2+1"
	fmt.Println(solve(input)) // Output: 1+1+2+3
}
