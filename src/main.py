import shutil
from pathlib import Path


def main() -> None:
    USER = Path(r"/home/jarryd/.config/Code/User/")
    keybindings = USER / "keybindings.json"
    settings = USER / "settings.json"

    shutil.copyfile(keybindings.absolute(), f".vscode/user/{keybindings.name}")
    shutil.copyfile(settings, f".vscode/user/{settings.name}")

    return None


if __name__ == "__main__":
    main()
