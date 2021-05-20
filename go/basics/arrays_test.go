package basics

import(
	"testing"
)

func TestStruct(t *testing.T) {

	a := foo{bar: make([]int, 0, 0)}

	a.bar = append(a.bar, 1)

	if a.bar[0] != 1 {
		t.Errorf("bad initial value")
	}
}
