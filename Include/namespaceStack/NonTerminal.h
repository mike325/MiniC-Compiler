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
        NonTerminal();
        virtual ~NonTerminal();

      private:
    };
}

#endif /* NONTERMINAL_H */
