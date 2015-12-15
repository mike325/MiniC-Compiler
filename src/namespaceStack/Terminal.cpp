/*
 * File:   Terminal.cpp
 * Author: Miguel Ochoa Hernandez
 *
 */

#include "../../Include/namespaceStack/Terminal.h"

stack::Terminal::Terminal() : GrammarElement() { this->symbol = ""; }
stack::Terminal::Terminal( std::string symbol ) : GrammarElement()
{
    this->symbol.assign( symbol );
}
stack::Terminal::~Terminal() { this->symbol = ""; }
void stack::Terminal::print()
{
    std::cout << "Terminal state " << this->state << std::endl;
    std::cout << "Terminal simbol " << this->symbol << std::endl;
}