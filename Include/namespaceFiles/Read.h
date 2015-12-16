/*
 * File:   Read.h
 * Author: Miguel Ochoa Hernandez
 *
 */

#ifndef READ_H
#define READ_H

#include <iostream>

namespace files
{
    class Read
    {
      public:
        std::string name;
        Read();
        virtual ~Read();
        void readFile();
        char* assignName( char* name );

      private:
    };
}

#endif /* READ_H */
