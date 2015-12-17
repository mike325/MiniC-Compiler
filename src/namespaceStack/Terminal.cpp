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
void stack::Terminal::print()
{
    std::cout << "Terminal state " << this->state << std::endl;
    std::cout << "Terminal simbol " << this->symbol << std::endl;
}

std::ostream& operator<<(std::ostream &output, const stack::Terminal &element)
{
    output << "Terminal state " << element.state << std::endl;
    output << "Terminal simbol " << element.symbol << std::endl;

    return output;
}