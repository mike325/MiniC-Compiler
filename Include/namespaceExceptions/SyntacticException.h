//
// Created by mike on 17/12/15.
//

#ifndef SYNTACTICEXCEPTION_H
#define SYNTACTICEXCEPTION_H

#include "../../Include/namespaceExceptions/GeneralException.h"
#include <iostream>

namespace exceptions
{
    class SyntacticException : public GeneralException
    {
    public:

        SyntacticException( std::string line );
        ~SyntacticException () throw() {}
        const char* what() const throw();

    private:
    };
}

#endif //SYNTACTICEXCEPTION_H
