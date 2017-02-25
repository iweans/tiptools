#! /usr/bin/env python3
# coding: utf-8

class Spinner:

    def __init__(self, msg):
        import threading
        import itertools

        self._infinite_loop = itertools.cycle('|/-\\')
        self._signal = True
        self._thread = threading.Thread(target=self._spin, args=(msg,))
        self.run = self._thread.start

    def _spin(self, msg):
        import sys
        import time

        write, flush = sys.stdout.write, sys.stdout.flush
        for char in self._infinite_loop:
            status = char + ' ' + msg
            write(status); flush()
            write('\x08'*len(status))
            time.sleep(.1)
            if not self._signal:
                break
        write(' '*len(status)+'\x08'*len(status))

    def stop(self):
        self._signal = False
        return self._thread.join()
    