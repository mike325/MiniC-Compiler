/*
 * File:   State.cpp
 * Author: Miguel Ochoa Hernandez
 *
 */

#include "../../Include/namespaceStack/State.h"

stack::State::State() : GrammarElement() { this->state = 0; }
stack::State::State( int state ) : GrammarElement() { this->state = state; }
stack::State::~State() { this->state = 0; }
void stack::State::print()
{
    std::cout << "State state ";
    std::cout << this->state << std::endl;
}

std::ostream& operator<<(std::ostream &output, const stack::State &element)
{
    output << "State's state ";
    output << element.state << std::endl;

    return output;
}