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
$ ./buildtools/gn gen out/Debug
$ ./buildtools/ninja -C out/Debug
```
The basic structure of the repo is that mojo/public is taken straight from the Mojo repo with no modification, as well as supported apps from examples/. The rest of the repo is then built up to be a minimal self-contained framework that allows building and running the supported apps without any external dependencies (other than the ones fetched by install-build-deps.sh).

If you have access to a Chromium checkout and a Mojo checkout, you can try revving the SDK and examples from the Mojo repo:

```
$ ./tools/rev_sdk.sh <path/to/chromium/src> <path/to/mojo/src>
```
