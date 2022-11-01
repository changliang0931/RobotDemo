from trezorRobot import TrezorRobot,TrezorRobotError
from trezorlib.client import get_default_client
from trezorlib.tools import parse_path
from trezorlib import ethereum,btc
class TrezorRobotLibrary(object):
    """Test library for testing *Trezor* business logic.
    """
    def __init__(self):
        self._trezor = TrezorRobot()
        self._result = ''

    def get_address(self,coin,path,address):
        """Verifies trezor Derive address from path`.
        
        Example:
        | Get Address | eth | 44'/60'/0'/0/0 |  0x4213C85B259D95a3BeA639b3668604847F03283A  |
        | Get Address | btc |  44'/0'/0'/0/0 |  1NyK66tHd9RnWZzQWnq5A6QEo2e8LH8zxW | 
        """
        self._result = self._trezor.get_address(coin,path)
        if self._result != address:
            raise AssertionError('%s != %s' % (self._result, address))     
    def result_should_be(self, expected):
        """Verifies that the current result is ``expected``.

        Example:
        | Push Buttons     | 1 + 2 = |
        | Result Should Be | 3       |
        """
        if self._result != expected:
            raise AssertionError('%s != %s' % (self._result, expected))               
