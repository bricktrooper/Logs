source colours.sh

# true and false are reversed in Bash
FALSE=1
TRUE=0

# ===================== CONSTANTS ===================== #

ERROR_COLOUR=${RED}
WARNING_COLOUR=${YELLOW}
SUCCESS_COLOUR=${GREEN}
DEBUG_COLOUR=${BLUE}
INFO_COLOUR=${CYAN}
NOTE_COLOUR=${MAGENTA}

ERROR_PREFIX="X"
WARNING_PREFIX="!"
SUCCESS_PREFIX="~"
DEBUG_PREFIX="#"
INFO_PREFIX=">"
NOTE_PREFIX="@"

# ===================== FLAGS ===================== #

SUPPRESS_ERROR=$FALSE
SUPPRESS_WARNING=$FALSE
SUPPRESS_SUCCESS=$FALSE
SUPPRESS_DEBUG=$FALSE
SUPPRESS_INFO=$FALSE
SUPPRESS_NOTE=$FALSE

suppressed()
{
	local FLAG=SUPPRESS_${1}
	return ${!FLAG}
}

TRACE_FILE=$FALSE
TRACE_LINE=$FALSE
TRACE_CALLER=$FALSE

trace()
{
	local FLAG=TRACE_${1}
	return ${!FLAG}
}

ENABLE_LOGS=$TRUE
ENABLE_TRACE=$FALSE
ENABLE_COLOUR=$TRUE

enabled()
{
	local FLAG=ENABLE_${1}
	return ${!FLAG}
}

# ===================== INTERNAL FUNCTIONS ===================== #

get_trace()
{
	if ! enabled TRACE
	then
		return
	fi

	local STACK=`caller 2`
	local FILE
	local LINE
	local CALLER

	if trace FILE
	then
		FILE=`echo $STACK | cut -d " " -f 3-`
		FILE="${FILE}:"
	fi

	if trace LINE
	then
		LINE=`echo $STACK | cut -d " " -f 1`
		LINE="${LINE}:"
	fi

	if trace CALLER
	then
		local CALLER=`echo $STACK | cut -d " " -f 2`
		CALLER="${CALLER}:"
	fi

	echo "${FILE}${LINE}${CALLER} "
}

get_prefix()
{
	local LEVEL=${1}
	local COLOUR=${LEVEL}_COLOUR
	local PREFIX=${LEVEL}_PREFIX

	if enabled COLOUR
	then
		echo "${!COLOUR}${!PREFIX}${RESET} "
	else
		echo "${!PREFIX} "
	fi
}


format_message()
{
	local LEVEL=${1}
	local MESSAGE=${2}

	if suppressed $LEVEL || ! enabled LOGS
	then
		return
	else
		local TRACE=`get_trace`
		local PREFIX=`get_prefix ${LEVEL}`
		echo "${TRACE}${PREFIX}${MESSAGE}\r\n"
	fi
}

# ===================== LOGGING API ===================== #

log_enable()
{
	export ENABLE_LOGS=$TRUE
}

log_disable()
{
	export ENABLE_LOGS=$FALSE
}

log_suppress()
{
	local LEVEL=${1}
	export SUPPRESS_${LEVEL}=$TRUE
}

log_show()
{
	local LEVEL=${1}
	export SUPPRESS_${LEVEL}=$FALSE
}

log_colourize()
{
	export ENABLE_COLOUR=$TRUE
}

log_colourless()
{
	export ENABLE_COLOUR=$FALSE
}

log_trace()
{
	local FILE=${1}
	local LINE=${2}
	local CALLER=${3}

	if [[ "${FILE}" == "true" ]]
	then
		export TRACE_FILE=$TRUE
	else
		export TRACE_FILE=$FALSE
	fi

	if [[ "${LINE}" == "true" ]]
	then
		export TRACE_LINE=$TRUE
	else
		export TRACE_LINE=$FALSE
	fi

	if [[ "${CALLER}" == "true" ]]
	then
		export TRACE_CALLER=$TRUE
	else
		export TRACE_CALLER=$FALSE
	fi

	if trace FILE || trace LINE || trace CALLER
	then
		export ENABLE_TRACE=$TRUE
	else
		export ENABLE_TRACE=$FALSE
	fi
}

log_error()
{
	printf "`format_message ERROR ${@}`"
}

log_warning()
{
	printf "`format_message WARNING ${@}`"
}

log_success()
{
	printf "`format_message SUCCESS ${@}`"
}

log_debug()
{
	printf "`format_message DEBUG ${@}`"
}

log_info()
{
	printf "`format_message INFO ${@}`"
}

log_note()
{
	printf "`format_message NOTE ${@}`"
}

export -f log_error
export -f log_warning
export -f log_success
export -f log_debug
export -f log_info
export -f log_note
