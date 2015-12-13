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
    this->nontermial_simbol = "";
}

stack::NonTerminal::NonTerminal( int id, int reductions, std::string nontermial_simbol )
    : GrammarElement()
{
    this->id         = id;
    this->reductions = reductions;
    this->nontermial_simbol.assign( nontermial_simbol );
}

stack::NonTerminal::~NonTerminal()
{
    this->id                = 0;
    this->reductions        = 0;
    this->nontermial_simbol = "";
}

void stack::NonTerminal::print()
{
    std::cout << "NonTerminal id " << this->id << std::endl;
    std::cout << "NonTerminal reductions " << this->reductions << std::endl;
    std::cout << "NonTerminal simbol " << this->nontermial_simbol << std::endl;
}