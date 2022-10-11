class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Creates a serial generator from a starting number"""
        self.start = start
        self.steps = 0

    def __repr__(self):
        """Gives a string representation of the class instance"""
        return f"<SerialGenerator start = {self.start} steps = {self.steps}>"

    def generate(self):
        """Returns the next number in the series starting at start num"""
        return_num = self.start + self.steps
        self.steps += 1
        return return_num

    def reset(self):
        """Resets the steps of the SerialGenerator instance"""
        self.steps = 0
