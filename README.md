# wdd

Wireless Traffic Sensing and Analysis

## Description

This project plans to exploit certain dimensions of wireless sensing and packet analysis.

* WiFi

### Note

* Consider all code here in as a developmental prototype and forgive any imperfections

### slave_sniff.py is loaded onto each agent (probably a raspberry pi) and will execute sniff, filter, send

* Sniff
* Filter
  * Filtering for the desired kind of WiFi Packets (eg mostly probe requests)
  * Also, for ethical reasons, this provides the opportunity to white-list MAC addresses when needed
* Send
  * To the Central Server for Analysis
  * For testing the initial prototype, an e-mail will be sent

### Setting up the individual agent (eg Raspberry Pi)

* Physical Connections
  * Connect via USB: mouse, Alfa Card, keyboard,
* Download the software/git package
* Terminal
  * sudo apt-get install aircrack-ng
  * sudo airmon-ng
  * sudo airmon-ng check
  * sudo airmon-ng kill
  * sudo airmon-ng start wlan0
  * iwconfig
    * to confirm that mon0 is up in Mode:Monitor

### Analyzing Packets

* Packets will be saved to a database on the central server.

### Current Work, Status

* Currently, this project is in the status of laying down the groundwork for work that might go in a number of directions.  This groundwork may be almost a repeat of sources found elsewhere.  Sources and references are cited as much as is feasible.
  * Using the scapy package in python to sniff wireless traffic and/or parse a pcap file
  * Converting a scapy packet list into a specified XML file

### Possible Directions this Project Might Take

* Cross-Device Correlation
 * Attribute packets to an individual as opposed to a device or MAC Address


### Test Plan

* Use capture1-05.cap as a private test: one sensor to the main terminal
* Main Terminal is 127.0.0.1
* Arrange everything in the testconfig file

### References

### Similar Work / Projects

### Diagram

#### Simple, Prototype Test Case


Slave              | Xfer Medium |  Master / Central Node

Sniff -> XML File -> String      -> XML File -> Dictionary -> mySQL DB

