cmake_minimum_required(VERSION 3.3)
project(Compiler)

set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -O2 -Wall")
set (Include_dirs   Include/namespaceFiles
                    Include/namespaceAnalyzers
)
set (Project_bin_src main.cpp)
set (Project_src    src/namespaceFiles/Read.cpp
                    src/namespaceAnalyzers/Lexic.cpp
                    src/namespaceAnalyzers/Syntactic.cpp
                    src/namespaceAnalyzers/Semantic.cpp
                    src/namespaceStack/Terminal.cpp
                    src/namespaceStack/NonTerminal.cpp
                    src/namespaceStack/State.cpp
                    src/namespaceStack/GrammarElement.cpp
)

include_directories (${Include_dirs})
add_library (Project_lib SHARED ${Project_src})

add_executable(Compiler ${Project_bin_src} ${Project_src})