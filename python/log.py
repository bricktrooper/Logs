import colours
import inspect

# ===================== CONSTANTS ===================== #

COLOURS = {
	"ERROR":   colours.RED,
	"WARNING": colours.YELLOW,
	"SUCCESS": colours.GREEN,
	"DEBUG":   colours.BLUE,
	"INFO":    colours.CYAN,
	"NOTE":    colours.MAGENTA
}

LEVELS = {
	"ERROR",
	"WARNING",
	"SUCCESS",
	"DEBUG",
	"INFO",
	"NOTE"
}

PREFIXES = {
	"ERROR":   "X",
	"WARNING": "!",
	"SUCCESS": "~",
	"DEBUG":   "#",
	"INFO":    ">",
	"NOTE":    "@"
}

# ===================== FLAGS ===================== #

SUPPRESSED = {
	"ERROR":   False,
	"WARNING": False,
	"SUCCESS": False,
	"DEBUG":   False,
	"INFO":    False,
	"NOTE":    False
}

TRACE = {
	"FILE":   False,
	"LINE":   False,
	"CALLER": False
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

	if TRACE["FILE"]:
		file = str(stack[3][1]) + ":"
	if TRACE["LINE"]:
		line = str(stack[3][2]) + ":"
	if TRACE["CALLER"]:
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
		return "{}{}{}\r\n".format(__prefix(level), __trace(), str(message))

def __invalid(level):
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
		__invalid(level)
		raise Exception("Invalid log level")

def show(level):
	if level in LEVELS:
		SUPPRESSED[level] = False
	else:
		__invalid(level)
		raise Exception("Invalid log level")

def colourize():
	global ENABLE_COLOUR
	ENABLE_COLOUR = True

def colourless():
	global ENABLE_COLOUR
	ENABLE_COLOUR = False

def trace(file, line, caller):
	TRACE["FILE"] = file
	TRACE["LINE"] = line
	TRACE["CALLER"] = caller

	global ENABLE_TRACE
	if file or line or caller:
		ENABLE_TRACE = True
	else:
		ENABLE_TRACE = False

def error(message):
	print(__format("ERROR", message), end = "")

def warning(message):
	print(__format("WARNING", message), end = "")

def success(message):
	print(__format("SUCCESS", message), end = "")

def debug(message):
	print(__format("DEBUG", message), end = "")

def info(message):
	print(__format("INFO", message), end = "")

def note(message):
	print(__format("NOTE", message), end = "")
