# GDB Commands

This page provides a brief summary of the most commonly used GDB commands with the Black Magic Probe.  It is provided just as an introduction, the [GDB Manual](https://sourceware.org/gdb/current/onlinedocs/gdb) should be consulted for more complete information.

GDB's online help system is also a good source of information.  Use the command `help <command>` for more information about any GDB command.

## Connecting to the Black Magic Probe and target
### Connecting GDB to the Black Magic Probe
```
target extended-remote <port>
```
This command connects GDB to the Black Magic Probe for remote target debugging.  It does not perform any JTAG or SWD actions and does not attach GDB to the target processor.

The port parameter should be the name of the serial interface of the GDB server provided by the Black Magic Probe.
On Linux:
```
target extended-remote /dev/ttyACM0
target extended-remote /dev/serial/by-id/usb-Black_Sphere_Technologies_Black_Magic_Probe_E2C0C4C6-if00
target extended-remote /dev/ttyBmpGdb
```
On macOS:
```
target extended-remote /dev/cu.usbmodemE2C0C4C6
```
On Windows:
```
target extended-remote COM3
target extended-remote \\.\COM10
```

### List available Black Magic Probe commands
```
(gdb) monitor help
General commands:
	version -- Display firmware version info
	help -- Display help for monitor commands
	jtag_scan -- Scan JTAG chain for devices
	swdp_scan -- Scan SW-DP for devices: [TARGET_ID]
	auto_scan -- Automatically scan all chain types for devices
	frequency -- set minimum high and low times: [FREQ]
	targets -- Display list of available targets
	morse -- Display morse error message
	halt_timeout -- Timeout to wait until Cortex-M is halted: [TIMEOUT, default 2000ms]
	connect_rst -- Configure connect under reset: [enable|disable]
	reset -- Pulse the nRST line - disconnects target: [PULSE_LEN, default 0ms]
	tdi_low_reset -- Pulse nRST with TDI set low to attempt to wake certain targets up (eg LPC82x)
	traceswo -- Start trace capture, NRZ mode: [BAUDRATE] [decode [CHANNEL_NR ...]]
	heapinfo -- Set semihosting heapinfo: HEAPINFO HEAP_BASE HEAP_LIMIT STACK_BASE STACK_LIMIT
```

The list of available commands is context sensitive. After connecting to certain targets the list of available commands changes. For example STM32 targets provide `monitor erase_mass` that is not available until you scan for available targets and find the STM32 target.

### Finding connected targets
```
monitor jtag_scan
monitor swdp_scan
```
These commands instruct the Black Magic Probe to scan for connected target devices using the JTAG or SWD interfaces.  Any currently connected target will be detached by this command.

```
monitor tpwr enable
```
Using black magic probe v2, there is a voltage translator present. By default, the voltage translator is off, and expects a Vtarget voltage present. If Vtarget is not connected to the target board, use the tpwr enable command to power translator with the onboard 3.3V regulator.

### Attaching to a target
```
attach <n>
```
Attach GDB to a target device connected to the Black Magic Probe.  The argument must be a target id displayed in the output of one of the monitor commands above.  Attaching will not reset the target, for that use the `run` or `start` commands.

### Enabling access to memory mapped IO from GDB
```
set mem inaccessible-by-default off
```
This command instructs GDB to allow access to memory outside of the devices known memory map.  This is useful to allow access to memory mapped IO from GDB.

Because the above are all common commands that you are likely to run every time you start GDB, you may want to include them in your `.gdbinit` file.  Create a text file named `.gdbinit` in your home directory or project directory from which you run GDB and it will execute these commands on startup.

## Loading your program onto the target
```
load [filename]
```
This command will transfer your program binary to the target device.  If the program is linked at Flash memory addresses, the Flash will be erased and programmed accordingly.
```
compare-sections
```
This command will compare a CRC32 of the target memory to the sections of your binary file and report if an inconsistency is found.  It is useful to verify the flash programming.

## Debugging with GDB
### Starting your program
```
start
run
```
These command reset and begin execution on the target.  `run` allows the target to run normally until interrupted or other event occurs, while `start` runs through the start-up code will halt on entry to the `main` function.

While the target is running, it may be interrupted by typing Ctrl-C in the GDB console or sending GDB a SIGINT.

### Setting stop conditions
```gdb
break <function>
break <file>:<line>
watch <var>
```
These commands set breakpoints and watchpoints.  Breakpoints will interrupt the target when a particular location in the program is reached, and watchpoints will interrupt the program when a particular variable is changed.

### Examining the target state
```
print <expr>
x <address>
info registers
```
These commands may be used to inspect target variables, memory or core registers.

```
dump ihex memory <file> <start> <stop>
```
This command can be used to dump the target memory contents to an Intel hex file.  There are other variants for alternative formats, use the command `help dump` for more information.

### Detaching from the target device
```
detach
kill
```
These commands can be used to disconnect the Black Magic Probe from the target device.  `kill` will also reset the target on detach.
