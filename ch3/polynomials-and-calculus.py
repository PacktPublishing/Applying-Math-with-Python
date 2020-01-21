
class Polynomial:
    """Basic polynomial class"""

    def __init__(self, coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return f"Polynomial({repr(self.coeffs)})"

    def __call__(self, x):
        return sum(coeff*x**i for i, coeff in enumerate(self.coeffs))

    def differentiate(self):
        """Differentiate the polynomial and return the derivative"""
        coeffs = [i*c for i, c in enumerate(self.coeffs[1:], start=1)]
        return Polynomial(coeffs)

    def integrate(self, constant=0):
        """Integrate the polynomial and return the integral"""
        coeffs = [float(constant)]
        coeffs += [c/i for i, c in enumerate(self.coeffs, start=1)]
        return Polynomial(coeffs)

