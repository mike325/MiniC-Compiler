//
// Created by mike on 17/12/15.
//

#ifndef LEXICEXCEPTION_H
#define LEXICEXCEPTION_H

#include "../../Include/namespaceExceptions/GeneralException.h"
#include <iostream>

namespace exceptions
{
    class LexicException : public GeneralException
    {
    public:

        LexicException( std::string token );
        ~LexicException () throw() {}
        const char* what() const throw();

    private:
    };
}

#endif //LEXICEXCEPTION_H
