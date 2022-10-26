# real!

import subprocess as sp
from pathlib import Path

def get_version() -> str:
    if Path('.git').exists():
        return f"{sp.getoutput('git rev-parse --abbrev-ref HEAD')}_{sp.getoutput('git rev-parse --short HEAD')}"
    else:
        return pkg_resources.get_distribution(__package__).version

def main() -> None:
    print("this ratio")
    print(get_version())

if __name__ == "__main__":
    main()
