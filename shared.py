from enum import Enum
from random import randint

from easmListener import easmListener


class SharedRules:

    decoupleIDs: bool = True
    noRuntime: bool = False


class SharedId:

    def __init__(self) -> None:
        self.uids: list[str] = list()
        self.decouplingId: dict[str, str] = dict()
        self.decouplingUid: dict[str, str] = dict()

    def getRandomUId(self) -> str:
        result = '_'
        while result in self.uids or result == '_':
            result: str = '_' + hex(randint(0, 0xFF_FFFF_FFFF))
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
        return self.decouplingUid.get(uid, uid)


class SharedExceptionLevel(Enum):
    Error = 0
    Warning = 1
    Notice = 2


class SharedException:

    def __init__(self, code: str, level: SharedExceptionLevel, line: int, column: int, file: str, msg: str) -> None:
        self.code: str = code.upper()
        self.level: SharedExceptionLevel = level
        self.line: int = line
        self.column: int = column
        self.file = file
        self.msg: str = msg

    def __str__(self) -> str:
        color = ""
        match self.level:
            case SharedExceptionLevel.Error:
                pass
            case _:
                pass
        return f"({color}{self.code}) {self.level.name} at ({self.line}:{self.column}) in '{self.file}':\n   {self.msg}\n"


class SharedBuilder:

    def __init__(self, folder: str) -> None:
        self.exceptions: list[SharedException] = list()
        self.folder = folder

    def build(self) -> None:
        pass


class SharedTranslator(easmListener):

    def __init__(self, ids: SharedId, rules: SharedRules, filecode: str, filename: str) -> None:
        super().__init__()
        self.ids: SharedId = ids
        self.rules: SharedRules = rules
        self.filecode: str = filecode
        self.filename: str = filename
        self.imports: set[str] = set()
        self.functions: set[str] = set()
        self.neededFunctions: set[str] = set()
        self.structures: set[str] = set()
        self.neededStructures: set[str] = set()
        self.externalValues: set[str] = set()
        self.expressionConnection: list[int] = list()
        self.opcodesConnection: list[int] = list()
        self.exceptions: list[SharedException] = list()
        self.result: list[str] = list()

    def __str__(self) -> str:
        return "\n".join(self.result)


class SharedRunner:

    def __init__(self, outFolder: str) -> None:
        self.outFolder: str = outFolder

    def run(self) -> None:
        return


class SharedHandler:

    def __init__(self, name: str, lang: str, translator: type[SharedTranslator], builder: type[SharedBuilder], runner: type[SharedRunner], runtime: str, version: tuple[int, int, int]) -> None:
        self.name: str = name
        self.translator: type[SharedTranslator] = translator
        self.builder: type[SharedBuilder] = builder
        self.lang: str = lang
        self.runner: type[SharedRunner] = runner
        self.runtime: str = runtime
        self.version: tuple[int, int, int] = version
