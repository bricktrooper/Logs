# Logging API

### Usage

Messages can be printed on any of the following log levels:

```
Log.error(String format, Object ... args);
Log.warning(String format, Object ... args);
Log.success(String format, Object ... args);
Log.debug(String format, Object ... args);
Log.info(String format, Object ... args);
Log.note(String format, Object ... args);
```

Each log level has an associated `Log.Level` enum:

```
enum Log.Level
{
	ERROR,
	WARNING,
	SUCCESS,
	DEBUG,
	INFO,
	NOTE
}
```

Each log level has a prefix symbol with a unique ANSI colour.  If your terminal does not support colours, you can disable it:

```
Log.colourless();
Log.colourize();
```

Each log level can be individually suppressed:

```
Log.suppress(Level level);
Log.show(Level level);
```

All log printing can be disabled.  This overrides suppressions.  When enabled, suppressions still apply:

```
Log.enable();
Log.disable();
```

The file, line number, and calling function of log prints can be traced.
By default, tracing is disabled.  It can be enabled using the boolean arguments of the following function:

```
Log.trace(boolean file, boolean line, boolean caller);
```

### Example

The following example can be found in `Demo.java`

#### Code

```
class Demo
{
	public static void test()
	{
		Log.error("ERROR");
		Log.warning("WARNING");
		Log.success("SUCCESS");
	}

	public static void main(String [] args)
	{
		Log.trace(false, false, true);

		test();
		Log.info("INFO");
		Log.debug("DEBUG");
		Log.note("NOTE");
	}
}
```

#### Output

```
test: X ERROR
test: ! WARNING
test: ~ SUCCESS
main: > INFO
main: # DEBUG
main: @ NOTE
```
