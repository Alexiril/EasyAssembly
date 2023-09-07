ponyPhrases: list[str] = [
    "You know what they say, friendship truly is the magic.",
    "Wow, that's my little pony!",
    "Does anypony know where I can find an accordion?",
    "Thank you, everypony, for being here bright and early.",
    "I challenge you to a hoof-wrestle.",
    "I am going for a hooficure and that is that!",
    "I wish the mailpony would just come already!"
]

if __name__ == '__main__':
    print("EASM Interpreter")

    from os.path import join
    from sys import argv

    from genericpath import isdir, isfile

    if len(argv) < 3:
        # TODO: explain what's wrong and how to use
        print("Uncorrect using (wrong argv)")
        exit(-1)
    asmFile = argv[1]
    if not isfile(asmFile):
        print("Uncorrect using (wrong file)")  # TODO: explain
        exit(-1)

    from os import mkdir

    outFolder = argv[2]

    if not isdir(outFolder):
        mkdir(outFolder)

    from random import choice

    from antlr4 import (CommonTokenStream, FileStream,  # type: ignore
                        ParseTreeWalker)

    from easm2c import easm2cBuilder, easm2cTranslator, easm2cVersion, easm2cRuntime
    from easmErrorListener import easmErrorListener
    from easmLexer import easmLexer
    from easmParser import easmParser
    from shared import UnifiedId, UnifiedRules

    files: list[str] = [asmFile]
    baseFolder: str = '.'
    clearedAsmFile = asmFile.replace("\\", "/")
    if len(clearedAsmFile.split("/")) > 1:
        baseFolder = "/".join(clearedAsmFile.split("/")[:-1])
    includedFiles: set[str] = set()
    declaredFunction: dict[str, str] = dict()
    declaredStructures: dict[str, str] = dict()
    result: list[str] = list()
    ids = UnifiedId()
    rules = UnifiedRules()

    print(f"{choice(ponyPhrases)}\n")

    # Translate step

    def findFile(filename: str) -> str:
        if isfile(filename):
            return filename
        if isfile(join(baseFolder, filename)):
            return join(baseFolder, filename)
        if isfile(join("Lib", filename)):
            return join("Lib", filename)
        return ''

    print(f"EASM2C Translator v{'.'.join(map(str, easm2cVersion))}\n")

    while len(files) > 0:
        files[0] = findFile(files[0])
        filecode: str = files[0].translate({46: 95, 47: 95, 92: 95}).upper()
        if filecode in includedFiles:
            files.pop(0)
            continue
        readableAddr = files[0].replace('\\', '/')
        print(f"---- File: '{readableAddr}' ----")
        includedFiles.add(filecode)
        input_stream = FileStream(files[0], 'utf8')
        lexer = easmLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = easmParser(stream)
        errorListener = easmErrorListener()
        lexer.removeErrorListeners()
        parser.removeErrorListeners()
        lexer.addErrorListener(errorListener)  # type: ignore
        parser.addErrorListener(errorListener)  # type: ignore
        tree = parser.program()
        if errorListener.errAmount > 0:
            print(f"{errorListener.errAmount} syntax errors found.\n")
        walker = ParseTreeWalker()
        listener = easm2cTranslator(ids, rules, filecode, files[0])
        walker.walk(listener, tree)
        result.insert(0, str(listener))
        imports: set[str] = listener.imports
        funcs: set[str] = listener.functions
        structs: set[str] = listener.structures
        err: bool = len(listener.exceptions) > 0
        if err:
            for exception in listener.exceptions:
                print(exception)
        for func in funcs:
            if func in declaredFunction:
                print(
                    f"Function '{func}' is already defined. Functions cannot share same name. Files: '{declaredFunction[func]}', '{files[0]}'")
                err = True
            else:
                declaredFunction[func] = files[0]
        for struct in structs:
            if struct in declaredStructures:
                print(
                    f"Structure '{struct}' is already defined. Structures cannot share same name. Files: '{declaredStructures[struct]}', '{files[0]}'")
                err = True
            else:
                declaredStructures[struct] = files[0]
        if err:
            print(
                f"{len(listener.exceptions)} exceptions located.")
            print("Stopping translating. Needs to fix errors to continue.")
            exit(-1)
        files.pop(0)
        files.extend(imports)

    result.insert(0, easm2cRuntime())

    writable: str = "\n".join(result)

    print("Translated successfully.")
    print("Building starts:")

    # Building step

    builder = easm2cBuilder(outFolder, writable)
    builder.build()

    if not builder.exceptions:
        print("Builded successfully.")

    # Run step

    from subprocess import Popen

    Popen([join(outFolder, "native_build", "Debug", "easmProgram.exe")]).wait()
