# Building `bmputil` on Windows

## Background

`bmputil` is a companion tool to the project for managing the firmware on your probes, allowing easy and fast switching
and upgrade of the runing firmware. The tool is available on all major OSes, but special attention and care must be paid
on Windows to build it successfully and correctly.

The tool may be cross-built for Windows, which is detailed after the main section on acomplishing a build on Windows
itself.

## Pre-requisites

The tool requires a few pre-requisites to be available, starting with a copy of the Rust compiler and stdlib installed
via rustup. Due to how one of the dependencies works, you will need a working installation of Visual Studio or at least
the build tools component as well. It must feature both x86_64 and AArch64 support. Said same dependency also requires a
working installation of the WDK (Windows Driver Kit) development kit version 8.0 to be available.

Details of how to acomplish all that are outlined below:

1. Everything starts by installing Visual Studio or Build Tools for Visual Studio - the rustup book provides
   a good [guide for acomplishing this](https://rust-lang.github.io/rustup/installation/windows-msvc.html), though
   it must be noted that for `bmputil` you must install both the "x64/x86 build tools" component as well as the
   "ARM64 build tools" component as we require both MSVC compiler flavours.
2. Install [rustup](https://rustup.rs/), which is a toolchain manager for Rust. Follow those instructions on their
   website, and then continue here at 3.
3. Install Rust stable via rustup - run the following (presuming x86_64 Windows) on a console that has rustup on path:

```sh
rustup set default-host x86_64-pc-windows-msvc
rustup toolchain install stable
rustup target add aarch64-pc-windows-msvc
```

4. Install the [WDK v8.0 redistributable components](https://go.microsoft.com/fwlink/p/?LinkID=253170) to the default
   path the installer chooses (you can do it to a different one but will have to adjust the path for the environment
   in the build steps below).

## Building `bmputil`

The following instructions must be executed either from in a shell that used the "Developer Command Prompt" launcher
to have all compilers available, or have a shell-appropriate version of the VsDevCmd script executed to put the
compilers into the available environment for the build process to find.

If using the VsDevCmd script, you will want to run either:

* cmd.exe:

```sh
"C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\Tools\VsDevCmd.bat"
```

* PowerShell:

```sh
. "C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\Tools\Launch-VsDevShell.ps1"
```

(This assumes you are using Visual Studio 2022, which is the latest available at time of writing - update as
appropriate if you are using newer. It is ill advised to run older.)

Before we can run any build commands, we must first execute the following to make the WDK available:

* cmd.exe:

```sh
set WDK_PATH="C:\Program Files (x86)\Windows Kits\8.0"
```

* PowerShell:

```sh
$env:WDK_PATH = "C:\Program Files (x86)\Windows Kits\8.0"
```

Having done that, building (assuming you have the Rust toolchain on PATH from the pre-requisites!) is thankfully quite
simple - run:

```sh
cargo build --release
```

When that completes, you will have a binary available ready to run in `target/release` under the name `bmputil-cli`.
You may then either copy this to a location found on PATH (`%PATH%` for cmd.exe, `$env:PATH` for PowerShell/pwsh)
or run it directly as in `target/release/bmputil-cli --help`.
