package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var s = [][]int{
		{0, 6, 0},
		{5, 8, 7},
		{0, 9, 0},
	}

	fmt.Println(getMaximumGold(s))
}

func subsets(nums []int) [][]int {
	var (
		result    [][]int
		trackback func(int, []int)
	)

	trackback = func(i int, s []int) {
		result = append(result, s)
		for j := i; j < len(nums); j++ {
			s = append(s, nums[j])
			trackback(j+1, s)
			s = s[:len(s)-1]
		}
	}
	trackback(0, nil)
	return result
}

func restoreIpAddresses(s string) []string {
	var k = len(s)
	if k < 4 || k > 12 {
		return nil
	}

	var i = 0
	var result []string
	var backtrace func(int, []string)

	backtrace = func(i int, t []string) {
		if i == 3 {
			// if len(t)
			x, _ := strconv.Atoi(string(s[3:]))
			if x > 255 {
				return
			}
			t = append(t, string(s[3:]))
			result = append(result, strings.Join(t, "."))
			return
		}
		for j := i; j < len(s); j++ {
			v := string(s[j])
			if v == "0" {
				continue
			}
			t = append(t, v)
			backtrace(i+1, t)
			t = t[:len(t)-1]
			backtrace(i+1, t)
			// fmt.Println(t, "wwww")
		}
	}
	backtrace(i, nil)
	return result
}

func getMaximumGold(grid [][]int) int {
	var (
		row = len(grid)
		col = len(grid[0])
	)

	var result int
	var trackback func(x, y int, grid *[][]int) int

	trackback = func(x, y int, grid *[][]int) int {
		if x < 0 || y < 0 || x >= row || y >= col || (*grid)[x][y] == 0 {
			return 0
		}
		t := (*grid)[x][y]
		(*grid)[x][y] = 0
		var (
			up    = trackback(x-1, y, grid)
			down  = trackback(x+1, y, grid)
			left  = trackback(x, y-1, grid)
			right = trackback(x, y+1, grid)
		)
		r := max(right, max(left, max(up, down)))
		(*grid)[x][y] = t
		return r + t
	}

	for i := 0; i < row; i++ {
		for j := 0; j < col; j++ {
			result = max(trackback(i, j, &grid), result)
		}
	}

	return result
}

func max(x, y int) int {
	if x >= y {
		return x
	}
	return y
}
