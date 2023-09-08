#!/usr/bin/env python

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
    from random import choice, randint

    separated = ("EASM\n\n" + choice(ponyPhrases)).split(" ")

    print("\033[4m", end='')
    for c in separated:
        color: int = randint(91, 96)
        print(f"\033[{color}m{c} ", end='')
    print("\033[0m\n")

    from argparse import ArgumentParser, Namespace
    from os.path import join
    from sys import argv

    from genericpath import isdir, isfile

    from easm2c import easm2c
    from shared import SharedHandler

    avaliable_handlers: list[SharedHandler] = [easm2c]
    avaliable_handlers_names: list[str] = [
        x.name for x in avaliable_handlers]

    parser = ArgumentParser()
    parser.add_argument('command', type=str,
                        help="command that the handler will run. Commands:\n\ttranslate\n\tbuild\n\trun")
    parser.add_argument('source', type=str, default="main.easm",
                        help="path to source asm / easm / eab file")
    parser.add_argument('out', type=str, default='.',
                        help="path to output folder")
    parser.add_argument('-d', '--handler', required=False, type=str, default="easm2c",
                        help=f"set handler. Avaliable: {avaliable_handlers_names}")

    args: Namespace = parser.parse_args(argv[1:])

    if not args.handler in avaliable_handlers_names:
        print(f"Sorry, the handler '{args.handler}' is not avaliable.")
        print(f"Avaliable handler: {avaliable_handlers_names}")
        exit()

    handlername = str(args.handler)

    handler: SharedHandler = list(filter(
        lambda x: x.name == handlername, avaliable_handlers))[0]

    args.command = args.command.lower()

    if not args.command in ["translate", "build", "run"]:
        print(f"Sorry, {args.command} is not the correct command.")
        print("Avaliable commands are: 'translate', 'build', 'run'")
        exit()

    if not isfile(args.source):
        print(
            f"Sorry, {args.source} is not the correct filename of source code.")
        exit()

    outFolder = args.out

    if not isdir(outFolder):
        from os import mkdir

        mkdir(outFolder)

    from antlr4 import (CommonTokenStream, FileStream,  # type: ignore
                        ParseTreeWalker)

    from easmErrorListener import easmErrorListener
    from easmLexer import easmLexer
    from easmParser import easmParser
    from shared import SharedId, SharedRules

    files: list[str] = [args.source]
    baseFolder: str = '.'
    clearedAsmFile = args.source.replace("\\", "/")
    if len(clearedAsmFile.split("/")) > 1:
        baseFolder = "/".join(clearedAsmFile.split("/")[:-1])
    includedFiles: set[str] = set()
    declaredFunction: dict[str, str] = dict()
    declaredStructures: dict[str, str] = dict()
    result: list[str] = list()
    ids = SharedId()
    rules = SharedRules()

    # Translate step

    print("Translating starts.")

    def findFile(filename: str) -> str:
        def checkExt(filename: str) -> str:
            if isfile(filename):
                return filename
            if isfile(f"{filename}.asm"):
                return f"{filename}.asm"
            if isfile(f"{filename}.easm"):
                return f"{filename}.easm"
            if isfile(f"{filename}.eab"):
                return f"{filename}.eab"
            return ''
        value: str = checkExt(filename)
        if value == '':
            value = checkExt(join(baseFolder, filename))
        if value == '':
            value = checkExt(join("Lib", filename))
        return value

    print(f"{handler.name.upper()} Handler v{'.'.join(map(str, handler.version))}\n")

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
        listener = handler.translator(ids, rules, filecode, files[0])
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

    result.insert(0, handler.runtime)

    writable: str = "\n".join(result)

    print("Translated successfully.")

    with open(join(outFolder, "EASMTranslated.c"), 'w') as cfile:
        cfile.write(writable)

    if args.command == "translate":
        exit()

    # Building step

    print("Building starts.")

    builder = handler.builder(outFolder)
    builder.build()

    if not builder.exceptions:
        print("Builded successfully.")

    if args.command == "build":
        exit()

    # Run step

    handler.runner(outFolder).run()

    if args.command == "run":
        exit()
