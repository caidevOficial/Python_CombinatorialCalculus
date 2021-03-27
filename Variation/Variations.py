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

from Permutations.Factorial import Factorial as F


def SimpleVariation():
    """
    Calculates the amount of variations of 'n' elements from 'k' elements.
    Order and nature are important.
    """
    print("\n###### Simple Variation #######")
    try:
        print("V(n, k)")
        numberN = int(input("Value for n: "))
        numberK = int(input("Value for k: "))
        dividend = F(numberN)
        divisor = F((numberN - numberK))
        print(f"Simple Variation of V({numberN}, {numberK}):")
        print(f"Formula: {numberN}! / ({numberN} - {numberK})!")
        print(f"Result: {dividend/divisor}")
    except Exception as e:
        print(f"Error: {e}")


def CompoundVariation():
    """
    It calculates the number of variations of 'n' elements of 'k' elements, being able to repeat.
    Order and nature are important
    """
    print("\n###### Compound Variation #######")
    try:
        print("V'(n, k)")
        number = int(input("Amount of total elements [n]: "))
        exponent = int(input("Amount of element to take [k]: "))
        print(f"Compound Variation V'({number}, {exponent}):")
        print(f"Formula: {number}^{exponent}")
        print(f"Result: {pow(number,exponent)}")
    except Exception as e:
        print(f"Error: {e}")
