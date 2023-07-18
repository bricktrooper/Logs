import java.util.Arrays;
import java.lang.StackTraceElement;

// ===================== CONSTANTS ===================== //

class Log
{
	private static final String COLOUR_ERROR   = Colours.RED;
	private static final String COLOUR_WARNING = Colours.YELLOW;
	private static final String COLOUR_SUCCESS = Colours.GREEN;
	private static final String COLOUR_DEBUG   = Colours.CYAN;
	private static final String COLOUR_INFO    = Colours.BLUE;
	private static final String COLOUR_VERBOSE = Colours.MAGENTA;
	private static final String COLOUR_TRACE   = Colours.BLACK;

	private static final String PREFIX_ERROR   = "X";
	private static final String PREFIX_WARNING = "!";
	private static final String PREFIX_SUCCESS = "~";
	private static final String PREFIX_DEBUG   = "#";
	private static final String PREFIX_INFO    = ">";
	private static final String PREFIX_VERBOSE = "@";

	private static final String [] PREFIXES = {
		PREFIX_ERROR,
		PREFIX_WARNING,
		PREFIX_SUCCESS,
		PREFIX_DEBUG,
		PREFIX_INFO,
		PREFIX_VERBOSE
	};

	private static final String [] COLOURS = {
		COLOUR_ERROR,
		COLOUR_WARNING,
		COLOUR_SUCCESS,
		COLOUR_DEBUG,
		COLOUR_INFO,
		COLOUR_VERBOSE
	};

	public enum Level
	{
		ERROR,
		WARNING,
		SUCCESS,
		DEBUG,
		INFO,
		VERBOSE,

		NUM_LEVELS
	};

	private static final String [] LEVEL_NAMES = {
		"ERROR",
		"WARNING",
		"SUCCESS",
		"DEBUG",
		"INFO",
		"VERBOSE"
	};

	// ===================== FLAGS ===================== //

	private static boolean [] SUPPRESSED = {
		false,
		false,
		false,
		false,
		false,
		false
	};

	private static boolean traceFile = false;
	private static boolean traceLine = false;
	private static boolean traceCaller = false;

	private static boolean enableLogs = true;
	private static boolean enableTrace = false;
	private static boolean enableColour = true;

	// ===================== INTERNAL FUNCTIONS ===================== //

	private static String getTrace()
	{
		if (!enableTrace)
		{
			return "";
		}

		StackTraceElement [] stack = Thread.currentThread().getStackTrace();

		String file = "";
		String line = "";
		String caller = "";

		if (traceFile)
		{
			file = stack[4].getFileName() + ":";
		}

		if (traceLine)
		{
			line = stack[4].getLineNumber() + ":";
		}

		if (traceCaller)
		{
			caller = stack[4].getMethodName() + ":";
		}


		if (enableColour)
		{
			return String.format("%s%s%s%s%s ", COLOUR_TRACE, file, line, caller, Colours.RESET);
		}
		else
		{
			return String.format("%s%s%s ", file, line, caller);
		}

	}

	private static String getPrefix(Level level)
	{
		int index = level.ordinal();

		if (enableColour)
		{
			return String.format("%s%s%s ", COLOURS[index], PREFIXES[index], Colours.RESET);
		}
		else
		{
			return String.format("%s ", PREFIXES[index]);
		}
	}

	private static String formatMessage(Level level, String format, Object... args)
	{
		if (SUPPRESSED[level.ordinal()] || !enableLogs)
		{
			return "";
		}
		else
		{
			return String.format("%s%s%s\r\n", getPrefix(level), getTrace(), String.format(format, args));
		}
	}

	private static void printInvalidLogLevel(Level level)
	{
		System.out.printf("'%s' is an invalid log level\r\n", level);
		System.out.printf("Valid log levels: %s\r\n", Arrays.toString(LEVEL_NAMES));
	}

	// ===================== LOGGING API ===================== //

	public static void enable()
	{
		enableLogs = true;
	}

	public static void disable()
	{
		enableLogs = false;
	}

	public static void suppress(Level level)
	{
		if (level.ordinal() < Level.NUM_LEVELS.ordinal())
		{
			SUPPRESSED[level.ordinal()] = true;
		}
		else
		{
			printInvalidLogLevel(level);
		}
	}

	public static void show(Level level)
	{
		if (level.ordinal() < Level.NUM_LEVELS.ordinal())
		{
			SUPPRESSED[level.ordinal()] = false;
		}
		else
		{
			printInvalidLogLevel(level);
		}
	}

	public static void colourize()
	{
		enableColour = true;
	}

	public static void colourless()
	{
		enableColour = false;
	}

	public static void trace(boolean file, boolean line, boolean caller)
	{
		traceFile = file;
		traceLine = line;
		traceCaller = caller;

		if (file || line || caller)
		{
			enableTrace = true;
		}
		else
		{
			enableTrace = false;
		}
	}

	public static void error(String format, Object ... args)
	{
		System.out.print(formatMessage(Level.ERROR, format, args));
	}

	public static void warning(String format, Object ... args)
	{
		System.out.print(formatMessage(Level.WARNING, format, args));
	}

	public static void success(String format, Object ... args)
	{
		System.out.print(formatMessage(Level.SUCCESS, format, args));
	}

	public static void debug(String format, Object ... args)
	{
		System.out.print(formatMessage(Level.DEBUG, format, args));
	}

	public static void info(String format, Object ... args)
	{
		System.out.print(formatMessage(Level.INFO, format, args));
	}

	public static void verbose(String format, Object ... args)
	{
		System.out.print(formatMessage(Level.VERBOSE, format, args));
	}
}
