# CAN-examples

CAN Examples repository

## vcan

[Reference](https://stackoverflow.com/questions/21022749/how-to-create-virtual-can-port-on-linux-c)

```
$ sudo modprobe vcan
$ sudo ip link add dev vcan0 type vcan
$ sudo ip link set up vcan0
```

## Build

```
$ gcc can_transmit.c -o can_tx
$ gcc can_receive.c -o can_rx
```

## Run

Terminal 1:

```
$ ./can_tx
```

Terminal 2:

```
$ ./can_tx
```

## CAN Dump

```
$ candump vcan0
```

## CAN / J1939

* https://www.csselectronics.com/pages/dbc-editor-can-bus-database

* Some scripts need a J1939 dbc on the `j1939` directory.
This dbc file can't be hosted on GitHub because of licensing.
