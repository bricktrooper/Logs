# Logging API

### Usage

Messages can be printed on any of the following log levels:

```
error(message)
warning(message)
success(message)
debug(message)
info(message)
note(message)
```

Each log level has an associated `str`:

```
"error"
"warning"
"success"
"debug"
"info"
"note"
```

Each log level has a prefix symbol with a unique ANSI colour.  If your terminal does not support colours, you can disable it:

```
colourless()
colourize()
```

Each log level can be individually suppressed:

```
suppress(level)
show(level)
```

All log printing can be disabled.  This overrides suppressions.  When enabled, suppressions still apply:

```
enable()
disable()
```

The file, line number, and calling function of log prints can be traced.
By default, tracing is disabled.  It can be enabled using the boolean arguments of the following function:

```
trace(file, line, caller)
```

### Example

The following example can be found in `demo.py`

#### Code

```
import log

log.trace(file = False, line = False, caller = True)

def test():
	log.error("ERROR")
	log.warning("WARNING")
	log.success("SUCCESS")

test()
log.info("INFO")
log.debug("DEBUG")
log.note("NOTE")
```

#### Output

```
test: X ERROR
test: ! WARNING
test: ~ SUCCESS
__main__: > INFO
__main__: # DEBUG
__main__: @ NOTE
```
