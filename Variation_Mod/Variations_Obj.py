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
        self.__number_n = 0
        self.__number_k = 0
        self.__dividend = 0
        self.__divisor = 0
        self.__formula_top = ''
        self.__formula_mid = ''
        self.__formula_bot = ''

    @property
    def Number_N(self) -> int:
        """[summary]
        Getter for the number of elements of the variation.
        Returns:
            int: [The number of elements of the variation]
        """
        return self.__number_n
    
    @property
    def Number_K(self) -> int:
        """[summary]
        Getter for the number of elements that want take from \n
        the total elements of the variation.
        Returns:
            int: [The number of elements that want take from \n
            the total elements of the variation]"""
        return self.__number_k
    
    @property
    def Dividend(self) -> int:
        """[summary]\n
        Getter for the dividend of the formula.\n
        Returns:
            int: [The dividend of the formula]
        """
        return self.__dividend

    @property
    def Divisor(self) -> int:
        """[summary]\n
        Getter for the divisor of the formula.\n
        Returns:
            int: [The divisor of the formula]
        """
        return self.__divisor
    
    @property
    def Formula_Top(self) -> str:
        """[summary]\n
        Getter for the top formula as a string.\n
        Returns:
            str: [The top formula as a string]
        """
        return self.__formula_top
    
    @property
    def Formula_Mid(self) -> str:
        """[summary]\n
        Getter for the middle formula as a string.\n
        Returns:
            str: [The middle formula as a string]
        """
        return self.__formula_mid

    @property
    def Formula_Bot(self) -> str:
        """[summary]\n
        Getter for the bottom formula as a string.\n
        Returns:
            str: [The bottom formula as a string]
        """
        return self.__formula_bot

    @Number_N.setter
    def Number_N(self, numberN: int) -> None:
        """[summary]\n
        Setter for the number of elements of the variation.\n
        Arguments:
            numberN {int} -- [The number of elements of the variation]
        """
        self.__number_n = numberN

    @Number_K.setter
    def Number_K(self, numberK: int) -> None:
        """[summary]\n
        Setter for the number of elements that want take from \n
        the total elements of the variation.\n
        Arguments:
            numberK {int} -- [The number of elements that want take from \n
            the total elements of the variation]
        """
        self.__number_k = numberK
    
    @Dividend.setter
    def Dividend(self, dividend: int) -> None:
        """[summary]\n
        Setter for the dividend of the formula.\n
        Arguments:
            dividend {int} -- [The dividend of the formula]
        """
        self.__dividend = dividend
    
    @Divisor.setter
    def Divisor(self, divisor: int) -> None:
        """[summary]\n
        Setter for the divisor of the formula.\n
        Arguments:
            divisor {int} -- [The divisor of the formula]
        """
        self.__divisor = divisor
    
    @Formula_Top.setter
    def Formula_Top(self, formula_top: str) -> None:
        """[summary]\n
        Setter for the top formula as a string.\n
        Arguments:
            formula_top {str} -- [The top formula as a string]
        """
        self.__formula_top = formula_top
    
    @Formula_Mid.setter
    def Formula_Mid(self, formula_mid: str) -> None:
        """[summary]\n
        Setter for the middle formula as a string.\n
        Arguments:
            formula_mid {str} -- [The middle formula as a string]
        """
        self.__formula_mid = formula_mid

    @Formula_Bot.setter
    def Formula_Bot(self, formula_bot: str) -> None:
        """[summary]\n
        Setter for the bottom formula as a string.\n
        Arguments:
            formula_bot {str} -- [The bottom formula as a string]
        """
        self.__formula_bot = formula_bot

    def __create_spaces_by_guide(self, formu: str, guide: str)-> str:
        """
        Create spaces for the print of the top formula.
        """
        amount_spaces = len(guide) - len(formu)
        total_spaces = int(amount_spaces / 2)
        final_string = f'{" "*total_spaces}{formu}!{" "*total_spaces}'
        return final_string

    def do_simple_variation(self) -> None:
        """
        Calculates the amount of variations of 'n' elements from 'k' elements.
        Order and nature are important.
        """
        mess = M()
        mess.print_messages(
            "Simple Variation #######", 
            "V(n, k) ######"
        )

        try:
            self.Number_N = int(input("###### Value for n: ").strip())
            self.Number_K = int(input("###### Value for k: ").strip())
            self.Dividend = F(self.Number_N).calculate_factorial()
            self.Divisor = F((self.Number_N - self.Number_K)).calculate_factorial()
            self.Formula_Bot = f'({self.Number_N} - {self.Number_K})!'
            self.Formula_Mid = '_' * len(self.Formula_Bot)
            self.Formula_Top = self.__create_spaces_by_guide(str(self.Number_N), str(self.Formula_Mid))


            mess.print_messages(
                f"Simple Variation of V({self.Number_N}, {self.Number_K}):",
                f"Formula:",
                f"{self.Formula_Top}",
                f"{self.Formula_Mid}",
                f"{self.Formula_Bot}",
                f"Result: {self.Dividend / self.Divisor}"
            )
        except Exception as e:
            print(f"Error: {e}")

    def do_compound_variation(self) -> None:
        """
        It calculates the number of variations of 'n' elements of 'k' elements, being able to repeat.
        Order and nature are important
        """
        mess = M()
        mess.print_messages(
            "Compound Variation #######",
            "V'(n, k) ######"
        )
        try:
            self.Number_N = int(input("###### Amount of total elements [n]: ").strip())
            self.Number_K = int(input("###### Amount of element to take [k]: ").strip())
            self.Formula_Top = f'{self.Number_N}^{self.Number_K}'

            mess.print_messages(
                f"Compound Variation of V'({self.Number_N}, {self.Number_K}):",
                f"Formula: {self.Formula_Top}",
                f"Result: {pow(self.Number_N, self.Number_K)}"
            )
        except Exception as e:
            print(f"Error: {e}")
