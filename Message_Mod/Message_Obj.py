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

class Message:
    """[summary]
    Class that handle the messages.
    Returns:
        [class]: [Message]
    """
    
    __PREFIX: str = '###### '

    def __init__(self) -> None:
        self.__messages = list[str]()
    
    @property
    def Message(self) -> list:
        """[summary]
        Returns the list of messages.
        Returns:
            list: [The list of messages.]
        """
        return self.__getMessages()
    
    @Message.setter
    def Message(self, text: str) -> None:
        """[summary]
        Adds a message into the list.
        Args:
            text (str): [The message to be added.]
        """
        self.__getMessages().append(text)
    
    def get_bigger_message(self) -> int:
        """[summary]
        Returns the bigger message.
        Returns:
            str: [The bigger message.]
        """
        return len(max(self.__getMessages(), key=len)) + len(self.__PREFIX)

    def __print_symbols(self) -> str:
        """[summary]
        Prints the symbols.
        Returns:
            str: [The symbols.]
        """
        max_amount: int = self.get_bigger_message()
        symbols: str = '#'
        for i in range(max_amount):
            symbols += '#'
        return symbols

    def __printMessage(self, amount: int) -> None:
        """[summary]
        Prints the messages 'amount' times.
        Args:
            amount (int): [The amount of times that must print the messages.]
        """
        symbols: str = self.__print_symbols()
        print(f'\n{symbols}')
        for i in range(amount):
            print(f"{self.__PREFIX}{self.__getMessages()[i]}")
        print(symbols)
    
    def __getMessages(self) -> list:
        """[summary]
        Returns the list of messages.
        Returns:
            list: [The list of messages.]
        """
        return self.__messages

    def __delMessages(self) -> None:
        """[summary]
        Deletes all the messages from the list.
        """
        self.__messages.clear()
    
    def print_messages(self, *args) -> None:
        """[summary]
        Creates a message and prints it.
        """
        self.__delMessages()
        for arg in args:
            self.Message = arg
        self.__printMessage(len(args))
