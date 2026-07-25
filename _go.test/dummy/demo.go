//go:build demo

package dummy

// Multiply returns the product of a and b. Only built with the "demo" tag.
func Multiply(a, b int) int {
	return a * b
}
