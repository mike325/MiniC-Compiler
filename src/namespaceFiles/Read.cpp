/*
 * File:   Read.cpp
 * Author: Miguel Ochoa Hernandez
 *
 */

#include <fstream>
#include <string.h>
#include "../../Include/namespaceFiles/Read.h"
#include "../../Include/namespaceExceptions/FileException.h"

files::Read::Read() { name = ""; }
files::Read::~Read() { name = ""; }
void files::Read::readFile()
{
    name = "";
    while ( name == "" )
    {
        std::cout << "File to Compile:  ";
        std::getline( std::cin, name );

        if ( !std::cin.good() )
        {
            name = "";
            std::cin.clear();
        }
        else
        {
            std::ifstream file( name.c_str() );

            if ( !file.good() )
            {
                name = "";
            }

            file.close();
        }
    }
}
char *files::Read::assignName( char *name )
{
    char *new_name;

    if ( name == NULL )
    {
        new_name = new char[this->name.size()];
        strcpy( new_name, this->name.c_str() );
    }
    else
    {
        new_name = new char[strlen( name )];
        strcpy( new_name, name );
    }

    std::ifstream file(new_name);

    if(!file.good())
    {
        std::string file_name(new_name);
        throw new exceptions::FileException(file_name);
    }

    return new_name;
}
