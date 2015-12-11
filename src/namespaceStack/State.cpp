/*
 * File:   State.cpp
 * Author: Miguel Ochoa Hernandez
 *
 */

#include "../../Include/namespaceStack/State.h"

stack::State::State() : StackElement() { this->state = 0; }
stack::State::State( int state ) : StackElement() { this->state = state; }
stack::State::~State() { this->state = 0; }
void stack::State::print()
{
    std::cout << "State state ";
    std::cout << this->state << std::endl;
}