/*
 * File:   Syntactic.cpp
 * Author: Miguel Ochoa Hernandez
 *
 */

#include <fstream>
#include <cstdlib>
#include "../../Include/namespaceAnalyzers/Syntactic.h"
#include "../../Include/namespaceStack/GrammarElement.h"
#include "../../Include/namespaceStack/NonTerminal.h"

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
        std::string simbol = "";
        int nonterminal_id = 0, reductions = 0;
        unsigned int rule_number = 0;
        char read[500];
        grammar.getline( read, 10, '\n' );
        rule_number = atoi( read );

        for ( int i = 0; i < ( int )rule_number; ++i )
        {
            grammar.getline( read, 20, '\t' );
            nonterminal_id = atoi( read );

            grammar.getline( read, 20, '\t' );
            reductions = atoi( read );

            grammar.getline( read, 30, '\n' );
            simbol.assign( read );

            // try with pointers
            // this->rules[i] = new NonTerminal( nonterminal_id, reductions,simbol );

            stack::NonTerminal new_nonterminal( nonterminal_id, reductions, simbol );
            this->rules[i] = new_nonterminal;
        }
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
