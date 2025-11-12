// https://www.codewars.com/kata/5264d2b162488dc400000001

package kata

import (
	"fmt"
	"strings"
)

func Reverse(s string) (result string) {
	for _, v := range s {
		result = string(v) + result
	}
	return
}

func SpinWords(str string) string {
	output := []string{}

	split := strings.Split(str, " ")
	for _, word := range split {
		fmt.Println(word)
		if len(word) > 4 {
			output = append(output, Reverse(word))
		} else {
			output = append(output, word)
		}
	}
	return strings.Join(output, " ")
}
