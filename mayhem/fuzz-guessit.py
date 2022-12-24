#! /usr/bin/python3

import atheris
import sys
import io
import random

with atheris.instrument_imports():
    import guessit

def TestOneInput(input_bytes):
    fdp = atheris.FuzzedDataProvider(input_bytes)
    data = fdp.ConsumeString(sys.maxsize)
    guessit.guessit(data)

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
