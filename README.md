mojo-standalone
===============

Experiment at building a minimal repo for development of standalone Mojo apps.

To see it in action, do the following on a Linux64 machine (note: nothing will work on any other OS):

```
$ git clone https://github.com/colinblundell/mojo-standalone.git mojo_sdk
$ cd mojo_sdk
$ ./build/install-build-deps.sh
```

At this point you should be ready to go forward, although I must warn you that that the script for installing build deps doesn't have any error checking.

You can run one of the supported examples:

```
$ ./run_example.sh echo
$ ./run_example.sh apptest
```

or build the entire public SDK:

```
$ ./buildtools/gn out/Debug
$ ./buildtools/ninja -C out/Debug
```
If you have access to a Chromium checkout and a Mojo checkout, you can also try revving the SDK:

```
$ ./tools/rev_sdk.sh <path/to/chromium/src> <path/to/mojo/src>
```
