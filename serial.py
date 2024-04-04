"""Python serial number generator."""

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
        """
        Initialize SerialGenerator 

        Args:
            start (int) is the starting value for the serial numbers
        """
        self.start = start
        self.current = start

    def __repr__(self):
        """
        Returns a string representation of SerialGenerator
        """
        return f"SerialGenerator(start={self.start}, durrent={self.current})"
    
    def generate(self):
        """
        Generate next serial number

        Returns:
            int of next serial number
        """
        current_value = self.current
        self.current += 1
        return current_value
    
    def reset(self):
        """
        Resets serial number starting value
        """
        self.current = self.start

