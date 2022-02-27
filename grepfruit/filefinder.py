from pathlib import Path
from typing import Iterator
import re

def find_files(path: Path, glob_pattern: str, recurse: bool = True) -> Iterator[Path]:
    glob = ''
    if recurse:
        glob += '**/'
    glob += glob_pattern
    return path.glob(glob)

def find_dirs(path: Path, pattern: re.Pattern) -> Iterator[Path]:
    for d in path.iterdir():
        if d.is_dir() and re.search(pattern, d.name):
            yield d

def find_lines(file: Path, pattern: re.Pattern) -> Iterator[str]:
    with file.open() as f:
        for i, line in enumerate(f):
            if re.search(pattern, line):
                yield f"{i+1}: {line.strip()}"
    



def main():
    path = Path('C:/Users/btona/MyGit')

    y = find_dirs(path, re.compile(r'Sudoku'))
    dir = next(y)

    x = find_files(dir, '*.py', False)
    files = list(x)
    print(files)

    z = find_lines(files[0], re.compile(r'^import'))
    for match in z:
        print(match)

if __name__ == '__main__':
    main()