import glob

def get_files_content(filenames):
    for filename in filenames:
        with open(filename) as f:
            yield f.read()


def read_files(filenames):
    return '\n'.join(list(get_files_content(filenames)))
