from typing import List


class Statement:
    pass


class Select(Statement):
    def __init__(self, table: str, cols: list) -> None:
        """
        Represents an SQL `SELECT` statement
        """
        self.table = table
        self.cols = cols
