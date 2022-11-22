
#include <stdio.h>
#include <stdbool.h>
#include <stdarg.h>

#include "colours.h"

#include "log.h"

// ===================== CONSTANTS ===================== //

#define NEWLINE   "\r\n"

#define COLOUR_ERROR     RED
#define COLOUR_WARNING   YELLOW
#define COLOUR_SUCCESS   GREEN
#define COLOUR_DEBUG     CYAN
#define COLOUR_INFO      BLUE
#define COLOUR_NOTE      MAGENTA

#define PREFIX_ERROR     "X"
#define PREFIX_WARNING   "!"
#define PREFIX_SUCCESS   "~"
#define PREFIX_DEBUG     "#"
#define PREFIX_INFO      ">"
#define PREFIX_NOTE      "@"

static char const * prefixes [NUM_LOG_LEVELS] = {
	PREFIX_ERROR,
	PREFIX_WARNING,
	PREFIX_SUCCESS,
	PREFIX_DEBUG,
	PREFIX_INFO,
	PREFIX_NOTE
};

static char const * colours [NUM_LOG_LEVELS] = {
	COLOUR_ERROR,
	COLOUR_WARNING,
	COLOUR_SUCCESS,
	COLOUR_DEBUG,
	COLOUR_INFO,
	COLOUR_NOTE
};

// ===================== FLAGS ===================== //

static bool suppressed [NUM_LOG_LEVELS] = {
	false,
	false,
	false,
	false,
	false,
	false
};

static bool trace_file = false;
static bool trace_line = false;
static bool trace_caller = false;

static bool enable = true;
static bool trace = false;
static bool colourize = true;

// ===================== LOGGING API ===================== //

void log_enable(void)
{
	enable = true;
}

void log_disable(void)
{
	enable = false;
}

void log_suppress(Log_Level level)
{
	if (level < NUM_LOG_LEVELS)
	{
		suppressed[level] = true;
	}
}

void log_show(Log_Level level)
{
	if (level < NUM_LOG_LEVELS)
	{
		suppressed[level] = false;
	}
}

void log_colourize(void)
{
	colourize = true;
}

void log_colourless(void)
{
	colourize = false;
}

void log_trace(bool file, bool line, bool caller)
{
	trace_file = file;
	trace_line = line;
	trace_caller = caller;

	trace = file || line || caller;
}

void log_print(char const * file, int line, char const * caller, Log_Level level, char const * format, ...)
{
	if (format == NULL || caller == NULL || file == NULL || level >= NUM_LOG_LEVELS)
	{
		return;
	}

	if (suppressed[level] || !enable)
	{
		return;
	}

	if (colourize)
	{
		printf("%s", colours[level]);
	}

	printf("%s " RESET, prefixes[level]);

	if (trace)
	{
		if (trace_file)
		{
			printf("%s:", file);
		}

		if (trace_line)
		{
			printf("%d:", line);
		}

		if (trace_caller)
		{
			printf("%s:", caller);
		}

		printf(" ");
	}

	va_list args;
	va_start(args, format);
	vprintf(format, args);
	va_end(args);

	printf(NEWLINE);
}
