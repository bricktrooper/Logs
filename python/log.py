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

LEVELS = {
	"error",
	"warning",
	"success",
	"debug",
	"info",
	"note"
}

PREFIXES = {
	"error":     "X",
	"warning":   "!",
	"success":   "~",
	"debug":     "#",
	"info":      ">",
	"note":      "@"
}

SUPPRESSED = {
	"error":     False,
	"warning":   False,
	"success":   False,
	"debug":     False,
	"info":      False,
	"note":      False
}

TRACE = {
	"file":     False,
	"line":     False,
	"caller":   False
}

DISABLED = False
NO_TRACE = True

def __trace():
	if NO_TRACE:
		return ""

	file = ""
	line = ""
	caller = ""

	stack_trace = inspect.stack()

	if TRACE["file"]:
		file = str(stack_trace[3][1]) + ":"

	if TRACE["line"]:
		line = str(stack_trace[3][2]) + ":"

	if TRACE["caller"]:
		caller = str(stack_trace[3][3]) + ":"

	return "{}{}{}".format(file, line, caller)

def __prefix(level):
	return "{}{}{}".format(COLOURS[level], PREFIXES[level], COLOURS["reset"])

def __format(level, message):
	if DISABLED or SUPPRESSED[level]:
		return ""
	else:
		return "{} {} {}\r\n".format(__trace(), __prefix(level), str(message))

def enable():
	global DISABLED
	DISABLED = False

def disable():
	global DISABLED
	DISABLED = True

def suppress(level):
	if level in LEVELS:
		SUPPRESSED[level] = True

def unsuppress(level):
	if level in LEVELS:
		SUPPRESSED[level] = False

def trace(file, line, caller):
	TRACE["file"] = file
	TRACE["line"] = line
	TRACE["caller"] = caller

	global NO_TRACE

	if not file and not line and not caller:
		NO_TRACE = True
	else:
		NO_TRACE = False

def error(message):
	print(__format("error", message), end="")

def warning(message):
	print(__format("warning", message), end="")

def success(message):
	print(__format("success", message), end="")

def debug(message):
	print(__format("debug", message), end="")

def info(message):
	print(__format("info", message), end="")

def note(message):
	print(__format("note", message), end="")
