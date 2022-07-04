# STM32 Targets

Black Magic Probe supports a lot of targets from many manufacturers.
Despite the effort to provide a unified way of handling the targets, some specificities exist.
This page documents some of them.

## STM32G0 OTP programming

Many STM32 chips provide a One Time Programmable flash memory area. This area is typically used to store read-only data, e.g. secure keys or any very stable non volatile data. Program code is very likely not stored in this area.

As of current master branch (November 2021), OTP programming is only supported for the STM32G0 series.

It is _not recommended_ to write the OTP area from GDB for at least two reasons:

* Due to a different page/block size of the OTP area compared to the main flash program memory, one can notice ARM GDB's unexpected behaviour (as of version 8) in case of programming a file to areas with heterogeneous block sizes (in particular, some program code sections appear split when sent over the debug probe). Programming such a file will probably fail.

* OTP is by definition programmed once whereas GDB usage is likely to happen several times, especially invoking its `load` operation which would attempt to write the OTP area as many times as debugging a new firmware.

For these reasons, the preferred way of OTP programming is done from _hosted_ Blackmagic.

## Programming OTP from hosted blackmagic

Before, make sure you have an OTP only binary data. The next chapter can help you doing that.

STM32G0 non reversible operations (currently Read Out Protection level 2 and OTP programming) are protected with an `irreversible enable|disable` monitor command.

Note: this monitor command may change any time in the future.

Then, the start address of the OTP write has to be explicitly specified to prevent blackmagic from defaulting to 0x08000000 main flash start.

Note that any multiple of 8 bytes sized data can be written to an 8-byte aligned _free_ address (not already programmed with non 0xFF data).
Consequently, one can program a piece of the entire OTP area and program the rest (or some of the rest) later.

Typical usage:
```shell
$ blackmagic -M "irreversible enable" -a 0x1FFF7000 otp_1024bytes.bin
Irreversible operations: enabled
Flash Write succeeded for 1024 bytes,    x.yyy kiB/s
```

For a sub part of OTP:
```shell
$ blackmagic -M "irreversible enable" -a 0x1FFF73E0 otp_8bytes.bin
Irreversible operations: enabled
Flash Write succeeded for 8 bytes,    1.143 kiB/s
```

## Preparing an OTP only binary data

Here is an example of defining OTP data in a C source file.
As mentioned before, is is recommended to link this file only once, not along the program code.
```
/* OTP */
const uint32_t otp_tab[2] __attribute__ ((section (".otp"))) = {
	0xAABBAABB, 0xCCDDCCDD
};
```

The linker script can be populated with the .otp section as followed:
```
MEMORY
{
	/* rom and ram definitions here */
	otp (r) : ORIGIN = 0x1FFF7000, LENGTH = 1K
}
SECTIONS
{
	.otp : {
		. = ALIGN(8);
		KEEP(*(.otp))
		. = ALIGN(8);
	} >otp
}
```

Once the linked elf file is generated, the output .otp section can be extracted with the objcopy binutil:
```shell
$ arm-none-eabi-objcopy -j ".otp" -O binary firmware.elf otp_data.bin
```