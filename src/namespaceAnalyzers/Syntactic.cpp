/*
 * File:   Syntactic.cpp
 * Author: Miguel Ochoa Hernandez
 *
 */

#include <fstream>
#include <cstdlib>
#include "../../Include/namespaceAnalyzers/Syntactic.h"
#include "../../Include/namespaceStack/GrammarElement.h"

analyzers::Syntactic::Syntactic()
{
    this->error = false;
    // this->rules.clear();
    this->stack = new std::stack< stack::GrammarElement >();

    std::ifstream grammar( "../../Grammar/compiler.lr" );

    if ( !grammar.good() )
    {
        std::cout << "There's a problem with the grammar file\n";
    }
    else
    {
        unsigned int rule_number = 0;
        char read[500];
        grammar.getline( read, 10, '\n' );
        rule_number = atoi( read );
    }
    grammar.close();
}
analyzers::Syntactic::~Syntactic()
{
    this->error = false;
    this->rules.clear();
    delete this->stack;
}

/*
void analyzers::Syntactic::analyze();
void analyzers::Syntactic::read();
int analyzers::Syntactic::stackTop();
void analyzers::Syntactic::printStack();
void analyzers::Syntactic::print();
*/
