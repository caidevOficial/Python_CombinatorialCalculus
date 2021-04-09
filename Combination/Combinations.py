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

from Permutation.Factorial import Factorial as F


def SimpleCombinatory():
    """
    Calculate the simple combination of K elements from N total elements.
    Only Nature is important.
    """
    try:
        print("\n###### Simple Combinatory #######")
        print("###### C(n, k) ######")
        numberN = int(input("Value for n: "))
        numberK = int(input("Value for k: "))
        n = F(numberN)
        k = F(numberK) * F((numberN - numberK))
        print(f"Simple Combination of C({numberN},{numberK}): ")
        print(f"Formula: {numberN}! / ( {numberK}! * ({numberN-numberK})! )")
        print(f"Result: {n/k}")
    except Exception as e:
        print(f"Error: {e}")


def CompoundCombinatory():
    """
    Calculate the simple combination of K elements from N total elements, being able to repeat.
    Only Nature is important.
    """
    print("\n###### Compound Combinatory #######")
    try:
        print("###### C'(n, k) ######")
        numberN = int(input("Value for n: "))
        numberK = int(input("Value for k: "))
        n = numberN + numberK - 1
        k = F(numberN - 1) * F(numberK)
        print(f"Compound Combination of C'({numberN},{numberK}):")
        print(f"Formula: ({numberN} + {numberK} - 1) / ({numberN} - 1)!{numberK}!")
        print(f"Result: {F(n)/k}")
    except Exception as e:
        print(f"Error: {e}")
