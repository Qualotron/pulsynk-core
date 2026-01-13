from sx126x import SX126x
import time

class SX126xDriver:
    def __init__(
        self,
        frequency=868_000_000,
        cs=8,
        busy=22,
        reset=27,
        dio1=17,
    ):
        self.lora = SX126x(
            cs=cs,
            busy=busy,
            reset=reset,
            dio1=dio1,
            freq=frequency,
        )

        self.lora.begin()
        
