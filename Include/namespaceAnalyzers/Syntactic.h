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

namespace analyzers
{
    class Syntactic
    {
      public:
        bool error;
        int **matrix;
        std::stack< std::shared_ptr< stack::GrammarElement > > *stack;
        std::map< int, std::shared_ptr< stack::NonTerminal > > rules;

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
