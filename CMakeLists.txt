cmake_minimum_required(VERSION 3.3)
project(Compiler)

set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14 -O3 -Wall")
set (Include_dirs Include)
set (Project_bin_src main.cpp)
set (Project_src    src/Sintactical.cpp
                    src/Lexical.cpp
                    src/Semantical.cpp
                    src/Read.cpp
)

include_directories (${Include_dirs})
add_library (Project_lib SHARED ${Project_src})

add_executable(Compiler ${Project_bin_src} ${Project_src})