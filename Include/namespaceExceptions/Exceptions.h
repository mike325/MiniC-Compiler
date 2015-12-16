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
            Exception(int mot) : exception(), motivo(mot) {}
            const char* what() const throw();
        private:
            int motivo;
    };
}

#endif  // EXCEPTIONS_H
