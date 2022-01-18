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


class Combination:
    """[summary]
    Calculates the simple or compound combination of K elements from N total elements.
    Returns:
        [class]: [Combination]
    """

    __numberN = None
    __numberK = None

    def __init__(self) -> None:
        pass

    def SimpleCombinatory(self) -> None:
        """
        Calculate the simple combination of K elements from N total elements.
        Only Nature is important.
        """
        mess = M()
        try:
            mess.createPrint(
                "Simple Combinatory #######",
                "C(n, k) ######"
            )

            numberN = int(input("###### Value for n: ").strip())
            numberK = int(input("###### Value for k: ").strip())
            self.set_numbers(numberN, numberK)

            n = F(self.get_numberN()).CalculateFactorial()
            k = F(numberK).CalculateFactorial() * F((numberN - numberK)).CalculateFactorial()

            mess.createPrint(
                f"Simple Combination of C({numberN},{numberK}): ",
                f"Formula: {numberN}! / ( {numberK}! * ({numberN-numberK})! )",
                f"Result: {n/k}"
            )

        except Exception as e:
            mess.createPrint(f"Error: {e}")

    def CompoundCombinatory(self) -> None:
        """
        Calculate the simple combination of K elements from N total elements, being able to repeat.
        Only Nature is important.
        """
        mess = M()
        try:
            mess.createPrint(
                "Compound Combinatory #######", 
                "C(n, k) ######"
            )

            numberN = int(input("###### Value for n: ").strip())
            numberK = int(input("###### Value for k: ").strip())
            self.set_numbers(numberN, numberK)

            n = numberN + numberK - 1
            k = F(numberN - 1).CalculateFactorial() * F(numberK).CalculateFactorial()

            mess.createPrint(
                f"Compound Combination of C({numberN},{numberK}): ",
                f"Formula: ({numberN} + {numberK} - 1) / ({numberN} - 1)!{numberK}!",
                f"Result: {F(n).CalculateFactorial()/k}"
            )

        except Exception as e:
            print(f"Error: {e}")

    def set_numbers(self, numberN, numberK) -> None:
        """[summary]
        Sets the numbers of that the class will use.
        Args:
            numberN (int): [Represents the total number of elements]
            numberK (int): [Represents the number of elements that will be selected]
        """
        self.set_numberN(numberN)
        self.set_numberK(numberK)

    def set_numberN(self, numberN) -> None:
        """[summary]
        Sets the N number of that the class will use.
        Args:
            numberN (int): [Represents the total number of elements]

        Raises:
            ValueError: [If the value is not an integer]
        """
        if isinstance(numberN, int):
            self.__numberN = numberN
        else:
            raise ValueError("The value must be an integer")

    def set_numberK(self, numberK) -> None:
        """[summary]
        Sets the K number of that the class will use.
        Args:
            numberN (int): [Represents the number of elements that will be selected]

        Raises:
            ValueError: [If the value is not an integer]
        """
        if isinstance(numberK, int):
            self.__numberK = numberK
        else:
            raise ValueError("The value must be an integer")

    def get_numberN(self) -> int:
        """[summary]
        Gets the N number of that the class will use.
        Returns:
            [int]: [Represents the total number of elements]
        """
        return self.__numberN

    def get_numberK(self) -> int:
        """[summary]
        Gets the K number of that the class will use.
        Returns:
            [int]: [Represents the number of elements that will be selected]
        """
        return self.__numberK
