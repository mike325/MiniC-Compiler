/*
 * File:   Sintactical.h
 * Author: Miguel Ochoa Hernandez
 *
 */

#ifndef SINTACTICAL_H
#define SINTACTICAL_H

#include <iostream>
#include <stack>
#include <map>

namespace analyzers
{
    class Sintactical
    {
      public:
        bool error;
        int **matrix;
        // std::stack<GrammarElement> elements_stack;
        // std::map <int, NotTerminal> rules;

        Sintactical();
        virtual ~Sintactical();

        void analyze();
        void read();
        int stackTop();
        void printStack();
        void print();

      private:
    };
}
#endif /* SINTACTICAL_H */
