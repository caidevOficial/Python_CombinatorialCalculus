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

from Permutation_Mod.Factorial_Obj import Factorial as Facto
from Message_Mod.Message_Obj import Message as M


class Permutation:
    """[summary]
    Calculates the simple or compound permutation of n.
    Returns:
        [class]: [Permutation]
    """

    __PERM_MAIN: str = "P' n1, n2 ..nn = "
    __PERM_TOP:str = " (n1 + n2 + ..nn) "
    __PERM_MID: str = '_'*len(__PERM_TOP)
    __PERM_BOT:str = "(n1)! (n2)!..(nn)!"

    def __init__(self):
        pass

    @property
    def PermMain(self):
        return self.__PERM_MAIN
    
    @property
    def PermTop(self):
        return self.__PERM_TOP

    @property
    def PermMid(self):
        return self.__PERM_MID

    @property
    def PermBot(self):
        return self.__PERM_BOT

    def SimplePermutation(self):
        """
        Calculates the simple permutation of n. Only the order is important.
        """
        mess = M()
        try:
            mess.createPrint(
                'Simple Permutation #######', 
                "Pn = n! ######"
            )

            numberN = int(input("###### Value for n: ").strip())
            try:
                factorial = Facto(numberN)
                fact = factorial.CalculateFactorial()
                mess.createPrint(
                    f"Simple Permutation of {numberN}: ", 
                    f"Formula: {numberN}!", 
                    f"Result: {fact}"
                )

            except Exception as e:
                print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def ComposedPermutation(self):
        """
        Calculates the permutation according to the number of differents variables. Only the order is important.
        """
        sumCases = 0
        dividend = 1
        listCases = []
        mess = M()
        space_msg = " "*len(self.PermMain)
        mess.createPrint(
            'Composed Permutation #######',
            f'{self.PermMain}{self.PermTop} ######',
            f'{space_msg}{self.PermMid} ######',
            f'{space_msg}{self.PermBot} ######'
        )

        try:
            number = int(input("###### Amount of Variables: ").strip())
            for case in range(1, number+1):
                listCases.append(int(input(f"###### Value for {case}° n: ").strip()))
                sumCases += listCases[case-1]

            factorial = Facto(sumCases)
            f_top, f_mid, f_bot = self.__create_formula_str(listCases, number, dividend)
            mess.createPrint(
                f"Composed Permutation of {number} variables: ",
                "Formula:", f"{f_top}", f"{f_mid}", f"{f_bot}",
                f"Result: {factorial.CalculateFactorial() / dividend}"
            )

        except Exception as e:
            print(f"Error: {e}")

    def __create_formula_str(self, list_cases: list, number: int, dividend: int) -> str:
        formulaTop = "("
        formulaBot = " "
        for case in list_cases:
                factorial = Facto(case)
                dividend *= factorial.CalculateFactorial()
                formulaBot += f"{case}!  "

                if list_cases.index(case) == (len(list_cases)-1):
                    formulaTop += f"{case})!"
                else:
                    formulaTop += f"{case} + "

        middle = "-"*(4*number)
        return formulaTop, middle, formulaBot
