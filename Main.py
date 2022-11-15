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


def print_menu() -> int:
    """
    Prints in console the menu of the app.
    """
    mess = M()
    option = 0
    mess.print_messages(
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


def __select_operation(option: int) -> None:
    """
    Receives an integer to do any of the 6 functions of the combinatorial calculus.
    """
    perm = P()
    vari = V()
    comb = C()
    clean_screen()
    try:
        if option == 1:
            perm.do_simple_permutation()
        elif option == 2:
            vari.do_simple_variation()
        elif option == 3:
            comb.do_simple_combinatory()
        elif option == 4:
            perm.do_composed_permutation()
        elif option == 5:
            vari.do_compound_variation()
        elif option == 6:
            comb.do_compound_combinatory()
        else:
            print("###### Invalid option selected, please try again.")
    except Exception as e:
        print(f"Error: {e}")


def clean_screen():
    """
    Cleans the screen.
    """
    return lambda: os.system('cls')


def do_combinatorial_calculus():
    appName = "Combinatorial Calculus"
    version = "v1.5.13"
    author = "Facu Falcone"
    continueExec = "y"
    mess = M()

    while continueExec == 'y':
        mess.print_messages(
            f"{appName}",
            f"{version}",
            f"by {author}."
        )

        __select_operation(print_menu())

        print("###### Write Y to do another calculus or N to close the app.")
        continueExec = input("###### Your option (Y/N): ").lower()
        clean_screen()


if __name__ == '__main__':
    do_combinatorial_calculus()
