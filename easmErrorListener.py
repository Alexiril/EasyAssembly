from antlr4.error.ErrorListener import ErrorListener # type: ignore
from antlr4.Token import CommonToken # type: ignore

from easmParser import easmParser

class easmErrorListener(ErrorListener):
    
    def __init__(self) -> None:
        self.errAmount = 0
        super().__init__()

    def syntaxError(self, recognizer: easmParser, offendingSymbol: CommonToken, line: int, column: int, msg: str, e: None) -> None:
        if len(msg) > 60:
            msg = msg[:60] + "..."
        print(f"\n---\nSyntax error on line {line}, column {column} :\n" + (" " * 2) + f"... {msg}\n---\n")
        self.errAmount += 1