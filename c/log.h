#ifndef LOG_H
#define LOG_H

#include <stdio.h>

#define BLACK     "\033[0;30m"
#define RED       "\033[0;31m"
#define GREEN     "\033[0;32m"
#define YELLOW    "\033[0;33m"
#define BLUE      "\033[0;34m"
#define MAGENTA   "\033[0;35m"
#define CYAN      "\033[0;36m"
#define WHITE     "\033[0;37m"
#define RESET     "\033[0m"

#define NEWLINE "\r\n"

#define __log_print(format, ...)   printf(format, ##__VA_ARGS__)

#define COMPILE_LOGS   // comment out this line exclude logs from compilation

#ifdef COMPILE_LOGS
#define log_error(format, ...)     __log_print(RED     "X " RESET format NEWLINE, ##__VA_ARGS__)
#define log_warning(format, ...)   __log_print(YELLOW  "! " RESET format NEWLINE, ##__VA_ARGS__)
#define log_success(format, ...)   __log_print(GREEN   "~ " RESET format NEWLINE, ##__VA_ARGS__)
#define log_debug(format, ...)     __log_print(CYAN    "# " RESET format NEWLINE, ##__VA_ARGS__)
#define log_info(format, ...)      __log_print(BLUE    "> " RESET format NEWLINE, ##__VA_ARGS__)
#define log_note(format, ...)      __log_print(MAGENTA "@ " RESET format NEWLINE, ##__VA_ARGS__)
#else
#define log_error(...)
#define log_warning(...)
#define log_success(...)
#define log_debug(...)
#define log_info(...)
#define log_note(...)
#endif

#endif /* LOG_H */
