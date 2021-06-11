name = "qtbase"

version = "5.15.2"

description = \
    """
    Qt Base
    """

with scope("config") as c:
    # Determine location to release: internal (int) vs external (ext)

    # NOTE: Modify this variable to reflect the current package situation
    release_as = "ext"

    # The `c` variable here is actually rezconfig.py
    # `release_packages_path` is a variable defined inside rezconfig.py

    import os
    if release_as == "int":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_INT"]
    elif release_as == "ext":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

    #c.build_thread_count = "physical_cores"

requires = [
]

private_build_requires = [
    "cmake",
]

variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7", "python-2.7"],
    ["platform-linux", "arch-x86_64", "os-centos-7", "python-3.7"],
]

# If want to use Ninja, run the `rez-build -i --cmake-build-system "ninja"`
# or `rez-release --cmake-build-system "ninja"`

uuid = "repository.qtbase"

def pre_build_commands():
    command("source /opt/rh/devtoolset-6/enable")

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.QT_LOCATION = "{root}"
