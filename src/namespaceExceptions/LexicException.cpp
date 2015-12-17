//
// Created by mike on 17/12/15.
//

#include <string>
#include "../../Include/namespaceExceptions/LexicException.h"

exceptions::LexicException::LexicException( std::string token )
        : GeneralException()
{
    this->description.assign( "The token " );
    this->message.assign( token );
    this->message.append( " is not part of the language" );
    this->description.append( this->message );
}

const char *exceptions::LexicException::what() const throw() { return this->description.c_str(); }