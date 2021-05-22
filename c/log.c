
#include <stdio.h>
#include <stdbool.h>
#include <stdarg.h>

#include "colours.h"

#include "log.h"

// ===================== CONSTANTS ===================== //

#define ERROR_COLOUR     RED
#define WARNING_COLOUR   YELLOW
#define SUCCESS_COLOUR   GREEN
#define DEBUG_COLOUR     BLUE
#define INFO_COLOUR      CYAN
#define NOTE_COLOUR      MAGENTA

#define ERROR_PREFIX     "X"
#define WARNING_PREFIX   "!"
#define SUCCESS_PREFIX   "~"
#define DEBUG_PREFIX     "#"
#define INFO_PREFIX      ">"
#define NOTE_PREFIX      "@"

static char const * PREFIXES [NUM_LOG_LEVELS] = {
	ERROR_PREFIX,
	WARNING_PREFIX,
	SUCCESS_PREFIX,
	DEBUG_PREFIX,
	INFO_PREFIX,
	NOTE_PREFIX
};

static char const * COLOURS [NUM_LOG_LEVELS] = {
	ERROR_COLOUR,
	WARNING_COLOUR,
	SUCCESS_COLOUR,
	DEBUG_COLOUR,
	INFO_COLOUR,
	NOTE_COLOUR
};

// ===================== FLAGS ===================== //

static bool SUPPRESSED [NUM_LOG_LEVELS] = {
	false,
	false,
	false,
	false,
	false,
	false
};

static bool TRACE_FILE = false;
static bool TRACE_LINE = false;
static bool TRACE_CALLER = false;

static bool ENABLE_LOGS = true;
static bool ENABLE_TRACE = false;
static bool ENABLE_COLOUR = true;

// ===================== LOGGING API ===================== //

void log_enable(void)
{
	ENABLE_LOGS = true;
}

void log_disable(void)
{
	ENABLE_LOGS = false;
}

void log_suppress(LogLevel level)
{
	if (level < NUM_LOG_LEVELS)
	{
		SUPPRESSED[level] = true;
	}
}

void log_show(LogLevel level)
{
	if (level < NUM_LOG_LEVELS)
	{
		SUPPRESSED[level] = false;
	}
}

void log_colourize(void)
{
	ENABLE_COLOUR = true;
}

void log_colourless(void)
{
	ENABLE_COLOUR = false;
}

void log_trace(bool file, bool line, bool caller)
{
	TRACE_FILE = file;
	TRACE_LINE = line;
	TRACE_CALLER = caller;

	ENABLE_TRACE = file || line || caller;
}

void log_print(char const * file, int line, char const * caller, LogLevel level, char const * format, ...)
{
	if (format == NULL || caller == NULL || file == NULL || level >= NUM_LOG_LEVELS)
	{
		return;
	}

	if (SUPPRESSED[level] || !ENABLE_LOGS)
	{
		return;
	}

	if (ENABLE_TRACE)
	{
		if (TRACE_FILE)
		{
			printf("%s:", file);
		}

		if (TRACE_LINE)
		{
			printf("%d:", line);
		}

		if (TRACE_CALLER)
		{
			printf("%s:", caller);
		}

		printf(" ");
	}

	if (ENABLE_COLOUR)
	{
		printf("%s", COLOURS[level]);
	}

	printf("%s" RESET " ", PREFIXES[level]);

	va_list args;
    va_start(args, format);
	vprintf(format, args);
    va_end(args);

	printf("\r\n");
}
