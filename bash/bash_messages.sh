# ===================== TERMINAL MESSAGES ===================== #

print_error()
{
	echo -e "${RED}X ${RESET}${@}"
}

print_warning()
{
	echo -e "${YELLOW}! ${RESET}${@}"
}

print_success()
{
	echo -e "${GREEN}~ ${RESET}${@}"
}

print_debug()
{
	echo -e "${BLUE}# ${RESET}${@}"
}


print_info()
{
	echo -e "${PURPLE}> ${RESET}${@}"
}

print_note()
{
	echo -e "${PINK}@ ${RESET}${@}"
}

export -f print_error
export -f print_warning
export -f print_success
export -f print_debug
export -f print_info
export -f print_note
