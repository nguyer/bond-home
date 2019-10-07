# Bond Home Library for Python

_A Python library for interacting with the Local API of a Bond Home Hub_
https://bondhome.io/

Local API Docs: http://docs-local.appbond.com/

## Installation

    $ pip3 install bond-home

## Usage

```python
from bond import Bond
import time

bond = Bond(bondIp='192.168.1.100', bondToken='abcdefghijklmnop')

bond.toggleLight('5842137d')
time.sleep(2)
bond.toggleLight('5842137d')
```
