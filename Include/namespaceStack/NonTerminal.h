/*
 * File:   NonTerminal.h
 * Author: Miguel Ochoa Hernandez
 *
 */

#ifndef NONTERMINAL_H
#define NONTERMINAL_H

#include <memory>
#include <iostream>
#include "GrammarElement.h"

namespace stack
{
    class NonTerminal : public GrammarElement
    {
      public:
        int reductions, id;
        std::string nontermial_symbol;

        NonTerminal();

        NonTerminal( const std::shared_ptr< stack::NonTerminal > &copied_nonterminal );

        NonTerminal( int id, int reductions, std::string nontermial_symbol );
        virtual ~NonTerminal();

        void print();
        friend std::ostream& operator<<(std::ostream &output, const NonTerminal &element);

      private:
    };
}

#endif /* NONTERMINAL_H */
