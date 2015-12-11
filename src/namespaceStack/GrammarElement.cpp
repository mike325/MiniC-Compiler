/*
 * File:   GrammarElement.cpp
 * Author: Miguel Ochoa Hernandez
 *
 */

#include "../../Include/namespaceStack/GrammarElement.h"

stack::GrammarElement::GrammarElement() { this->state = 0; }
stack::GrammarElement::~GrammarElement() { this->state = 0; }
void stack::GrammarElement::print()
{
    std::cout << "The parent state is ";
    std::cout << this->state << std::endl;
}
