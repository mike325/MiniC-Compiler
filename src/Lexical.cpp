/*
 * File:   Lexical.cpp
 * Author: Miguel Ochoa Hernandez
 *
 */

#include <string.h>
#include "../Include/Lexical.h"

analyzers::Lexical::Lexical()
{
    // pendient
    this->keyword["int"]    = 4;
    this->keyword["float"]  = 4;
    this->keyword["void"]   = 4;
    this->keyword["string"] = 4;
    this->keyword["if"]     = 19;
    this->keyword["else"]   = 22;
    this->keyword["while"]  = 20;
    this->keyword["return"] = 21;

    this->simbol = "";
    this->state  = 0;
    this->type   = 0;
    this->index  = 0;
    this->error  = false;
}

analyzers::Lexical::~Lexical()
{
    this->keyword.clear();
    this->simbol = "";
    this->state  = 0;
    this->type   = 0;
    this->index  = 0;
    this->error  = false;
}

std::string analyzers::Lexical::deleteSpaces( std::string stream )
{
    stream.assign( stream.substr( this->index ) );
    if ( stream[0] == ' ' || stream[0] == '\t' || stream[0] == '\n' || stream[0] == '\r' )
    {
        this->index++;
        stream.assign( this->deleteSpaces( stream ) );
    }
    return stream;
}

std::string analyzers::Lexical::getToken( std::string stream )
{
    this->index  = 0;
    this->state  = 0;
    this->simbol = "";

    stream.assign( this->deleteSpaces( stream ) );
    this->index = 0;

    if ( stream != "" && this->index < stream.size() )
    {
        this->consume( stream );

        if ( this->index < stream.size() )
        {
            stream.assign( stream.substr( this->index ) );
        }
        else
        {
            stream = "";
        }
    }
    else
    {
        stream = "";
    }

    return stream;
}

bool analyzers::Lexical::outLimit( std::string stream )
{
    bool out_limit = false;

    if ( this->index + 1 >= stream.size() )
    {
        out_limit = true;
    }

    return out_limit;
}

void analyzers::Lexical::keywords( std::string stream )
{
    if ( this->keyword.find( stream ) != this->keyword.end() )
    {
        this->state = 2;
    }
}

void analyzers::Lexical::nextState( std::string stream, int state )
{
    this->state = state;
    this->simbol.push_back( stream[this->index] );
    this->index++;
}

void analyzers::Lexical::identifier( std::string stream )
{
    if ( !this->outLimit( stream ) )
    {
        if ( isalpha( stream[this->index] ) || isdigit( stream[this->index] ) ||
             stream[this->index] == '_' )
        {
            this->nextState( stream, 1 );
            this->identifier( stream );
        }
    }
}

void analyzers::Lexical::real( std::string stream )
{
    if ( !this->outLimit( stream ) )
    {
        if ( isdigit( stream[this->index] ) )
        {
            this->nextState( stream, 5 );
            this->real( stream );
        }
    }
}

void analyzers::Lexical::integer( std::string stream )
{
    if ( !this->outLimit( stream ) )
    {
        if ( isdigit( stream[this->index] ) )
        {
            this->nextState( stream, 3 );
            this->integer( stream );
        }
        else if ( stream[this->index] == '.' )
        {
            this->nextState( stream, 4 );
            this->real( stream );
        }
    }
}

void analyzers::Lexical::string( std::string stream )
{
    if ( !this->outLimit( stream ) )
    {
        if ( stream[this->index] != '"' )
        {
            this->nextState( stream, 7 );
            this->string( stream );
        }
    }
}

void analyzers::Lexical::checkNext( std::string stream, char character, int state )
{
    if ( !this->outLimit( stream ) )
    {
        if ( stream[this->index] == character )
        {
            this->nextState( stream, state );
        }
    }
}

void analyzers::Lexical::consume( std::string stream )
{
    if ( isalpha( stream[this->index] ) )
    {
        this->nextState( stream, 1 );
        this->identifier( stream );

        this->keywords( stream );
    }
    else if ( isdigit( stream[this->index] ) )
    {
        this->nextState( stream, 3 );
        this->integer( stream );
    }
    else if ( stream[this->index] == '"' )
    {
        this->nextState( stream, 6 );
        this->string( stream );

        if ( stream[this->index] == '"' )
        {
            this->nextState( stream, 8 );
        }
    }
    else if ( stream[this->index] == ';' )
    {
        this->nextState( stream, 9 );
    }
    else if ( stream[this->index] == ',' )
    {
        this->nextState( stream, 10 );
    }
    else if ( stream[this->index] == '+' || stream[this->index] == '-' )
    {
        this->nextState( stream, 11 );
    }
    else if ( stream[this->index] == '*' || stream[this->index] == '/' )
    {
        this->nextState( stream, 12 );
    }
    else if ( stream[this->index] == '(' || stream[this->index] == ')' )
    {
        this->nextState( stream, 13 );
    }
    else if ( stream[this->index] == '[' || stream[this->index] == ']' )
    {
        this->nextState( stream, 14 );
    }
    else if ( stream[this->index] == '{' || stream[this->index] == '}' )
    {
        this->nextState( stream, 15 );
    }
    else if ( stream[this->index] == '=' )
    {
        this->nextState( stream, 16 );
        this->checkNext( stream, '=', 18 );
    }
    else if ( stream[this->index] == '!' )
    {
        this->nextState( stream, 17 );
        this->checkNext( stream, '=', 18 );
    }
    else if ( stream[this->index] == '<' || stream[this->index] == '>' )
    {
        this->nextState( stream, 19 );
        this->checkNext( stream, '=', 20 );
    }
    else if ( stream[this->index] == '&' )
    {
        this->nextState( stream, 21 );
        this->checkNext( stream, '&', 22 );
    }
    else if ( stream[this->index] == '|' )
    {
        this->nextState( stream, 23 );
        this->checkNext( stream, '|', 24 );
    }
    else if ( stream[this->index] == '$' )
    {
        this->nextState( stream, 25 );
    }
    else
    {
        this->nextState( stream, 26 );
    }
}

void analyzers::Lexical::getType()
{
    switch ( this->state )
    {
        case 1:
            break;
        case 2:
            break;
        case 3:
            break;
        case 4:
            break;
        case 5:
            break;
        case 6:
            break;
        case 7:
            break;
        case 8:
            break;
        case 9:
            break;
        case 10:
            break;
        case 11:
            break;
        case 12:
            break;
        case 13:
            break;
        case 14:
            break;
        case 15:
            break;
        case 16:
            break;
        case 17:
            break;
        case 18:
            break;
        case 19:
            break;
        case 20:
            break;
        case 21:
            break;
        case 22:
            break;
        case 23:
            break;
        case 24:
            break;
        case 25:
            break;
    }
}

/*
void print();
*/