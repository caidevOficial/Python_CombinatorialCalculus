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

from Permutation_Mod.Factorial_Obj import Factorial as F
from Message_Mod.Message_Obj import Message as M

class Variation:
    """[summary]
    Calculates the simple or compound Variation of 'n' elements of 'k' elements, being able to repeat.
    Returns:
        [class]: [Variation]
    """

    def __init__(self) -> None:
        pass

    def SimpleVariation(self) -> None:
        """
        Calculates the amount of variations of 'n' elements from 'k' elements.
        Order and nature are important.
        """
        mess = M()
        mess.createPrint(
            "Simple Variation #######", 
            "V(n, k) ######"
        )

        try:
            numberN = int(input("###### Value for n: ").strip())
            numberK = int(input("###### Value for k: ").strip())
            dividend = F(numberN).CalculateFactorial()
            divisor = F((numberN - numberK)).CalculateFactorial()
            
            mess.createPrint(
                f"Simple Variation of V({numberN}, {numberK}):",
                f"Formula: {numberN}! / ({numberN} - {numberK})!",
                f"Result: {dividend/divisor}"
            )
        except Exception as e:
            print(f"Error: {e}")

    def CompoundVariation(self) -> None:
        """
        It calculates the number of variations of 'n' elements of 'k' elements, being able to repeat.
        Order and nature are important
        """
        mess = M()
        mess.createPrint(
            "Compound Variation #######",
            "V'(n, k) ######"
        )
        try:
            number = int(input("###### Amount of total elements [n]: ").strip())
            exponent = int(input("###### Amount of element to take [k]: ").strip())
            
            mess.createPrint(
                f"Compound Variation of V'({number}, {exponent}):",
                f"Formula: {number}^{exponent}",
                f"Result: {pow(number,exponent)}"
            )
            
        except Exception as e:
            print(f"Error: {e}")
