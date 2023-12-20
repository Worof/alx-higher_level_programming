#!/usr/bin/python3
"""Module 100-singly_linked_list

This module contains the definitions of the classes Node and SinglyLinkedList which together create a singly linked list with sorted insert functionality.
"""

class Node:
    """Defines a node of a singly linked list.

    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node): The next node in the linked list.
    """

    def __init__(self, data, next_node=None):
        """Initializes the Node.

        Args:
            data (int): The data to store in the node.
            next_node (Node, optional): The next node in the linked list. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data of the node.

        Returns:
            int: The data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data of the node.

        Args:
            value (int): The data to set in the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next node in the linked list.

        Returns:
            Node: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node in the linked list.

        Args:
            value (Node): The node to set as the next node.

        Raises:
            TypeError: If value is not a Node object and is not None.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list.

    Attributes:
        __head (Node): The head of the linked list.
    """

    def __init__(self):
        """Initializes the SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the list at the correct sorted position.

        Args:
            value (int): The data value to insert into the list.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Defines the print() representation of the SinglyLinkedList.

        Returns:
            str: The string representation of the linked list.
        """
        values = []
        current = self.__head
        while current:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)
