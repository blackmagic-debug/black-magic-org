# Semihosting

With semihosting the target can do keyboard input, screen output, and file I/O on the host.

Standard ARMv6-M/ARMv7-M semihosting is supported, i.e. you can build your application in a special way to have calls to certain functions (`open()`, `close()`, `read()`, `write()`, `lseek()`, `rename()`, `unlink()`,
`stat()`, `isatty()`, `system()`) executed on the debugging host itself. To make use of these facilities, add `--specs=rdimon.specs` and `-lrdimon` to the linker flags for your firmware.

If you're going to use stdin, stdout or stderr (e.g. via `printf()`/`scanf()`) and you're not using newlib's C runtime (by specifying `-nostartfiles`), you need to add this to your initialisation:
```
void initialise_monitor_handles(void);
initialise_monitor_handles();
```

Arm Arduino users can use the semihosting library from the Library Manager.

This document describes the low level interface on the ARM side:
[Semihosting for AArch32 and AArch64](https://static.docs.arm.com/100863/0300/semihosting.pdf)