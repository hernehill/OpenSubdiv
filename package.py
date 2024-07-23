name = "OpenSubdiv"

version = "3.6.0.hh.1.0.0"

authors = [
    "Pixar",
]

description = """Subdivision surface evaluation"""

with scope("config") as c:
    import os

    c.release_packages_path = os.environ["HH_REZ_REPO_RELEASE_EXT"]

requires = [
    "clew",
    "glfw",
    "tbb",
]

private_build_requires = []

variants = [
    ["python-3.7"],
    ["python-3.9"],
    ["python-3.10"],
    ["python-3.11"],
    ["python-3.12"],
]


def commands():
    env.REZ_OPENSUBDIV_ROOT = "{root}"
    env.OPENSUBDIV_ROOT = "{root}"
    env.OPENSUBDIV_ROOT_DIR = "{root}"
    env.OPENSUBDIV_LOCATION = "{root}"

    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")


uuid = "repository.OpenSubdiv"
