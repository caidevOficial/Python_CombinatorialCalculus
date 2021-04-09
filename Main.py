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
from Permutation import Permutations as P
from Combination import Combinations as C
from Variation import Variations as V


def PrintMenu() -> int:
    """
    Prints in console the menu of the app.
    """
    option = 0
    print("Select an option from the ones below")
    print("1 - Simple Permutation.\n2 - Simple Variation.\n3 - Simple Combination.")
    print("4 - Compound Permutation.\n5 - Compound Variation.\n6 - Compound Combination.")
    try:
        option = int(input("Your option: "))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        return option


def SelectOperation(option: int):
    """
    Receives an integer to do any of the 6 functions of the combinatorial calculus.
    """
    try:
        if option == 1:
            P.SimplePermutation()
        elif option == 2:
            V.SimpleVariation()
        elif option == 3:
            C.SimpleCombinatory()
        elif option == 4:
            P.ComposedPermutation()
        elif option == 5:
            V.CompoundVariation()
        elif option == 6:
            C.CompoundCombinatory()
        else:
            print("Invalid option selected, please try again.")
    except Exception as e:
        print(f"Error: {e}")


def CleanScreen():
    """
    Cleans the screen.
    """
    return lambda: os.system('cls')


def CombinatorialCalculus():
    appName = "Combinatorial Calculus"
    version = "v1.5.008"
    author = "Facu Falcone"
    continueExec = "y"

    while continueExec == 'y':
        print(f"\n## {appName} {version} by {author}. ##\n")
        print("#################################")

        SelectOperation(PrintMenu())

        print("#################################")
        print("Write Y to do another calculus or N to close the app.")
        continueExec = input("\nYour option (Y/N): ")
        continueExec = continueExec.lower()
        CleanScreen()()


if __name__ == '__main__':
    CombinatorialCalculus()
