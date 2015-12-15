/*
 * File:   Syntactic.h
 * Author: Miguel Ochoa Hernandez
 *
 */

#ifndef SYNTACTIC_H
#define SYNTACTIC_H

#include <iostream>
#include <stack>
#include <map>
#include <memory>
#include <mutex>

#include "../../Include/namespaceStack/NonTerminal.h"
#include "../../Include/namespaceStack/GrammarElement.h"

typedef std::shared_ptr< stack::GrammarElement > Grammar_ptr;
typedef std::shared_ptr< stack::NonTerminal > NonTerminal_prt;

namespace analyzers
{
    class Syntactic
    {
      public:
        bool error;
        int **matrix;
        std::stack< Grammar_ptr > *stack;
        std::map< int,  NonTerminal_prt > rules;

        Syntactic();
        virtual ~Syntactic();

        std::string replace( std::string stream, char character, char replacement);
        void analyze(char *file_name);
        void read();
        int stackTop();
        void printStack();
        void print();

      private:
    };
}
#endif /* SYNTACTIC_H */
