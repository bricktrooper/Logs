import log

log.trace_file(False)
log.trace_line(False)
log.trace_caller(True)
log.disable()
log.enable()

def test():
	log.error("Asd")

test()
log.error("ERROR")
log.warning("WARNING")
log.success("SUCCESS")
log.info("INFO")
log.debug("DEBUG")
log.note("NOTE")
