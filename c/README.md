# Logging API

### Usage

Messages can be printed on any of the following log levels:

```
void log_error(char const * format, ...);
void log_warning(char const * format, ...);
void log_success(char const * format, ...);
void log_debug(char const * format, ...);
void log_info(char const * format, ...);
void log_verbose(char const * format, ...);
```

Each log level has an associated `Log_Level` enum:

```
enum Log_Level
{
	LOG_ERROR,
	LOG_WARNING,
	LOG_SUCCESS,
	LOG_DEBUG,
	LOG_INFO,
	LOG_VERBOSE
};
```

Each log level has a prefix symbol with a unique ANSI colour.  If your terminal does not support colours, you can disable it:

```
void log_colourless(void);
void log_colourize(void);
```

Each log level can be individually suppressed:

```
void log_suppress(Log_Level level);
void log_show(Log_Level level);
```

All log printing can be disabled.  This overrides suppressions.  When enabled, suppressions still apply:

```
void log_enable(void);
void log_disable(void);
```

The logs can also be completely removed from the code compilation for better efficiency via the flag in `log.h`

```
#define COMPILE_LOGS     true   // set to false to exclude logs from compilation
```

The file, line number, and calling function of log prints can be traced.
By default, tracing is disabled.  It can be enabled using the boolean arguments of the following function:

```
void log_trace(bool file, bool line, bool caller);
```

### Example

The following example can be found in `demo.c`

#### Code

```
#include "log.h"

void test(void)
{
	log_error("ERROR");
	log_warning("WARNING");
	log_success("SUCCESS");
}

int main(void)
{
	log_trace(false, false, true);

	test();
	log_info("INFO");
	log_debug("DEBUG");

	log_suppress(LOG_ERROR);
	log_error("ERROR");
	log_verbose("VERBOSE");
}
```

#### Output

```
X test: ERROR
! test: WARNING
~ test: SUCCESS
> main: INFO
# main: DEBUG
@ main: VERBOSE
```
