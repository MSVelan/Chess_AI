import toml
import setuptools


def get_install_requirements():
    try:
        # read my pipfile
        with open("Pipfile", "r") as fh:
            pipfile = fh.read()
        # parse the toml
        pipfile_toml = toml.loads(pipfile)
    except FileNotFoundError:
        return []  # if the package's key isn't there then just return an empty
    # list
    try:
        required_packages = pipfile_toml["packages"].items()
    except KeyError:
        return []
    # If a version/range is specified in the Pipfile honor it
    # otherwise just list the package
    return [
        "{0}{1}".format(pkg, ver) if ver != "*" else pkg
        for pkg, ver in required_packages
    ]


setuptools.setup(
    name="chess_bot",
    version="1.0",
    packages=["Chess"],
    install_requires=get_install_requirements(),
    entry_points={"console_scripts": ["chess-bot=ChessMain:main"]},
    include_package_data=True,
)
