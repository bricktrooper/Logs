import colours
import inspect

# ===================== CONSTANTS ===================== #

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

DISABLE_LOGS = False
DISABLE_TRACE = True
DISABLE_COLOUR = False

# ===================== INTERNAL FUNCTIONS ===================== #

def __trace():
	if DISABLE_TRACE:
		return ""

	stack_trace = inspect.stack()
	file = ""
	line = ""
	caller = ""

	if TRACE["file"]:
		file = str(stack_trace[3][1]) + ":"
	if TRACE["line"]:
		line = str(stack_trace[3][2]) + ":"
	if TRACE["caller"]:
		caller = str(stack_trace[3][3])
		if caller == "<module>":
			caller = "__main__"
		caller += ":"

	return "{}{}{}".format(file, line, caller)

def __prefix(level):
	if DISABLE_COLOUR:
		return PREFIXES[level]
	else:
		return "{}{}{}".format(COLOURS[level], PREFIXES[level], COLOURS["reset"])

def __format(level, message):
	if DISABLE_LOGS or SUPPRESSED[level]:
		return ""
	else:
		return "{} {} {}\r\n".format(__trace(), __prefix(level), str(message))

def __invalid_level(level):
	print("'{}' is an invalid log level".format(level))
	print("Valid log levels: {}".format(LEVELS))

# ===================== LOGGING API ===================== #

def enable():
	global DISABLE_LOGS
	DISABLE_LOGS = False

def disable():
	global DISABLE_LOGS
	DISABLE_LOGS = True

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
	global DISABLE_COLOUR
	DISABLE_COLOUR = False

def colourless():
	global DISABLE_COLOUR
	DISABLE_COLOUR = True

def trace(file, line, caller):
	TRACE["file"] = file
	TRACE["line"] = line
	TRACE["caller"] = caller

	global DISABLE_TRACE
	if not file and not line and not caller:
		DISABLE_TRACE = True
	else:
		DISABLE_TRACE = False

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
