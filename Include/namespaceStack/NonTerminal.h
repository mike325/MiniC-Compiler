/*
 * File:   NonTerminal.h
 * Author: Miguel Ochoa Hernandez
 *
 */

#ifndef NONTERMINAL_H
#define NONTERMINAL_H

#include <iostream>
#include "StackElement.h"

namespace stack
{
    class NonTerminal : public StackElement
    {
      public:
        int reductions;
        std::string nontermial_simbol;

        NonTerminal();
        NonTerminal( int state, int reductions, std::string nontermial_simbol );
        virtual ~NonTerminal();

        void print();

      private:
    };
}

#endif /* NONTERMINAL_H */
