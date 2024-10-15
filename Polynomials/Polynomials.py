class Polynomial:
    def __init__(self,coefs):

        self.coefficients = coefs

    def degree(self):

        return len(self.coefficients)-1
    
# Converting polynomial to a string
    def __str__(self):

        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))

        if self.degree() and coefs[1]:
            terms.append(f"{''if coefs[1] == 1 else coefs[1]}x")
        terms += [f"{'' if c==1 else c}x^{d}" 
                  for d,c in enumerate(coefs[2:], start = 2) if c]  # by default enumerate starts from 0.
        
        return " + ".join(reversed(terms)) or "0"
    
# equality

    def __eq__(self, other):
        return self.coefficients == other.coefficients 
    
# addition

    def __add__(self,other):
        if isinstance(other,Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a+b for a,b in zip(self.coefficients,other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]
            return Polynomial(coefs)
        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,) + self.coefficients[1:])
        
        # exception
        else: 
            return NotImplemented
    
    def __radd__(self,other):
        return self + other 
