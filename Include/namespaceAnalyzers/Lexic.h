/*
 * File:   Lexic.h
 * Author: Miguel Ochoa Hernandez
 *
 */

#ifndef LEXIC_H
#define LEXIC_H

#include <iostream>
#include <map>

namespace analyzers
{
    class Lexic
    {
      public:
        std::string symbol;
        int type;
        bool error;

        Lexic();
        virtual ~Lexic();

        std::string deleteSpaces( std::string stream );
        std::string getToken( std::string stream );
        bool outLimit( std::string stream );
        void keywords( std::string stream );
        void consume( std::string stream );
        void nextState( std::string stream, int state );
        void identifier( std::string stream );
        void real( std::string stream );
        void integer( std::string stream );
        void string( std::string stream );
        void checkNext( std::string stream, char character, int state );
        void getType();
        void print();

      private:
        int state;
        unsigned int index;
        std::map< std::string, int > keyword;
    };
}

#endif /* LEXIC_H */
