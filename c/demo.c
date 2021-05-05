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
	log_note("NOTE");
}