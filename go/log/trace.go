package log

import (
	"errors"
	"fmt"
	"runtime"
)

func GetTrace() (string, int, string, error) {
	pc, fileName, lineNum, ok := runtime.Caller(3)
	if !ok {
		return "", -1, "", errors.New("unable to get caller")
	}

	return fileName, lineNum, runtime.FuncForPC(pc).Name(), nil
}

func FormatTrace(fileName string, lineNum int, funcName string) string {
	if !ENABLE_TRACE {
		return ""
	}

	traceFormat := fmt.Sprintf("%s:%d %s", fileName, lineNum, funcName)

	return traceFormat
}
