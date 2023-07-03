#include "log.h"

int main(void)
{
	log_error("ERROR");
	log_warning("WARNING");
	log_success("SUCCESS");
	log_info("INFO");
	log_debug("DEBUG");
	log_verbose("VERBOSE");
}
