import pdb

class ComplexNumber(object):
    def __init__(self, real, imaginary):
        if not isinstance(real, (int, float)) or not isinstance(imaginary, (int, float)):
            raise RuntimeError("The real or imaginary components must be numbers.")
        self.real = real
        self.imag = imaginary

    def conjugate(self):
        return ComplexNumber(self.real, -1 * self.imag)
    
    def __abs__(self):
        return (self.real**2 + self.imag**2)**0.5
    
    def __lt__(self, other):
        if abs(self) < abs(other):
            return True
        else:
            return False
        
    def __gt__(self, other):
        if abs(self) > abs(other):
            return True
        else:
            return False
        
    def __eq__(self, other):
        if (self.real == other.real) and (self.imag == other.imag):
            return True
        else:
            return False
        
    def __ne__(self, other):
        return not self == other

# Your code for debugging
mycn = ComplexNumber(2, "Hi!")  # This should trigger an error
othercn = ComplexNumber(3, 1)
mycn > othercn  # This will cause the comparison to fail due to the error in the fi
