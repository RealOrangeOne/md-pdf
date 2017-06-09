import glob
from typing import Generator, List


def get_files_content(filenames: List[str]) -> Generator[str, None, None]:
    for filename in filenames:
        with open(filename) as f:
            yield f.read()


def read_files(files_glob: str) -> str:
    filenames = sorted(glob.glob(files_glob))
    return '\n'.join(list(get_files_content(filenames)))
