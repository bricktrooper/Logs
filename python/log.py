RED     = "\033[0;31m"
GREEN   = "\033[0;32m"
YELLOW  = "\033[0;33m"
BLUE    = "\033[0;34m"
MAGENTA = "\033[0;35m"
CYAN    = "\033[0;36m"
RESET   = "\033[0m"

def error(message):
	print(f"{RED}X{RESET} {message}")

def warning(message):
	print(f"{YELLOW}!{RESET} {message}")

def success(message):
	print(f"{GREEN}~{RESET} {message}")

def debug(message):
	print(f"{CYAN}#{RESET} {message}")

def info(message):
	print(f"{BLUE}>{RESET} {message}")

def note(message):
	print(f"{MAGENTA}@{RESET} {message}")
