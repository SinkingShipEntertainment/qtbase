CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


set(pck_prefix qtbase)
set(pck_version $ENV{REZ_BUILD_PROJECT_VERSION})

message(STATUS "----------  Env and CMake variables-----")
message(STATUS "PROJECT_BINARY_DIR = ${PROJECT_BINARY_DIR}")
message(STATUS "env REZ_BUILD_SOURCE_PATH = $ENV{REZ_BUILD_SOURCE_PATH}")
message(STATUS "----------------------------------------")

ExternalProject_add(
    ${pck_prefix}
    SOURCE_DIR $ENV{REZ_BUILD_SOURCE_PATH}
    BINARY_DIR $ENV{REZ_BUILD_PATH}
    PREFIX ${pck_prefix}
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND $ENV{REZ_BUILD_SOURCE_PATH}/configure --prefix=${CMAKE_INSTALL_PREFIX} -opensource -nomake tests -nomake examples
    BUILD_COMMAND make -j$ENV{REZ_BUILD_THREAD_COUNT}
    INSTALL_COMMAND ""
    BUILD_IN_SOURCE 0
    BUILD_ALWAYS 1
)
