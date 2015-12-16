//
// Created by mike on 16/12/15.
//

#ifndef EXCEPTIONS_H
#define EXCEPTIONS_H

#include <iostream>

namespace exceptions
{
    class GeneralException : public std::exception
    {
    public:

        GeneralException ( ) : exception( ), message(""), description("Has been an usxpected error ") {}
        GeneralException ( std::string message, std::string description ) : exception( ), message( message ), description(description) {}
        virtual ~GeneralException () throw() {};
        virtual const char* what() const throw() { return this->description.c_str(); }

    protected:
        std::string message;
        std::string description;

    private:
    };
}

#endif  // EXCEPTIONS_H
