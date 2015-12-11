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
#include "../../Include/namespaceStack/NonTerminal.h"
#include "../../Include/namespaceStack/GrammarElement.h"

namespace analyzers
{
    class Syntactic
    {
      public:
        bool error;
        int **matrix;
        std::stack< stack::GrammarElement > elements_stack;
        std::map< int, stack::NonTerminal > rules;

        Syntactic();
        virtual ~Syntactic();

        void analyze();
        void read();
        int stackTop();
        void printStack();
        void print();

      private:
    };
}
#endif /* SYNTACTIC_H */
