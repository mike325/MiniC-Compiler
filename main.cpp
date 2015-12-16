/*
 * File:   main.cpp
 * Author: Miguel Ochoa Hernandez
 *
 */

#include "Include/namespaceAnalyzers/Syntactic.h"
#include "Include/namespaceFiles/Read.h"
#include "Include/namespaceExceptions/FileException.h"

int main( int argc, char *argv[] )
{
    char *name = NULL;
    analyzers::Syntactic analyzer;
    files::Read file;

    try {
        if ( argc <= 1 )
        {
            // std::cout << file.name << std::endl;
            file.readFile();
            name = file.assignName( NULL );
        }
        else
        {
            name = file.assignName( argv[1] );
        }

        analyzer.analyze( name );
    }
    catch (exceptions::FileException &load)
    {
        std::cout << load.what() << std::endl;
    }

    return 0;
}
