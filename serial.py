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
        """Construct the class variables"""
        self.start = start -1
        self.serial_number = self.start
        
    def __repr__(self):
        """Description of the class"""
        return f'Incremental serial numbers starting at: {self.start +1}. Current number is: {self.serial_number}.'
    
    def generate(self):
        """Generate the next incremental sequence number"""
        self.serial_number += 1
        return self.serial_number
    
    def reset(self):
        """Reset the serial number back to its initial starting value"""
        self.serial_number = self.start
