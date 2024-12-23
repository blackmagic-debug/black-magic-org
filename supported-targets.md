# Supported Targets

## Cortex-M

| Manufacturer      | Family      | Support Level | Version Introduced | Implemented In | Notes
|-------------------|-------------|---------------|--------------------|----------------|------
| ST Micro          | STM32F0     | ✔ Full        | v1.6               | stm32f1.c      | -
| ST Micro          | STM32F1     | ✔ Full        | pre-v1.6           | stm32f1.c      | -
| ST Micro          | STM32F2     | ✔ Full        | v1.6               | stm32f4.c      | -
| ST Micro          | STM32F3     | ✔ Full        | v1.6               | stm32f1.c      | -
| ST Micro          | STM32F4     | ✔ Full        | pre-v1.6           | stm32f4.c      | -
| ST Micro          | STM32F7     | ✔ Full        | v1.6               | stm32f4.c      | -
| ST Micro          | STM32G0     | ✔ Full        | v1.8.0             | stm32g0.c      | -
| ST Micro          | STM32G4     | ✔ Full        | v1.6.2             | stm32l4.c      | -
| ST Micro          | STM32C0     | ✔ Full        | v1.10.0            | stm32g0.c      | -
| ST Micro          | STM32H5     | ✔ Full        | v1.10.0            | stm32h5.c      | -
| ST Micro          | STM32H7     | ✔ Full        | v1.8.0             | stm32h7.c      | [^1]
| ST Micro          | STM32L0     | ✔ Full        | v1.6               | stm32l0.c      | -
| ST Micro          | STM32L1     | ✔ Full        | v1.6               | stm32l0.c      | -
| ST Micro          | STM32L4     | ✔ Full        | pre-v1.6           | stm32l4.c      | -
| ST Micro          | STM32L55    | ✔ Full        | v1.8.0             | stm32l4.c      | -
| ST Micro          | STM32U5     | ✔ Full        | v1.10.0            | stm32l4.c      | -
| ST Micro          | STM32WL     | ✔ Full        | v1.8.0             | stm32l4.c      | -
| ST Micro          | STM32WB     | ✔ Full        | v1.8.0             | stm32l4.c      | -
| ST Micro          | STM32WB0    | ✔ Full        | v2.0.0             | stm32wb0.c     | -
| ST Micro          | STM32MP15   | ✔ Full        | v2.0.0             | stm32mp15.c    | -
| GigaDevice        | GD32F1      | ✔ Full        | v1.8.0             | stm32f1.c      | -
| GigaDevice        | GD32F2      | ✔ Full        | v1.10.0            | stm32f1.c      | -
| GigaDevice        | GD32F3      | ✔ Full        | v1.8.0             | stm32f1.c      | -
| GigaDevice        | GD32F4      | ✔ Full        | v1.10.0            | stm32f4.c      | -
| GigaDevice        | GD32E230    | ✔ Full        | v1.8.0             | stm32f1.c      | -
| GigaDevice        | GD32E5      | ✔ Full        | v1.10.0            | stm32f1.c      | -
| ArteryTek         | AT32F40     | ✔ Full        | v1.9.0             | stm32f1.c      | -
| ArteryTek         | AT32F405    | ✔ Full        | v2.0.0             | at32f43x.c     | -
| ArteryTek         | AT32F41     | ✔ Full        | v1.9.0             | stm32f1.c      | -
| ArteryTek         | AT32F423    | ✔ Full        | v2.0.0             | at32f43x.c     | -
| ArteryTek         | AT32F43     | ✔ Full        | v1.10.0            | at32f43x.c     | -
| MindMotion        | MM32L0      | ✔ Full        | v1.10.0            | stm32f1.c      | -
| MindMotion        | MM32SPIN    | ✔ Full        | v1.10.0            | stm32f1.c      | -
| MindMotion        | MM32F3      | ✔ Full        | v1.10.0            | stm32f1.c      | -
| MindMotion        | MM32F5      | ✔ Full        | v1.10.0            | stm32f1.c      | -
| WinChipHead       | CH32F1      | ✔ Full        | v1.8.0             | ch32f1.c       | -
| WinChipHead       | CH579       | ✔ Full        | v2.0.0             | ch579.c        | -
| Puya              | PY32F       | ✔ Full        | v2.0.0             | puya.c         | -
| Texas Instruments | LM3S        | ✔ Full        | pre-v1.6           | lmi.c          | -
| Texas Instruments | LM4C/TM4C   | ✔ Full        | v1.6               | lmi.c          | -
| Microchip         | ATSAM D5/E5 | ✔ Full        | v1.6.2             | samx5x.c       | -
| Atmel             | ATSAM D     | ✔ Full        | v1.6               | samd.c         | -
| Atmel             | ATSAM 4L    | ✔ Full        | v1.6               | sam4l.c        | -
| Atmel             | ATSAM 3x    | ✔ Full        | v1.6               | sam3x.c        | -
| RPi Foundation    | RP2040      | ✔ Full        | v1.8.0             | rp2040.c       | -
| RPi Foundation    | RP2350      | ✔ Full        | v2.0.0             | rp2350.c       | -
| Renesas           | R7FA        | ○ Partial     | v1.9.0             | renesas_ra.c   | Unless specified below
| Renesas           | R7FARA2A1   | ✗ Debug only  | v1.9.0             | renesas_ra.c   | -
| Renesas           | R7FARA4M2   | ✔ Full        | v1.9.0             | renesas_ra.c   | -
| Renesas           | R7FARA4M3   | ✔ Full        | v1.9.0             | renesas_ra.c   | -
| Renesas           | R7FARA6M2   | ✔ Full        | v1.9.0             | renesas_ra.c   | -
| Freescale         | KE04        | ✔ Full        | v1.6.2             | nxpke04.c      | -
| Nordic Semi       | nRF51       | ✔ Full        | v1.6               | nrf51.c        | -
| Nordic Semi       | nRF52       | ✔ Full        | v1.6               | nrf51.c        | -
| Nordic Semi       | nRF54L      | ✔ Full        | v2.0.0             | nrf54l.c       | -
| Nordic Semi       | nRF91       | ✔ Full        | v1.10.0            | nrf91.c        | -
| Texas Instruments | MSP432P4    | ✔ Full        | v1.6.2             | msp432p4.c     | -
| Texas Instruments | MSP432E4    | ✔ Full        | v1.10.0            | msp432e4.c     | -
| NXP               | LPC546      | ✔ Full        | v1.8.0             | lpc546xx.c     | -
| NXP               | LPC55       | ✔ Full        | v1.10.0            | lpc55xx.c      | -
| NXP               | LPC43       | ✔ Full        | v1.6               | lpc43xx.c      | [^2]
| NXP               | LPC40       | ✔ Full        | v1.10.0            | lpc40xx.c      | -
| NXP               | LPC17       | ✔ Full        | v1.6.2             | lpc17xx.c      | -
| NXP               | LPC15       | ✔ Full        | v1.6               | lpc15xx.c      | -
| NXP               | LPC8        | ✔ Full        | v1.6               | lpc11xx.c      | -
| NXP               | LPC11       | ✔ Full        | v1.6               | lpc11xx.c      | -
| Freescale         | KL02        | ✔ Full        | pre-v1.6           | kinetis.c      | -
| Freescale         | KL03        | ✔ Full        | v1.6               | kinetis.c      | -
| Freescale         | KL16Z       | ✔ Full        | v1.6.2             | kinetis.c      | -
| Freescale         | KL25        | ✔ Full        | v1.6               | kinetis.c      | -
| Freescale         | KL27        | ✔ Full        | v1.6               | kinetis.c      | -
| Freescale         | K12         | ✔ Full        | v1.8.0             | kinetis.c      | -
| Freescale         | K22F        | ✔ Full        | pre-v1.6           | kinetis.c      | -
| Freescale         | K64F        | ✔ Full        | v1.6.2             | kinetis.c      | -
| NXP               | S32K11      | ✔ Full        | v1.8.0             | kinetis.c      | -
| NXP               | S32K14      | ✔ Full        | v1.8.0             | kinetis.c      | -
| NXP               | i.MX RT10   | ✔ Full        | v1.10.0            | imxrt.c        | -
| NXP               | i.MX RT11   | ✔ Full        | v1.10.0            | imxrt.c        | -
| NXP               | i.MX RT5    | ✔ Full        | v1.10.0            | imxrt.c        | -
| NXP               | i.MX RT6    | ✔ Full        | v1.10.0            | imxrt.c        | -
| HDSC              | HD32L110    | ✔ Full        | v1.10.0            | hd32l110.c     | -
| Energy Micro      | EFM32       | ✔ Full        | v1.6               | efm32.c        | -
| Energy Micro      | EZR32       | ✔ Full        | v1.6               | efm32.c        | -
| Energy Micro      | EFR32       | ✔ Full        | v1.6.2             | efm32.c        | -
| Ambiq             | Apollo 3    | ✗ Debug only  | v2.0.0             | apollo3.c      | -

[^1]: H72/H73, and H7A/H7B support was added in v2.0.0.
[^2]: LPC43x0 Flash support was added in v1.10.0.

## Cortex-A

| Manufacturer      | Family      | Support Level | Version Introduced | Implemented In | Notes
|-------------------|-------------|---------------|--------------------|----------------|------
| Renesas           | RZ/A1       | ✔ Full        | v2.0.0             | renesas_rz.c   | -
| Renesas           | RZ/A1L      | ✔ Full        | v2.0.0             | renesas_rz.c   | -
| Renesas           | RZ/A1LU     | ✔ Full        | v2.0.0             | renesas_rz.c   | -
| Renesas           | RZ/A1C      | ✔ Full        | v2.0.0             | renesas_rz.c   | -
| Renesas           | RZ/A1H      | ○ Partial     | v2.0.0             | renesas_rz.c   | -
| ST Micro          | STM32MP15   | ✔ Full        | v2.0.0             | stm32mp15.c    | -
| Xilinx            | Zynq7000    | ✗ Debug only  | v1.6               | zynq7000.c     | -
| Broadcom          | BCM2836     | ✗ Debug only  | v1.6               | cortexa.c      | -

## RISC-V 32-bit

| Manufacturer      | Family      | Support Level | Version Introduced | Implemented In | Notes
|-------------------|-------------|---------------|--------------------|----------------|------
| GigaDevice        | GD32VF1     | ✔ Full        | v2.0.0             | stm32f1.c      | -
| RPi Foundation    | RP2350      | ✔ Full        | v2.0.0             | rp2350.c       | -
