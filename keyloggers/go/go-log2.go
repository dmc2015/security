package main

import (
	"fmt"
	"github.com/MarinX/keylogger"
	"github.com/jaypipes/ghw"
	"github.com/shirou/gopsutil/v3/mem"
)

func main() {
	v, _ := mem.VirtualMemory()
	// pci, err := ghw.PCI()
	// chassis, err2 := ghw.Chassis()
	// bios, err3 := ghw.BIOS()
	// baseboard, err4 := ghw.Baseboard()
	// devices, err := keylogger.NewDevices()
	keyboard := keylogger.FindKeyboardDevice()

	// k  := keyboard
	fmt.Printf("pci %s}", pci)
	fmt.Printf("v %s}", v)
	
	// fmt.Printf("chassis %s}", chassis)
	// fmt.Printf("bios %s}", bios)
	// fmt.Printf("baseboard %s}", baseboard)
	
	fmt.Printf("err %s}", err)
	// fmt.Printf("err2 %s}", err2)
	// fmt.Printf("err3 %s}", err3)
	// fmt.Printf("err4 %s}", err4)


	fmt.Printf("keyboard %s}", keyboard)
	// fmt.Printf("keyloger %s}", keylogger)
	fmt.Print("logger")
	// if err != nil {
	// 	fmt.Printf("There is an error: {}", err)
	// 	return
	// }

	// for _, val := range devices {
	// 	fmt.Println("Id -> ", val.Id, "Device -> ", val.Name)
	// }

	// keyboard := keylogger.NewKeyLogger(devices[0])

	// in, err := keyboard.Read()

	// if err != nil {
	// 	fmt.Println(err)
	// 	return
	// }

	// for i := range in {

	// 	if i.Type == keylogger.EV_Key {
	// 		fmt.Println(i.KeyString())
	// 	}
	// }

}



// 83881     Keyboard:
// 83882 
// 83883       Version: 14.0
// 83884       Supported By: Apple
// 83885       Visible: Yes
// 83886       Identifier: com.apple.preference.keyboard
// 83887       Location: /System/Library/PreferencePanes/Keyboard.prefPane
// 83888       Kind: 64-Bit


// 83908     Mouse:
// 83909 
// 83910       Version: 14.0
// 83911       Supported By: Apple
// 83912       Visible: Yes
// 83913       Identifier: com.apple.preference.mouse
// 83914       Location: /System/Library/PreferencePanes/Mouse.prefPane
// 83915       Kind: 64-Bit


// 83917     Network:
// 83918 
// 83919       Version: 4.0
// 83920       Supported By: Apple
// 83921       Visible: Yes
// 83922       Identifier: com.apple.preference.network
// 83923       Location: /System/Library/PreferencePanes/Network.prefPane
// 83924       Kind: 64-Bit