/*
 * File:   NonTerminal.cpp
 * Author: Miguel Ochoa Hernandez
 *
 */

#include "../../Include/namespaceStack/NonTerminal.h"

stack::NonTerminal::NonTerminal() : GrammarElement()
{
    this->id                = 0;
    this->reductions        = 0;
    this->nontermial_symbol = "";
}

stack::NonTerminal::NonTerminal( int id, int reductions, std::string nontermial_symbol )
    : GrammarElement()
{
    this->id         = id;
    this->reductions = reductions;
    this->nontermial_symbol.assign( nontermial_symbol );
}

stack::NonTerminal::NonTerminal( const std::shared_ptr< stack::NonTerminal > &copied_nonterminal )
{
    this->id         = copied_nonterminal->id;
    this->reductions = copied_nonterminal->reductions;
    this->nontermial_symbol.assign( copied_nonterminal->nontermial_symbol );
}

stack::NonTerminal::~NonTerminal()
{
    this->id                = 0;
    this->reductions        = 0;
    this->nontermial_symbol = "";
}

void stack::NonTerminal::print()
{
    std::cout << "NonTerminal id " << this->id << std::endl;
    std::cout << "NonTerminal reductions " << this->reductions << std::endl;
    std::cout << "NonTerminal simbol " << this->nontermial_symbol << std::endl;
}

std::ostream& operator<<(std::ostream &output, const stack::NonTerminal &element)
{
    output << "NonTerminal id " << element.id << std::endl;
    output << "NonTerminal reductions " << element.reductions << std::endl;
    output << "NonTerminal simbol " << element.nontermial_symbol << std::endl;

    return output;
}
