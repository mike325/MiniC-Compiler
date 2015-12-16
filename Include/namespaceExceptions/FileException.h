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

        FileException ( std::string message);
        ~FileException () throw();
        const char* what() const throw();

    private:
    };
}

#endif //COMPILER_FILEEXCEPTION_H
