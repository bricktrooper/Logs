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

Each log level has an associated enum:

```
log.Level.ERROR
log.Level.WARNING
log.Level.SUCCESS
log.Level.DEBUG
log.Level.INFO
log.Level.NOTE
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

The file, line number, calling function, and module of log prints can be traced.
By default, tracing is disabled.  It can be enabled using the boolean arguments of the following function:

```
trace(module, file, line, caller)
```

### Example

The following example can be found in `demo.py`

#### Code

```
import log

log.trace(file = False, line = False, caller = True, module = True)

def test():
	log.error("ERROR")
	log.warning("WARNING")
	log.success("SUCCESS")

test()
log.info("INFO")
log.debug("DEBUG")

log.suppress(log.Level.ERROR)
log.error("ERROR")
log.note("NOTE")
```

#### Output

```
X test:[log.log] ERROR
! test:[log.log] WARNING
~ test:[log.log] SUCCESS
> __main__:[log.log] INFO
# __main__:[log.log] DEBUG
@ __main__:[log.log] NOTE
```
