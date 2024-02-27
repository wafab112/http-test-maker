#!/bin/bash
"exec" "python" "$0" "$@"

from cli import Cli

if __name__ == "__main__":
    cli = Cli()
