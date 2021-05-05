#ifndef LOG_H
#define LOG_H

#include <stdbool.h>

#define COMPILE_LOGS     true   // set to false to exclude logs from compilation

#if COMPILE_LOGS
#define log_error(...)     log_print(__FILE__, __LINE__, __func__, LOG_ERROR, __VA_ARGS__)
#define log_warning(...)   log_print(__FILE__, __LINE__, __func__, LOG_WARNING, __VA_ARGS__)
#define log_success(...)   log_print(__FILE__, __LINE__, __func__, LOG_SUCCESS, __VA_ARGS__)
#define log_debug(...)     log_print(__FILE__, __LINE__, __func__, LOG_DEBUG, __VA_ARGS__)
#define log_info(...)      log_print(__FILE__, __LINE__, __func__, LOG_INFO, __VA_ARGS__)
#define log_note(...)      log_print(__FILE__, __LINE__, __func__, LOG_NOTE, __VA_ARGS__)
#else
#define log_error(...)
#define log_warning(...)
#define log_success(...)
#define log_debug(...)
#define log_info(...)
#define log_note(...)
#endif

enum LogLevel
{
	LOG_ERROR,
	LOG_WARNING,
	LOG_SUCCESS,
	LOG_DEBUG,
	LOG_INFO,
	LOG_NOTE,

	NUM_LOG_LEVELS
};

typedef enum LogLevel LogLevel;

void log_enable(void);
void log_disable(void);
void log_suppress(LogLevel level);
void log_show(LogLevel level);
void log_colourize(void);
void log_colourless(void);
void log_trace(bool file, bool line, bool caller);
void log_print(char const * file, int line, char const * function, LogLevel level, char const * format, ...) __attribute__ ((format (printf, 5, 6)));

#endif /* LOG_H */
