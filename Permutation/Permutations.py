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


def SimplePermutation():
    """
    Calculates the simple permutation of n. Only the order is important.
    """
    print("\n###### Simple Permutation #######")
    try:
        print("Pn = n!")
        numberN = int(input("Value for n: "))
        try:
            fact = F(numberN)
            print(f"Simple Permutation of {numberN}:")
            print(f"Formula: {numberN}!")
            print(f"Result: {fact}")
        except Exception as e:
            print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


def ComposedPermutation():
    """
    Calculates the permutation according to the number of differents variables. Only the order is important.
    """
    sumCases = 0
    dividend = 1
    listCases = []
    formulaTop = "("
    formulaBot = ""
    print("\n###### Compound Permutation #######")
    try:
        print("P n1, n2 ..nn = (n1 + n2 + ..nn) / (n1)! (n2)! ..(nn)!")
        number = int(input("Amount of Variables: "))
        for case in range(1, number+1):
            listCases.append(int(input(f"Value for {case}° n: ")))
            sumCases += listCases[case-1]

        for case in listCases:
            dividend *= F(case)
            formulaBot += str(case) + "!"
            if listCases.index(case) == (len(listCases)-1):
                formulaTop += str(case) + ")!"
            else:
                formulaTop += str(case) + " + "

        print(f"Compound Permutation of {number} variables: ")
        print(f"Formula: {formulaTop} / {formulaBot}")
        print(f"Result: {F(sumCases) / dividend}")
    except Exception as e:
        print(f"Error: {e}")
