#!/usr/bin/env python3
"""
`morse` implementation

@authors: Aidan brook
@version: 2021.4
"""

from typing import Union
from pythonds3.trees import BinaryTree 



class Coder:
    """Morse code encoder and decoder"""

    def __init__(self, file_in: str):
        self.morse_tree = BinaryTree("")

        with open(file_in) as morse_file:
            for line in morse_file:
                letter, code = line.split()
                self.follow_and_insert(code, letter)

    def follow_and_insert(self, code_str: str, letter: str) -> None:
        """
        Follow the tree and insert a letter

        @param code_str: morse code sequence
        @param letter: letter corresponding to the `code_str`
        """

        currentPoint = self.morse_tree

        for i in code_str:
            if i == '.':
                if currentPoint.get_child_left() is None:
                    currentPoint.set_child_left(BinaryTree(""))
                currentPoint = currentPoint.get_child_left()
            if i == '-':
                if currentPoint.get_child_right() is None:
                    currentPoint.set_child_right(BinaryTree(""))            
                currentPoint = currentPoint.get_child_right()

        currentPoint.set_root_val(letter)
        
            
        

    def follow_and_retrieve(self, code_str: str) -> str:
        """
        Follow the tree and retrieve a letter

        @param code_str: morse code sequence
        @return letter corresponding to the `code_str`
        @raises ValueError if the code is not found
        """

        currentPoint = self.morse_tree

        for i in code_str:
            if i == '.':
                if currentPoint.get_child_left() is None:
                    raise ValueError("No Value")
                currentPoint = currentPoint.get_child_left()
            if i == '-':
                if currentPoint.get_child_right() is None:
                    raise ValueError("None")           
                currentPoint = currentPoint.get_child_right()

        currentPoint.get_root_val()

    def find_path(self, tree: BinaryTree, letter: str, path: str) -> Union[bool, str]:
        """
        Find a path to the letter
        Encoder's helper function

        @param tree: Morse tree
        @param letter: letter to encode
        @param path: path to the letter
        @return path to the letter
        """
        

    def encode(self, msg: str) -> str:
        """
        Encode a message
        
        @param msg: text to encode
        @return Morse code representation of the the message
        """
        

    def decode(self, code: str) -> str:
        """
        Decode a message

        @param code: Morse code sequence to decode
        @return text corresponding to the code
        """
        
