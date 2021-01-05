package treeutil

type TreeNode struct {
	Left  *TreeNode
	Right *TreeNode
	Val   int
}

func InOrder(root *TreeNode) []int {
	var result []int
	var stack []*TreeNode

	for root != nil || len(stack) != 0 {
		for root != nil {
			stack = append(stack, root)
			root = root.Left
		}
		root = stack[len(stack)-1]
		stack = stack[0 : len(stack)-1]
		result = append(result, root.Val)
		root = root.Right
	}
	return result
}
