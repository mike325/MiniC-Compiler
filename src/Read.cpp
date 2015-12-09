/*
 * File:   Read.cpp
 * Author: Miguel Ochoa Hernandez
 *
 */

#include <fstream>
#include <string.h>
#include "../Include/Read.h"

Read::Read() { name = ""; }
Read::~Read() { name = ""; }
void Read::readFile()
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
char *Read::assingName( char *name )
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

    return new_name;
}
