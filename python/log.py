from enum import Enum

RED     = "\033[0;31m"
GREEN   = "\033[0;32m"
YELLOW  = "\033[0;33m"
BLUE    = "\033[0;34m"
MAGENTA = "\033[0;35m"
CYAN    = "\033[0;36m"
RESET   = "\033[0m"

class Level(Enum):
	ERROR = 0
	WARNING = 1
	SUCCESS = 2
	DEBUG = 3
	INFO = 4
	NOTE = 5

SUPPRESSED = {
	Level.ERROR:   False,
	Level.WARNING: False,
	Level.SUCCESS: False,
	Level.DEBUG:   False,
	Level.INFO:    False,
	Level.NOTE:    False
}

def suppress(level):
	SUPPRESSED[level] = True

def show(level):
	SUPPRESSED[level] = False

def error(message):
	if not SUPPRESSED[Level.ERROR]:
		print(f"{RED}X{RESET} {message}")

def warning(message):
	if not SUPPRESSED[Level.WARNING]:
		print(f"{YELLOW}!{RESET} {message}")

def success(message):
	if not SUPPRESSED[Level.SUCCESS]:
		print(f"{GREEN}~{RESET} {message}")

def debug(message):
	if not SUPPRESSED[Level.DEBUG]:
		print(f"{CYAN}#{RESET} {message}")

def info(message):
	if not SUPPRESSED[Level.INFO]:
		print(f"{BLUE}>{RESET} {message}")

def note(message):
	if not SUPPRESSED[Level.NOTE]:
		print(f"{MAGENTA}@{RESET} {message}")
