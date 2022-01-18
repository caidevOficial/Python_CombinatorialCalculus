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

import os

from Combination_Mod.Combination_Obj import Combination as C
from Permutation_Mod.Permutation_Obj import Permutation as P
from Variation_Mod.Variations_Obj import Variation as V
from Message_Mod.Message_Obj import Message as M


def PrintMenu() -> int:
    """
    Prints in console the menu of the app.
    """
    mess = M()
    option = 0
    mess.createPrint(
        "Select an option from the ones below",
        "1 - Simple Permutation.", 
        "2 - Simple Variation.", 
        "3 - Simple Combination.",
        "4 - Compound Permutation.", 
        "5 - Compound Variation.", 
        "6 - Compound Combination."
    )

    try:
        option = int(input("###### Your option: ").strip())
    except Exception as e:
        print(f"Error: {e}")
    finally:
        return option


def SelectOperation(option: int) -> None:
    """
    Receives an integer to do any of the 6 functions of the combinatorial calculus.
    """
    perm = P()
    vari = V()
    comb = C()
    CleanScreen()
    try:
        if option == 1:
            perm.SimplePermutation()
        elif option == 2:
            vari.SimpleVariation()
        elif option == 3:
            comb.SimpleCombinatory()
        elif option == 4:
            perm.ComposedPermutation()
        elif option == 5:
            vari.CompoundVariation()
        elif option == 6:
            comb.CompoundCombinatory()
        else:
            print("###### Invalid option selected, please try again.")
    except Exception as e:
        print(f"Error: {e}")


def CleanScreen():
    """
    Cleans the screen.
    """
    return lambda: os.system('cls')


def CombinatorialCalculus():
    appName = "Combinatorial Calculus"
    version = "v1.5.10"
    author = "Facu Falcone"
    continueExec = "y"
    mess = M()

    while continueExec == 'y':
        mess.createPrint(
            f"{appName}",
            f"{version}",
            f"by {author}."
        )

        SelectOperation(PrintMenu())

        print("###### Write Y to do another calculus or N to close the app.")
        continueExec = input("###### Your option (Y/N): ")
        continueExec = continueExec.lower()
        CleanScreen()


if __name__ == '__main__':
    CombinatorialCalculus()
