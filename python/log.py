import colours
import inspect

# ===================== CONSTANTS ===================== #

COLOURS = {
	"error":     colours.RED,
	"warning":   colours.YELLOW,
	"success":   colours.GREEN,
	"debug":     colours.BLUE,
	"info":      colours.CYAN,
	"note":      colours.MAGENTA
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

# ===================== FLAGS ===================== #

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

ENABLE_LOGS = True
ENABLE_TRACE = False
ENABLE_COLOUR = True

# ===================== INTERNAL FUNCTIONS ===================== #

def __trace():
	if not ENABLE_TRACE:
		return ""

	stack = inspect.stack()
	file = ""
	line = ""
	caller = ""

	if TRACE["file"]:
		file = str(stack[3][1]) + ":"
	if TRACE["line"]:
		line = str(stack[3][2]) + ":"
	if TRACE["caller"]:
		caller = str(stack[3][3])
		if caller == "<module>":
			caller = "__main__"
		caller += ":"

	return "{}{}{} ".format(file, line, caller)

def __prefix(level):
	if ENABLE_COLOUR:
		return "{}{}{} ".format(COLOURS[level], PREFIXES[level], colours.RESET)
	else:
		return "{} ".format(PREFIXES[level])


def __format(level, message):
	if SUPPRESSED[level] or not ENABLE_LOGS:
		return ""
	else:
		return "{}{}{}\r\n".format(__trace(), __prefix(level), str(message))

def __invalid_level(level):
	print("'{}' is an invalid log level".format(level))
	print("Valid log levels: {}".format(LEVELS))

# ===================== LOGGING API ===================== #

def enable():
	global ENABLE_LOGS
	ENABLE_LOGS = True

def disable():
	global ENABLE_LOGS
	ENABLE_LOGS = False

def suppress(level):
	if level in LEVELS:
		SUPPRESSED[level] = True
	else:
		__invalid_level(level)
		raise "Invalid valid log level"

def show(level):
	if level in LEVELS:
		SUPPRESSED[level] = False
	else:
		__invalid_level(level)
		raise "Invalid valid log level"

def colourize():
	global ENABLE_COLOUR
	ENABLE_COLOUR = True

def colourless():
	global ENABLE_COLOUR
	ENABLE_COLOUR = False

def trace(file, line, caller):
	TRACE["file"] = file
	TRACE["line"] = line
	TRACE["caller"] = caller

	global ENABLE_TRACE
	if file or line or caller:
		ENABLE_TRACE = True
	else:
		ENABLE_TRACE = False

def error(message):
	print(__format("error", message), end = "")

def warning(message):
	print(__format("warning", message), end = "")

def success(message):
	print(__format("success", message), end = "")

def debug(message):
	print(__format("debug", message), end = "")

def info(message):
	print(__format("info", message), end = "")

def note(message):
	print(__format("note", message), end = "")
