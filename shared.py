from enum import Enum
from random import randint

class UnifiedRules:

    decoupleIDs: bool = True

class UnifiedId:

    def __init__(self) -> None:
        self.uids: list[str] = list()
        self.decouplingId: dict[str, str] = dict()
        self.decouplingUid: dict[str, str] = dict()

    def getRandomUId(self) -> str:
        result = '_'
        while result in self.uids or result == '_':
            result: str = '_' + hex(randint(0, 0xFFFFFF))
        self.uids.append(result)
        return result

    def decoupleId(self, id: str) -> str:
        if id in self.decouplingId:
            return self.decouplingId[id]
        uid = self.getRandomUId()
        self.decouplingId[id] = uid
        self.decouplingUid[uid] = id
        return uid
    
    def getId(self, uid: str) -> str:
        return self.decouplingUid.get(uid, '')


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
