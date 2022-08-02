package main

import (
	"fmt"

	// "github.com/ghedo/go.pkt/capture/pcap"
	"github.com/google/gopacket"
	"github.com/google/gopacket/pcap"
)

// func interfaces() {
// 	ifaces, err := net.Interfaces()

// 	return ifaces, err
// }

// func main() {
// 	ifaces, err := net.Interfaces()

// 	if err != nil {
// 		log.Fatal(err)
// 	}

// 	fmt.Println(len(ifaces))
// 	// interface_name := ifaces[0].Name

// 	// net_data, pcapErr := pcap.Open("etho0")
// 	net_data, pcapErr := pcap.Open("awdl0")

// 	if pcapErr != nil {
// 		log.Fatal(pcapErr)
// 	}

// 	// fmt.Printf("ifaces : %x", ifaces)
// 	fmt.Printf("net_data : %x", net_data)

// 	defer net_data.Close()

// 	for {

// 		buf, err := net_data.Capture()

// 		if err != nil {
// 			log.Fatal(err)
// 		}

// 		log.Println("Packet")

// 		fmt.Printf("buf : %x", buf)

// 	}
// }

const (
	defaultSnapLen = 262144
)

func main() {
	handle, err := pcap.OpenLive("en0", defaultSnapLen, true, pcap.BlockForever)

	if err != nil {
		panic(err)
	}

	defer handle.Close()

	if err := handle.SetBPFFilter("port 3030"); err != nil {
		panic(err)
	}

	packets := gopacket.NewPacketSource(
		handle, handle.LinkType()).Packets()

	for pkt := range packets {
		fmt.Println(pkt)
	}

}
