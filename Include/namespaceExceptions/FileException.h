//
// Created by mike on 16/12/15.
//

#ifndef FILEEXCEPTION_H
#define FILEEXCEPTION_H

#include "../../Include/namespaceExceptions/GeneralException.h"
#include <iostream>

namespace exceptions
{
    class FileException : public GeneralException
    {
      public:
        FileException( std::string file_name );
        FileException( std::string file_name, std::string description );
        ~FileException() throw() {}
        const char *what() const throw();

      private:
    };
}

#endif    // FILEEXCEPTION_H
