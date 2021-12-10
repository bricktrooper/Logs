# Lite

This version of the API is a slimmed down version of the full implementation.  Only the following basic functions are supported:

```
void log_error(char const * format, ...);
void log_warning(char const * format, ...);
void log_success(char const * format, ...);
void log_debug(char const * format, ...);
void log_info(char const * format, ...);
void log_note(char const * format, ...);
```
