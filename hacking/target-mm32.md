# MindMotion MM32 Targets

This document

- Introduces MM32 processors
- Lists the MindMotion MM32 processors currently supported in Black Magic Probe and
- Explains how to add new MindMotion MM32 processors to Black Magic Probe.

## Introduction

[MindMotion](https://www.mindmotion.com.cn/en/products/) is a manufacturer of Arm processors located in Shanghai, China.

MindMotion MM32 processors have similarities with STM32, but are not binary compatible with STM32. The clock generation tree is different. This means STM32 start-up code cannot be used.

MM32 peripherals are similar to STM32 peripherals.

- Flash. On STM32, 16-bit Flash writes use bits 0:15 for even halfwords; bits 16:31 for odd halfwords. On MM32 Cortex-M0, 16-bit Flash writes always use bits 0:15.
- SPI frame size is configurable from 1 to 32 bits, inclusive.

MM32 Arm architectures include Cortex-M0, Cortex-M0+, Cortex-M3, and Star-MC1.

STAR-MC1 is a "Made in China" Arm architecture, similar to Cortex-M3, and is used in newer MM32 processors. Comparing the memory map of the MM32F3270 Cortex-M3 and the MM32F5270 Star-MC1:

- Cortex-M3 has main memory at 0x2000000.
- Star-MC1 has 32 kibibyte tightly coupled ram at 0x2000000 for the stack. Main memory is at 0x3000000.

At the time of writing, Black Magic Probe supports the following MindMotion MM32 processors:

|MCU|architecture
---|---
MM32F3273|Cortex-M3
MM32F5277|STAR-MC1
MM32L07x|Cortex-M0
MM32SPIN05|Cortex-M0
MM32SPIN27|Cortex-M0

To add a new MM32 processor to Black Magic Probe four values are required: product ID, name, Flash size, and RAM size.

## HOWTO Add new MM32 Cortex-M0 or Cortex-M0+

To add support for a new MM32 Cortex-M0 or Cortex-M0+ processor, first check the product ID at address 0x40013400.
E.g. for MM32SPIN05:
```
(gdb) mon swd
Target voltage:
Available Targets:
No. Att Driver
*** 1   Unknown ARM Cortex-M Designer 0x43b Part ID 0x471 M0
(gdb) at 1
Attaching to Remote target
warning: No executable has been specified and target does not support
determining executable automatically.  Try using the "file" command.
warning: while parsing target memory map (at line 1): Required element <memory> is missing
0xfffffffe in ?? ()
(gdb) set mem inaccessible-by-default off
(gdb) x 0x40013400
0x40013400:	0xcc4460b1
```
The product id can also be found by searching the - English or Chinese - user manual for "DEV_ID". DEV_ID is the 32-bit Cortex JEDEC-106 ID code.

With the product ID known, add a new case to the switch statement in file src/target/stm32f1.c, function mm32l0xx_probe() :
```
case 0xcc4460b1U:
        name = "MM32SPIN05";
        flash_kbyte = 32;
        ram_kbyte = 4;
        break;
```
where flash_kbyte is the amount of Flash at 0x08000000, and ram_kbyte is the amount of RAM at 0x20000000.

## HOWTO Add new MM32 Cortex-M3 or STAR-MC1

To add support for a new MM32 Cortex-M3 or STAR-MC1 processor, first check the product ID at address 0x40007080.
E.g. for MM32F3273:
```
(gdb) mon swd
(gdb) at 1
(gdb) set mem inaccessible-by-default off
(gdb) x 0x40007080
0x40007080:	0xcc9aa0e7
```
With the product ID known, add a new case to the switch statement in file src/target/stm32f1.c, function mm32f3xx_probe() :
```
case 0xcc9aa0e7U:
        name = "MM32F3270";
        flash_kbyte = 512;
        ram1_kbyte = 128;
        break;
```
where flash_kbyte is the amount of Flash at 0x08000000, ram1_kbyte is the amount of RAM at 0x20000000. For STAR-MC1 processors with RAM at 0x30000000, set ram2_kbyte to the amount of RAM at 0x30000000.

If different models exist that have the same product ID but different amounts of Flash or RAM, choose the model with the largest amount of Flash or RAM.

Lastly, open a GitHub "Pull Request" to add the processor to the main [Black Magic Debug repository](https://github.com/blackmagic-debug/blackmagic).

## Resources

- [HAL library and sample code](https://www.mindmotion.com.cn/en/development_tools/) contains start-up code for Keil and IAR
- [mm32_startup](https://github.com/iclite/mm32_startup/) start-up code for mm32 with gcc
- [libgcc.a patch](https://github.com/koendv/MM32SPIN27-Arduino/tree/main/mm32/mm32-libgcc) to use hardware division with gcc on MM32 Cortex-M0.
- Arduino for [MM32SPIN27](https://github.com/koendv/MM32SPIN27-Arduino)
- Arduino for [MM32F031](http://47.106.166.129/fenyi/4_channel_SPDT_relay_wirmware/)
- SeekFree [libraries](https://gitee.com/seekfree/projects)  for MM32F527X, MM32F327X, MM32SPIN27, MM32SPIN360 and others

