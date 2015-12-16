//
// Created by mike on 16/12/15.
//

#include "../../Include/namespaceExceptions/Exceptions.h"

const char* exceptions::Exception::what() const throw()
{
    std::string description("Has been an unexpected error, ");
    description.append(this->message);
    return description.c_str();
}