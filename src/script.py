"""Model to represent a script"""
from dataclasses import dataclass


@dataclass
class Chapter:
    """Model to represent a chapter"""
    title: str
    description: str
    code: str


@dataclass
class Script:
    """Model to represent a script"""
    chapters: list[Chapter]
