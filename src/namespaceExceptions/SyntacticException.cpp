//
// Created by mike on 17/12/15.
//

//
// Created by mike on 17/12/15.
//

#include <string>
#include "../../Include/namespaceExceptions/SyntacticException.h"

exceptions::SyntacticException::SyntacticException( std::string line )
        : GeneralException()
{
    this->description.assign( "The token " );
    this->message.assign( line );
    this->message.append( " is not part of the language" );
    this->description.append( this->message );
}

const char *exceptions::SyntacticException::what() const throw() { return this->description.c_str(); }