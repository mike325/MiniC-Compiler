//
// Created by mike on 16/12/15.
//

#include <string>
#include "../../Include/namespaceExceptions/FileException.h"

exceptions::FileException::FileException(std::string message) : GeneralException()
{
    this->message.assign(message);
    this->message.append(" could not been loaded");
    this->description.assign("The file ");
    this->description.append(this->message);
}

exceptions::FileException::~FileException () throw()
{
    this->message = "";
    this->description = "";
}

const char* exceptions::FileException::what() const throw()
{
    return  this->description.c_str();
}