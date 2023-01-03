# SAM3x-4x-x7x

Black Magic Probe supports a lot of targets from many manufacturers.
Despite the effort to provide a unified way of handling the targets, some specificities exist.
This page documents some of them.

## Commands

### gpnvm get

Show the current status of GPNVM bits

```
gpnvm get
```

```
(gdb) monitor gpnvm get
GPNVM: 0x00000040
```

### gpnvm set

Set or clear the masked GPNVM bits

Valid bits range from 0 to 8 (see table)

```
gpnvm set <mask> <value>
```

```
(gdb) monitor gpnvm set 0x180 0x180
GPNVM: 0x000001C0
```

### Bits

SAMX7X

| GPNVM Bit | Function            | Values                                      |
|-----------|---------------------|---------------------------------------------|
| 0         | Security bit        | 0: disabled                                 |
|           |                     | 1: enabled                                  |
| 1         | Boot mode selection | 0: ROM                                      |
|           |                     | 1: Flash                                    |
| 5:2       | Free                |                                             |
| 6         | Reserved            |                                             |
| 8:7*      | TCM configuration   | 00: 0 Kbytes DTCM + 0 Kbytes ITCM (default) |
|           |                     | 01: 32 Kbytes DTCM + 32 Kbytes ITCM         |
|           |                     | 10: 64 Kbytes DTCM + 64 Kbytes ITCM         |
|           |                     | 11: 128 Kbytes DTCM + 128 Kbytes ITCM       |

`*Note: these bits only take effect after a reset, changing them via the gpnvm command will reset the target automatically`
