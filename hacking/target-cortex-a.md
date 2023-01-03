# Cortex A Targets

This captures some discussion from Gitter on Cortex-A driver implementation.

The Cortex-A driver supports ARMv7-A with a little Zynq-7000 specific code. ARMv8 has some in common, but many significant differences.

These Cortex-A variants should already be detected correctly: A5, A7, A8, and A9
https://github.com/blacksphere/blackmagic/blob/master/src/target/adiv5.c#L202

These bits may need to change for devices other than Zynq-7000:
- Cache line length: https://github.com/blacksphere/blackmagic/blob/master/src/target/cortexa.c#L77
- Reset implementation: https://github.com/blacksphere/blackmagic/blob/master/src/target/cortexa.c#L555

The current support has been used with Zynq-7000 (Dual-core A9) and Raspberry-Pi v2 (Quad-core A7) with success.
It is only of limited use in SMP configurations, as it's only possible to attach to a single core at one time.  SMP support is not a planned feature in BMP at this stage, but speak up on Gitter if you're interested in adding it.

A big challenge with Cortex-A devices as the variety of configurations. With Cortex-M microcontrollers, detecting the specific device is easy, and memory map and flash are generally fixed for a particular device. On Cortex-A memories are often external, so there are significantly more options.
