//
// Created by mike on 16/12/15.
//

#include <string>
#include <algorithm>
#include "../../Include/namespaceExceptions/FileException.h"

exceptions::FileException::FileException( std::string file_name )
    : GeneralException()
{
    this->description.assign( "The file " );
    this->message.assign( file_name );
    this->message.append( " could not be load" );
    this->description.append( this->message );
}

exceptions::FileException::FileException( std::string file_name, std::string description )
    : GeneralException()
{
    this->description.assign( description );
    std::size_t pos = this->description.find( '#' );
    this->description.replace( pos, 1, file_name );
}

const char *exceptions::FileException::what() const throw() { return this->description.c_str(); }