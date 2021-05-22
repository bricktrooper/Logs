import log

log.trace(file = False, line = False, caller = True)

def test():
	log.error("ERROR")
	log.warning("WARNING")
	log.success("SUCCESS")

test()
log.info("INFO")
log.debug("DEBUG")

log.suppress("ERROR")
log.error("ERROR")
log.note("NOTE")
