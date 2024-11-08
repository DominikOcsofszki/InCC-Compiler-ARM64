def _read_all_files_from_codeTx(file_name):
    with open(file_name, "r") as file:
        files = file.read()
        return files


def _checkForFirstFileEntryNotCommentedOut(file: str):
    if file.startswith("#"):
        return None
    return file


def _get_data_filename_of_first_file_not_commented(files, code_path):
    for found_filename in files.splitlines():
        # if found_filename.startswith("#"):
        if _checkForFirstFileEntryNotCommentedOut(found_filename):
            file_code_path = code_path + found_filename
            with open(file_code_path, "r") as file:
                data = file.read()
                return data, found_filename


def checkAndOpenFileFromCodeTx(all_code_file_list_name="code.tx", code_path="code/"):
    files = _read_all_files_from_codeTx(all_code_file_list_name)
    data, file_name = _get_data_filename_of_first_file_not_commented(files, code_path)
    data_copy, file_name_copy = data, file_name
    print(code_path + file_name)
    print("====================input:=======================")
    print_all_lines(file_name, code_path)
    print("====================output:=======================\n")
    return data_copy, file_name_copy


def print_all_lines(code_file_name, code_path):
    file = code_path + code_file_name
    with open(file, "r") as file:
        linenr = 1
        for line in file:
            if not line.startswith("\n"):
                line = line.partition("#")[0]
                line = line.rstrip()
                if len(line) > 0:
                    print(linenr, line)
            linenr += 1
        return


def _get_filename_of_first_file_not_commented(files):
    for found_filename in files.splitlines():
        if _checkForFirstFileEntryNotCommentedOut(found_filename):
            return found_filename


def getFileNameFromcodeTX(all_code_file_list_name="code.tx"):
    files = _read_all_files_from_codeTx(all_code_file_list_name)
    file_name = _get_filename_of_first_file_not_commented(files)
    file_name = file_name.strip()
    file_name=file_name.split(".")
    # return file_name.strip("\.incc")
    # return file_name.strip
    return file_name[:-1]


if __name__ == "__main__":
   file = getFileNameFromcodeTX()
   print(file)


def print_data_as_file(file):
    linenr = 1
    for line in file:
        if not line.startswith("\n"):
            line = line.partition("#")[0]
            line = line.rstrip()
            if len(line) > 0:
                print(linenr, line)
        linenr += 1
