package log

import (
	"fmt"
	"strings"
)

type Colour string

const (
	ColourBlack   Colour = "\033[0;30m"
	ColourRed     Colour = "\033[0;31m"
	ColourGreen   Colour = "\033[0;32m"
	ColourYellow  Colour = "\033[0;33m"
	ColourBlue    Colour = "\033[0;34m"
	ColourMagenta Colour = "\033[0;35m"
	ColourCyan    Colour = "\033[0;36m"
	ColourWhite   Colour = "\033[0;37m"
	ColourReset   Colour = "\033[0m"
)

func (colour *Colour) WrapText(v ...interface{}) string {
	sliceStr := make([]string, len(v))
	for i := range v {
		sliceStr[i] = fmt.Sprint(v[i])
	}
	joinedStr := strings.Join(sliceStr, " ")

	if ENABLE_COLOUR {
		return fmt.Sprintf("%s%s%s", *colour, joinedStr, ColourReset)
	}

	return joinedStr
}
