from trezorlib.client import get_default_client
from trezorlib.tools import parse_path
from trezorlib import ethereum,btc
class TrezorRobot(object):
    COINS = 'btc eth '

    def __init__(self):
        self._client = get_default_client()
    def get_address(self, coin ,path):
        if coin.strip() not in self.COINS:
            raise TrezorRobotError("Invalid coin '%s'." % coin)
        bip32_path = parse_path(path.strip())
        if coin.strip() == 'btc':
            address = btc.get_address(self._client, "Bitcoin", bip32_path, False)
        elif coin.strip() == 'eth':
            address = ethereum.get_address(self._client, bip32_path, False)
        return address

    def _error(self, expression):
        try:
            return str(eval(expression))
        except SyntaxError:
            raise TrezorRobotError('Invalid expression.')
        except ZeroDivisionError:
            raise TrezorRobotError('Division by zero.')

class TrezorRobotError(Exception):
    pass
