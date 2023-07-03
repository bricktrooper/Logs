package main

import (
	"fmt"

	"github.com/bricktrooper/Logs/go/log"
)

func myfunc(message string) {
	log.LogError("Error:", message)
	log.LogWarning("Warning:", message)
	log.LogSuccess("Success:", message)
	log.LogDebug("Debug:", message)
	log.LogInfo("Info:", message)
	log.LogVerbose("Verbose:", message)
}

func main() {
	fmt.Println("----------------------------")
	myfunc("Logging enabled")

	fmt.Println("----------------------------")
	log.Disable()
	myfunc("Logging disabled")

	fmt.Println("----------------------------")
	log.Enable()
	log.LogLevelWarning.Suppress()
	myfunc("Warnings suppressed")

	fmt.Println("----------------------------")
	log.LogLevelWarning.Show()
	log.Colourless()
	myfunc("Colourless logging")

	fmt.Println("----------------------------")
	log.Colourize()
	log.Traceful()
	myfunc("Logging with trace")
}
