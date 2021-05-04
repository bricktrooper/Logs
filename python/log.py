# ===================== LOGGING ===================== #

import colours

COLOURS = {
	"error":     colours.RED,
	"warning":   colours.YELLOW,
	"success":   colours.GREEN,
	"debug":     colours.BLUE,
	"info":      colours.CYAN,
	"note":      colours.MAGENTA,
	"reset":     colours.RESET
}

PREFIXES = {
	"error":     "X",
	"warning":   "!",
	"success":   "~",
	"debug":     "#",
	"info":      ">",
	"note":      "@"
}

def format(level, message):
	return COLOURS[level] + PREFIXES[level] + " " + COLOURS["reset"] + str(message)

def error(message):
	print(format("error", message))

def warning(message):
	print(format("warning", message))

def success(message):
	print(format("success", message))

def debug(message):
	print(format("debug", message))

def info(message):
	print(format("info", message))

def note(message):
	print(format("note", message))
