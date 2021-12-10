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

#define __log_print(colour, prefix, message)   do { printf(colour "%s " RESET, prefix); printf(message); printf("\r\n"); } while (0)

#ifndef LOG_DISABLE
#define log_error(...)     __log_print(RED, "X", __VA_ARGS__)
#define log_warning(...)   __log_print(YELLOW, "!", __VA_ARGS__)
#define log_success(...)   __log_print(GREEN, "~", __VA_ARGS__)
#define log_debug(...)     __log_print(CYAN, "#", __VA_ARGS__)
#define log_info(...)      __log_print(BLUE, ">", __VA_ARGS__)
#define log_note(...)      __log_print(MAGENTA, "@", __VA_ARGS__)
#else
#define log_error(...)
#define log_warning(...)
#define log_success(...)
#define log_debug(...)
#define log_info(...)
#define log_note(...)
#endif

#endif /* LOG_H */
