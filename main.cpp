/*
 * File:   main.cpp
 * Author: Miguel Ochoa Hernandez
 *
 */

#include "Include/namespaceAnalyzers/Syntactic.h"
#include "Include/namespaceFiles/Read.h"

int main( int argc, char *argv[] )
{
    char *name = NULL;
    analyzers::Syntactic analyzer;
    files::Read file;

    if ( argc <= 1 )
    {
        // std::cout << file.name << std::endl;
        file.readFile();
        name = file.assingName( NULL );
    }
    else
    {
        name = file.assingName( argv[1] );
    }

    analyzer.analyze(name);

    return 0;
}
