import log

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
