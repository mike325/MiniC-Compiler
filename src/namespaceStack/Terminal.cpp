/*
 * File:   Terminal.cpp
 * Author: Miguel Ochoa Hernandez
 *
 */

#include "../../Include/namespaceStack/Terminal.h"

stack::Terminal::Terminal() : StackElement() { this->terminal = ""; }
stack::Terminal::Terminal( std::string terminal ) : StackElement()
{
    this->terminal.assign( terminal );
}
stack::Terminal::~Terminal() { this->terminal = ""; }
void stack::Terminal::print()
{
    std::cout << "Terminal state " << this->state << std::endl;
    std::cout << "Terminal simbol " << this->terminal << std::endl;
}