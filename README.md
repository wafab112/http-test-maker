# HTTP-test-maker
A cli-tool for creating scripts, 
that execute various REST-endpoints (using the JSON-file-format) after authenticating.

## How does it work
When using a unix-like system, you can just call
```bash
$ ./http-tm.py -h
```
to see helpful information. It will call the python script via bash 
(provided it finds a `python3` interpreter in your `$PATH`).
If you are using windows or you do not have a `python3` in your `$PATH`, you must either change the shebang
in `http-tm.py` or you call the regular way:
```bash
$ /path/to/python http-tm.py -h
```
