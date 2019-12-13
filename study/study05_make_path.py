from pathlib import Path


def make_path(url):
    path = Path(url)
    full_path = path.absolute()
    return_path = full_path.as_posix()
    return return_path


if __name__ == "__main__":
    make_path("../images/test.jpg")