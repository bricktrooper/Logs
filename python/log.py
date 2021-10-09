import colours
import inspect

from enum import Enum

# ===================== LEVELS ===================== #

class Level(Enum):
	ERROR = 0
	WARNING = 1
	SUCCESS = 2
	DEBUG = 3
	INFO = 4
	NOTE = 5

# ===================== CONSTANTS ===================== #

COLOURS = {
	Level.ERROR:   colours.RED,
	Level.WARNING: colours.YELLOW,
	Level.SUCCESS: colours.GREEN,
	Level.DEBUG:   colours.BLUE,
	Level.INFO:    colours.CYAN,
	Level.NOTE:    colours.MAGENTA
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
	Level.ERROR:   "X",
	Level.WARNING: "!",
	Level.SUCCESS: "~",
	Level.DEBUG:   "#",
	Level.INFO:    ">",
	Level.NOTE:    "@"
}

# ===================== FLAGS ===================== #

SUPPRESSED = {
	Level.ERROR:   False,
	Level.WARNING: False,
	Level.SUCCESS: False,
	Level.DEBUG:   False,
	Level.INFO:    False,
	Level.NOTE:    False
}

class Trace(Enum):
	FILE = 0
	LINE = 1
	CALLER = 2

TRACE = {
	Trace.FILE:   False,
	Trace.LINE:   False,
	Trace.CALLER: False
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

	if TRACE[Trace.FILE]:
		file = str(stack[3][1]) + ":"
	if TRACE[Trace.LINE]:
		line = str(stack[3][2]) + ":"
	if TRACE[Trace.CALLER]:
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
	if level in Level:
		SUPPRESSED[level] = True
	else:
		__invalid(level)
		raise Exception("Invalid log level")

def show(level):
	if level in Level:
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
	TRACE[Trace.FILE] = file
	TRACE[Trace.LINE] = line
	TRACE[Trace.CALLER] = caller

	global ENABLE_TRACE
	if file or line or caller:
		ENABLE_TRACE = True
	else:
		ENABLE_TRACE = False

def error(message):
	print(__format(Level.ERROR, message), end = "")

def warning(message):
	print(__format(Level.WARNING, message), end = "")

def success(message):
	print(__format(Level.SUCCESS, message), end = "")

def debug(message):
	print(__format(Level.DEBUG, message), end = "")

def info(message):
	print(__format(Level.INFO, message), end = "")

def note(message):
	print(__format(Level.NOTE, message), end = "")
