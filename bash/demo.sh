#! /bin/bash

source log.sh

log_trace false false true

test()
{
	log_error "ERROR"
	log_warning "WARNING"
	log_success "SUCCESS"
}

test
log_info "INFO"
log_debug "DEBUG"

log_suppress ERROR
log_error "ERROR"
log_note "NOTE"
