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

    def __init__(self) -> None:
        self.__numberN = None
        self.__numberK = None
        self.__formula_top: str = None
        self.__formula_bot: str = None
        self.__formula_mid: str = None

    @property
    def Number_N(self) -> int:
        """[summary]\n
        Gets the total number of elements.
        Returns:
            int: [Represents the total number of elements]
        """
        return self.__numberN

    @property
    def Number_K(self) -> int:
        """[summary]\n
        Gets the number of elements that will be selected.
        Returns:
            int: [Represents the number of elements that will be selected]
        """
        return self.__numberK
    
    @property
    def Formula_Top(self) -> str:
        """[summary]\n
        Gets the formula top.
        Returns:
            str: [Represents the formula top]
        """
        return self.__formula_top
    
    @property
    def Formula_Bot(self) -> str:
        """[summary]\n
        Gets the formula bottom.
        Returns:
            str: [Represents the formula bottom]
        """
        return self.__formula_bot
    
    @property
    def Formula_Mid(self) -> str:
        """[summary]\n
        Gets the formula middle.
        Returns:
            str: [Represents the formula middle]
        """
        return self.__formula_mid

    @Number_N.setter
    def Number_N(self, numberN: int) -> None:
        """[summary]\n
        Sets the total number of elements.\n
        Args:
            numberN (int): [Represents the total number of elements]\n
        Raises:
            ValueError: [If the value is not an integer]
        """
        if isinstance(numberN, int):
            self.__numberN = numberN
        else:
            raise ValueError("The value must be an integer")
    
    @Number_K.setter
    def Number_K(self, numberK: int) -> None:
        """[summary]\n
        Sets the number of elements that will be selected.\n
        Args:
            numberK (int): [Represents the number of elements that will be selected]
        Raises:
            ValueError: [If the value is not an integer]
        """
        if isinstance(numberK, int):
            self.__numberK = numberK
        else:
            raise ValueError("The value must be an integer")

    @Formula_Top.setter
    def Formula_Top(self, formula_top: str) -> None:
        """[summary]\n
        Sets the formula top.\n
        Args:
            formula_top (str): [Represents the formula top]
        Raises:
            TypeError: [If the value is not a string]
        """
        if isinstance(formula_top, str):
            self.__formula_top = formula_top
        else:
            raise TypeError("The value must be a string")

    @Formula_Bot.setter
    def Formula_Bot(self, formula_bot: str) -> None:
        """[summary]\n
        Sets the formula bottom.\n
        Args:
            formula_bot (str): [Represents the formula bottom]
        Raises:
            TypeError: [If the value is not a string]
        """
        if isinstance(formula_bot, str):
            self.__formula_bot = formula_bot
        else:
            raise TypeError("The value must be a string")
    
    @Formula_Mid.setter
    def Formula_Mid(self, formula_mid: str) -> None:
        """[summary]\n
        Sets the formula middle.\n
        Args:
            formula_mid (str): [Represents the formula middle]
        Raises:
            TypeError: [If the value is not a string]
        """
        if isinstance(formula_mid, str):
            self.__formula_mid = formula_mid
        else:
            raise TypeError("The value must be a string")

    def __create_spaces_by_guide(self, formu: str, guide: str)-> str:
        """
        Create spaces for the print of the top formula.
        """
        amount_spaces = len(guide) - len(formu)
        total_spaces = int(amount_spaces / 2)
        final_string = f'{" "*total_spaces}{formu}!{" "*total_spaces}'
        return final_string

    def __input_numbers(self) -> None:
        """[summary]\n
        Gets the numbers that the class will use.
        """
        self.Number_N = int(input("###### Value for n: ").strip())
        self.Number_K = int(input("###### Value for k: ").strip())

    def do_simple_combinatory(self) -> None:
        """
        Calculate the simple combination of K elements from N total elements.
        Only Nature is important.
        """
        mess = M()
        try:
            mess.print_messages(
                "Simple Combinatory #######",
                "C(n, k) ######"
            )

            self.__input_numbers()

            n = F(self.Number_N).calculate_factorial()
            k = F(self.Number_K).calculate_factorial() * F((self.Number_N - self.Number_K)).calculate_factorial()

            self.Formula_Bot = f'( {self.Number_K}! * ({self.Number_N-self.Number_K})! )'
            self.Formula_Mid = '_' * len(self.Formula_Bot)
            self.Formula_Top = self.__create_spaces_by_guide(str(self.Number_N), self.Formula_Mid)

            mess.print_messages(
                f"Simple Combination of C({self.Number_N},{self.Number_K}): ",
                f"Formula:",
                f'{self.Formula_Top}',
                f'{self.Formula_Mid}',
                f'{self.Formula_Bot}',
                f"Result: {n/k}"
            )

        except Exception as e:
            mess.print_messages(f"Error: {e}")

    def do_compound_combinatory(self) -> None:
        """
        Calculate the simple combination of K elements from N total elements, being able to repeat.
        Only Nature is important.
        """
        mess = M()
        try:
            mess.print_messages(
                "Compound Combinatory #######", 
                "C(n, k) ######"
            )

            self.__input_numbers()
            
            n: int = self.Number_N + (self.Number_K - 1)
            k: int = F(self.Number_N - 1).calculate_factorial() * F(self.Number_K).calculate_factorial()

            self.Formula_Top = f'({self.Number_N} + {self.Number_K} - 1)'
            self.Formula_Mid = '_' * len(self.Formula_Top)
            self.Formula_Bot = f'({self.Number_N} - 1)! {self.Number_K}!'

            mess.print_messages(
                f"Compound Combination of C({self.Number_N},{self.Number_K}): ",
                f"Formula:",
                f'{self.Formula_Top}',
                f'{self.Formula_Mid}',
                f'{self.Formula_Bot}',
                f"Result: {F(n).calculate_factorial()/k}"
            )

        except Exception as e:
            print(f"Error: {e}")
