RED     = "\033[0;31m"
GREEN   = "\033[0;32m"
YELLOW  = "\033[0;33m"
BLUE    = "\033[0;34m"
MAGENTA = "\033[0;35m"
CYAN    = "\033[0;36m"
RESET   = "\033[0m"

def error(message):
	print("{}{}{} {}".format(RED, "X", RESET, str(message)))

def warning(message):
	print("{}{}{} {}".format(YELLOW, "!", RESET, str(message)))

def success(message):
	print("{}{}{} {}".format(GREEN, "~", RESET, str(message)))

def debug(message):
	print("{}{}{} {}".format(CYAN, "#", RESET, str(message)))

def info(message):
	print("{}{}{} {}".format(BLUE, ">", RESET, str(message)))

def note(message):
	print("{}{}{} {}".format(MAGENTA, "@", RESET, str(message)))
