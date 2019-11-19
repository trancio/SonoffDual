from machine import UART


class SonoffDual:
    def __init__(self):
        self.relay0 = False
        self.relay1 = False
        self.serial = UART(0, 19200)

    def _setRelays(self):
        r0 = 1 if self.relay0 else 0
        r1 = 2 if self.relay1 else 0
        buf = [0xA0, 0x04, r0 | r1, 0xA1]
        assert self.serial.write(bytes(buf)) == len(buf)

    def setOn(self, r):
        if r == 0:
            self.relay0 = True
        elif r == 1:
            self.relay1 = True
        self._setRelays()

    def setOff(self, r):
        if r == 0:
            self.relay0 = False
        elif r == 1:
            self.relay1 = False
        self._setRelays()

    def getStatus(self):
        r0 = 'on' if self.relay0 else 'off'
        r1 = 'on' if self.relay1 else 'off'
        return r0, r1
