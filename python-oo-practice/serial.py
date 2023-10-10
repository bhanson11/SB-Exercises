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

    def __init__(self, start=0):
        """Create a new generator starting at start or 0 as default"""
        self.start = self.next = start
    
    def __repr__(self):
        """Make a representation so it tells you start and next of serial generator"""
        return f"<SerialGenerator start={self.start} next={self.next}"
    
    def generate(self):
        """Generate the next sequential number"""
        self.next = self.next + 1
        return self.next - 1
    
    def reset(self):
        """Reset to start"""
        self.next = self.start