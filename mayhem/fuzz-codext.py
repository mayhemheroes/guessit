#! /usr/bin/python3

import atheris
import sys
import io
import random

with atheris.instrument_imports():
    import codext

def TestOneInput(input_bytes):
    try:
        fdp = atheris.FuzzedDataProvider(input_bytes)
        data = fdp.ConsumeString(sys.maxsize)
        encoded = codext.encode(data, "base100")
        decoded = codext.decode(data, "base100")

        if data != decoded:
            raise Exception("Logic error")
    except UnicodeDecodeError:
        pass
    except ValueError:
        pass

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
