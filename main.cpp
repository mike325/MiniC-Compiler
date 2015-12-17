/*
 * File:   main.cpp
 * Author: Miguel Ochoa Hernandez
 *
 */

#include <stdexcept>
#include "Include/namespaceAnalyzers/Syntactic.h"
#include "Include/namespaceFiles/Read.h"
#include "Include/namespaceExceptions/FileException.h"
#include "Include/namespaceExceptions/LexicException.h"
#include "Include/namespaceExceptions/SyntacticException.h"

int main( int argc, char *argv[] )
{
    try
    {
        char *name = NULL;
        analyzers::Syntactic analyzer;
        files::Read file;
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
    catch ( const std::out_of_range &index_error )
    {
        std::cout << "An unexpected error has ocurred:" << std::endl;
        std::cout << index_error.what() << std::endl;
    }
    catch ( const exceptions::FileException &load_error )
    {
        std::cout << load_error.what() << std::endl;
    }
    catch ( const exceptions::LexicException &token_error)
    {
        std::cout << token_error.what() << std::endl;
    }
    catch ( const exceptions::SyntacticException &grammar_error)
    {
        std::cout << grammar_error.what() << std::endl;
    }

    return 0;
}
