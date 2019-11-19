##MicroPython relay module for Sonoff Dual

Simple module for original Sonoff Dual

**Functions**

SonoffDual.setOn(relay)   # relay: 0 or 1
SonoffDual.setOff(relay)  # relay: 0 or 1
Sonoffdual.getStatus()    # return a list, e.g. ['on', 'off']

**Example**

```
from sonoffdual import SonoffDual

relay = SonoffDual()

relay.setOn(0)
relay.setOn(1)
print(relay.getStatus())
relay.setOff(0)
relay.setOff(1)
print(relay.getStatus()[0])
```
