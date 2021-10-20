import java.util.Arrays;
import java.lang.StackTraceElement;

// ===================== CONSTANTS ===================== //

class Log
{
	private static final String ERROR_COLOUR = Colours.RED;
	private static final String WARNING_COLOUR = Colours.YELLOW;
	private static final String SUCCESS_COLOUR = Colours.GREEN;
	private static final String DEBUG_COLOUR   = Colours.CYAN;
	private static final String INFO_COLOUR    = Colours.BLUE;
	private static final String NOTE_COLOUR    = Colours.MAGENTA;

	private static final String ERROR_PREFIX   = "X";
	private static final String WARNING_PREFIX = "!";
	private static final String SUCCESS_PREFIX = "~";
	private static final String DEBUG_PREFIX   = "#";
	private static final String INFO_PREFIX    = ">";
	private static final String NOTE_PREFIX    = "@";

	private static final String [] PREFIXES = {
		ERROR_PREFIX,
		WARNING_PREFIX,
		SUCCESS_PREFIX,
		DEBUG_PREFIX,
		INFO_PREFIX,
		NOTE_PREFIX
	};

	private static final String [] COLOURS = {
		ERROR_COLOUR,
		WARNING_COLOUR,
		SUCCESS_COLOUR,
		DEBUG_COLOUR,
		INFO_COLOUR,
		NOTE_COLOUR
	};

	public enum Level
	{
		ERROR,
		WARNING,
		SUCCESS,
		DEBUG,
		INFO,
		NOTE,

		NUM_LEVELS
	};

	private static final String [] LEVEL_NAMES = {
		"ERROR",
		"WARNING",
		"SUCCESS",
		"DEBUG",
		"INFO",
		"NOTE"
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

		return String.format("%s%s%s ", file, line, caller);
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

	public static void note(String format, Object ... args)
	{
		System.out.print(formatMessage(Level.NOTE, format, args));
	}
}
