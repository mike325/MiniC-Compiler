/*
 * File:   StackElement.cpp
 * Author: Miguel Ochoa Hernandez
 *
 */

#include "../../Include/namespaceStack/StackElement.h"

stack::StackElement::StackElement() { this->state = 0; }
stack::StackElement::~StackElement() { this->state = 0; }
void stack::StackElement::print()
{
    std::cout << "The parent state is ";
    std::cout << this->state << std::endl;
}
