# Logging API

### Usage

Messages can be printed on any of the following log levels:

```
log_error <message>
log_warning <message>
log_success <message>
log_debug <message>
log_info <message>
log_verbose <message>
```

Each log level has an associated string:

```
"ERROR"
"WARNING"
"SUCCESS"
"DEBUG"
"INFO"
"VERBOSE"
```

Each log level has a prefix symbol with a unique ANSI colour.  If your terminal does not support colours, you can disable it:

```
log_colourless
log_colourize
```

Each log level can be individually suppressed:

```
log_suppress <level>
log_show <level>
```

All log printing can be disabled.  This overrides suppressions.  When enabled, suppressions still apply:

```
log_enable
log_disable
```

The file, line number, and calling function of log prints can be traced.
By default, tracing is disabled.  It can be enabled using the boolean arguments of the following function:

```
log_trace <file> <line> <caller>
```

### Example

The following example can be found in `demo.sh`

#### Code

```
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
log_verbose "VERBOSE"
```

#### Output

```
X test: ERROR
! test: WARNING
~ test: SUCCESS
> main: INFO
# main: DEBUG
@ main: VERBOSE
```
