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

		Log.suppress(Log.Level.ERROR);
		Log.error("ERROR");
		Log.verbose("VERBOSE");
	}
}
