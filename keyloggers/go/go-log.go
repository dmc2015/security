package main

import (
	"log"

	"github.com/MarinX/keylogger"
)

func main() {
	listen()
}

func listen() {
	// for

	keyboard := keylogger.FindKeyboardDevice()

	log.Printf("Found keyboard: %s", keyboard)
	// status := watcher.States()

	// for {
	// 	fmt.Println("listening")
	// 	in := bufio.NewScanner(os.Stdin)
	// 	data := in.Bytes()
	// 	fmt.Printf("string: %s", in)
	// 	fmt.Printf("byte: %s", data)
	// }

}
