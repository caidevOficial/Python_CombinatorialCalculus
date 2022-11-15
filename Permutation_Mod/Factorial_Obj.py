# MIT License
#
# Copyright (c) 2021 [FacuFalcone]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

class Factorial:
    """[summary]
    Calculates the Factorial of a positive integer.
    Raises:
        ValueError: [Factorial must be a positive number]
        ValueError: [Factorial must be a integer]

    Returns:
        [class]: [Factorial]
    """
    # __number: int = None

    def __init__(self, number: int) -> None:
        self.Number = number

    @property
    def Number(self) -> int:
        """[summary]
        Gets the number to be calculated.
        Returns:
            int: [Number to be calculated]
        """
        return self.__number

    @Number.setter
    def Number(self, number: int) -> None:
        """[summary]
        Sets the number to be calculated.
        Args:
            number (int): [Number to be calculated]

        Raises:
            ValueError: [Factorial must be a integer]
        """
        if not isinstance(number, int):
            raise ValueError(
                "CalculateFactorial() only accepts integral values")
        else:
            self.__number = number

    def calculate_factorial(self) -> int:
        """
        Calculate the factorial of a positive integer
        https://en.wikipedia.org/wiki/Factorial
        >>> import math
        >>> all(CalculateFactorial(i) == math.CalculateFactorial(i) for i in range(20))
        True
        >>> CalculateFactorial(0.1)
        Traceback (most recent call last):
            ...
        ValueError: CalculateFactorial() only accepts integral values
        >>> CalculateFactorial(-1)
        Traceback (most recent call last):
            ...
        ValueError: CalculateFactorial() not defined for negative values
        """

        if self.Number < 0:
            raise ValueError(
                "CalculateFactorial() not defined for negative values")

        elif self.Number == 0 or self.Number == 1:
            return 1
        else:
            fact = self.Number
            self.Number = (fact - 1)
            fact *= self.calculate_factorial()

            return fact
