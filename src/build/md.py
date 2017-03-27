import glob

def get_files_content(filenames):
    for filename in filenames:
        with open(filename) as f:
            yield f.read()


def read_files(files_glob):
    filenames = glob.glob(files_glob)
    return '\n'.join(list(get_files_content(filenames)))
