package log

import "os"

type LogLevel struct {
	Name       string
	Colour     Colour
	Prefix     string
	File       *os.File
	Suppressed bool
}

var LogLevelError = LogLevel{
	Name:       "ERROR",
	Colour:     ColourRed,
	Prefix:     "X",
	File:       os.Stderr,
	Suppressed: false,
}

var LogLevelWarning = LogLevel{
	Name:       "WARNING",
	Colour:     ColourYellow,
	Prefix:     "!",
	File:       os.Stdout,
	Suppressed: false,
}

var LogLevelSuccess = LogLevel{
	Name:       "SUCCESS",
	Colour:     ColourGreen,
	Prefix:     "~",
	File:       os.Stdout,
	Suppressed: false,
}

var LogLevelDebug = LogLevel{
	Name:       "DEBUG",
	Colour:     ColourCyan,
	Prefix:     "#",
	File:       os.Stdout,
	Suppressed: false,
}

var LogLevelInfo = LogLevel{
	Name:       "INFO",
	Colour:     ColourBlue,
	Prefix:     ">",
	File:       os.Stdout,
	Suppressed: false,
}

var LogLevelNote = LogLevel{
	Name:       "NOTE",
	Colour:     ColourMagenta,
	Prefix:     "@",
	File:       os.Stdout,
	Suppressed: false,
}

var ENABLE_LOGGING = true
var ENABLE_COLOUR = true
var ENABLE_TRACE = false
var TIME_FORMAT = "2006-01-02 3:4:5 PM"

func Enable() {
	ENABLE_LOGGING = true
}

func Disable() {
	ENABLE_LOGGING = false
}

func Colourize() {
	ENABLE_COLOUR = true
}

func Colourless() {
	ENABLE_COLOUR = false
}

func Traceful() {
	ENABLE_TRACE = true
}

func Traceless() {
	ENABLE_TRACE = false
}

func (level *LogLevel) Suppress() {
	level.Suppressed = true
}

func (level *LogLevel) Show() {
	level.Suppressed = false
}

func SetTimeFormat(format string) {
	TIME_FORMAT = format
}
