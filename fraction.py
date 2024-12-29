class Fraction:

    def __init__(self,numerator=1.0,denominator=1.0):

        if isinstance(numerator,int) and isinstance(denominator,int):
            self.numerator = numerator
            self.denominator = denominator
        else:
            raise ValueError('Numerator and Denominator should be integers')

        # if self.denominator == 0:

           #  raise ValueError("Denominator value should be not zero")
        

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'
    
    def __add__(self,other):

        temp_num = (self.numerator * other.denominator) + (other.denominator * self.numerator)
        temp_den = (self.numerator * other.denominator)

        new_result  = Fraction(temp_num,temp_den)

        return new_result
    
    def __sub__(self,other):

        temp_num = (self.numerator * other.denominator) - (other.denominator * self.numerator)
        temp_den = (self.numerator * other.denominator)

        new_result  = Fraction(temp_num,temp_den)

        return new_result
    
    def __mul__(self,other):

        temp_num = self.numerator * other.numerator
        temp_den = self.denominator * other.denominator

        new_result = Fraction(temp_num,temp_den)

        return new_result
    
    def __truediv__(self,other):

        temp_num = self.numerator * other.denominator
        temp_den = self.denominator * other.numerator

        new_result = Fraction(temp_num,temp_den)

        return new_result

    




