from enum import Enum


class UnifiedExceptionLevel(Enum):
    Error = 0
    Warning = 1
    Notice = 2


class UnifiedException:

    def __init__(self, code: str, level: UnifiedExceptionLevel, line: int, column: int, file: str, msg: str) -> None:
        self.code: str = code.upper()
        self.level: UnifiedExceptionLevel = level
        self.line: int = line
        self.column: int = column
        self.file = file
        self.msg: str = msg

    def __str__(self) -> str:
        return f"({self.code}) {self.level.name} at ({self.line}:{self.column}) in '{self.file}':\n   {self.msg}\n"