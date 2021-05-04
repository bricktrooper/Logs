import log

log.trace(file = False, line = False, caller = True)

def test():
	log.error("ERROR")
	log.warning("WARNING")
	log.success("SUCCESS")
	log.info("INFO")
	log.debug("DEBUG")
	log.note("NOTE")

test()
