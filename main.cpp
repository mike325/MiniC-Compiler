/*
 * File:   main.cpp
 * Author: Miguel Ochoa Hernandez
 *
 */

#include <iostream>
#include <string.h>
#include "Include/Sintactical.h"
#include "Include/Read.h"

int main( int argc, char *argv[] )
{
    char *name = NULL;
    analyzers::Sintactical analizer;
    Read file;

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

    // std::cout << name << std::endl;
    return 0;
}
