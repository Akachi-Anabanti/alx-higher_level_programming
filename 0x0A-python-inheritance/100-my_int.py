#!/usr/bin/python3
# Author: Akachi Anabanti

"""supplies MyInt that inherits
the int class"""


class MyInt(int):
    """inherits the int class
    Reverses the == and != operator
    """

    def __eq__(self, other):
        """Returns False if 2 instances of MyInt are
        equal"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Returns False if 2 instances of MyInt are
        not equal"""
        return super().__eq__(other)
