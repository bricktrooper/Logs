# ===================== LOGGING ===================== #

import colours
import inspect

COLOURS = {
	"error":     colours.RED,
	"warning":   colours.YELLOW,
	"success":   colours.GREEN,
	"debug":     colours.BLUE,
	"info":      colours.CYAN,
	"note":      colours.MAGENTA,
	"reset":     colours.RESET,
	"trace":     colours.BLACK
}

PREFIXES = {
	"error":     "X",
	"warning":   "!",
	"success":   "~",
	"debug":     "#",
	"info":      ">",
	"note":      "@"
}

TRACE = {
	"file":     False,
	"line":     False,
	"caller":   False
}

def trace_file(enabled):
	TRACE["file"] = enabled

def trace_line(enabled):
	TRACE["line"] = enabled

def trace_caller(enabled):
	TRACE["caller"] = enabled

def enable():
	global DISABLED
	DISABLED = False

def disable():
	global DISABLED
	DISABLED = True

def format(message):
	if DISABLED:
		return ""

	stack_trace = inspect.stack()
	level = stack_trace[1][3]

	if TRACE["file"]:
		file = str(stack_trace[2][1]) + ":"
	else:
		file = ""

	if TRACE["line"]:
		line = str(stack_trace[2][2]) + ":"
	else:
		line = ""

	if TRACE["caller"]:
		caller = str(stack_trace[2][3]) + ":"
	else:
		caller = ""

	return "{}{}{} {}{}{} {}\r\n".format(file, line, caller, COLOURS[level], PREFIXES[level], COLOURS["reset"], str(message))

def error(message):
	print(format(message), end="")

def warning(message):
	print(format(message), end="")

def success(message):
	print(format(message), end="")

def debug(message):
	print(format(message), end="")

def info(message):
	print(format(message), end="")

def note(message):
	print(format(message), end="")
