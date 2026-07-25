//go:build demo

package dummy

import "testing"

func TestMultiply(t *testing.T) {
	if Multiply(2, 3) != 6 {
		t.Fatal("unexpected result")
	}
}
