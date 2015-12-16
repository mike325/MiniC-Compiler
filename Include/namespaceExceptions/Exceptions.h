//
// Created by mike on 16/12/15.
//

#ifndef EXCEPTIONS_H
#define EXCEPTIONS_H

#include <iostream>

namespace exceptions
{
    class Exception : public std::exception
    {
      public:
        Exception( std::string message ) : exception( ), message( message ) {}
        ~Exception() throw();
        const char* what() const throw();

      private:
        std::string message;
    };
}

#endif  // EXCEPTIONS_H
