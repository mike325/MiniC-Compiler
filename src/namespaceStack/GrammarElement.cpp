/*
 * File:   GrammarElement.cpp
 * Author: Miguel Ochoa Hernandez
 *
 */

#include "../../Include/namespaceStack/GrammarElement.h"

stack::GrammarElement::GrammarElement() { this->state = 0; }
void stack::GrammarElement::print()
{
    std::cout << "The parent state is ";
    std::cout << this->state << std::endl;
}

std::ostream& operator<<(std::ostream &output, const stack::GrammarElement &element)
{
    output << "The parent state is ";
    output << element.state << std::endl;
    return output;
}