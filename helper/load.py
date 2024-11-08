from file_loader import checkAndOpenFileFromCodeTx


def get_caller_module_dict(levels):
    # import sys
    import sys

    f = sys._getframe(levels)
    ldict = f.f_globals.copy()
    if f.f_globals != f.f_locals:
        ldict.update(f.f_locals)
    return ldict


if __name__ == "__main__":
    import os

    data, filename = checkAndOpenFileFromCodeTx()
    print(data)

    print(os.environ.get("incc"))
    # vim.eval("ASD")
    # runFromFile_code()
