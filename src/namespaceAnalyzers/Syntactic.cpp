
#include <fstream>
#include <cstdlib>
#include <cstdio>
#include "../../Include/namespaceAnalyzers/Syntactic.h"
#include "../../Include/namespaceStack/GrammarElement.h"
#include "../../Include/namespaceStack/NonTerminal.h"
#include "../../Include/namespaceStack/Terminal.h"
#include "../../Include/namespaceStack/State.h"

analyzers::Syntactic::Syntactic()
{
    this->error = false;
    // this->rules.clear();
    this->stack = new std::stack< std::shared_ptr< stack::GrammarElement > >();

    std::ifstream grammar( "../../Grammar/compiler.lr" );

    if ( !grammar.good() )
    {
        std::cout << "There's a problem with the grammar file\n";
    }
    else
    {
        std::string simbol = "";
        int nonterminal_id = 0, reductions = 0;
        unsigned int rule_number = 0, colums = 0, rows = 0;
        char buffer[500], matrix_buffer[5];
        grammar.getline( buffer, 10, '\n' );
        rule_number = atoi( buffer );

        for ( int i = 0; i < ( int )rule_number; ++i )
        {
            grammar.getline( buffer, 20, '\t' );
            nonterminal_id = atoi( buffer );

            grammar.getline( buffer, 20, '\t' );
            reductions = atoi( buffer );

            grammar.getline( buffer, 30, '\n' );
            simbol.assign( buffer );

            // try with pointers
            // this->rules[i] = new stack::NonTerminal( nonterminal_id, reductions, simbol );

            // stack::NonTerminal new_nonterminal( nonterminal_id, reductions, simbol );
            // this->rules[i] = new_nonterminal;
            this->rules[i] = std::shared_ptr< stack::NonTerminal >(
                new stack::NonTerminal( nonterminal_id, reductions, simbol ) );
        }

        grammar.getline( buffer, 20, '\t' );
        colums = atoi( buffer );

        grammar.getline( buffer, 30, '\n' );
        rows = atoi( buffer );

        // matrix size
        this->matrix = new int*[rows];

        for ( unsigned int i = 0; i < colums; ++i )
        {
            this->matrix[i] = new int[colums];
        }

        for ( unsigned int i = 0; i < rows; ++i )
        {
            grammar.getline( buffer, 500, '\n' );
            // std::istringstream matrix_buffer( buffer );
            for ( unsigned int j = 0; j < colums; ++j )
            {
                sscanf( buffer, "%[^\t^\n]s", matrix_buffer );
                this->matrix[i][j] = atoi( matrix_buffer );
            }
            buffer[0] = '\0';
        }
    }
    grammar.close();

    this->stack->push( std::shared_ptr< stack::Terminal >( new stack::Terminal( "$" ) ) );
    this->stack->push( std::shared_ptr< stack::State >( new stack::State( 0 ) ) );
}

analyzers::Syntactic::~Syntactic()
{
    this->error = false;
    this->rules.clear();
    delete this->stack;
    // not finished yet
    int size = sizeof( this->matrix[0] ) / sizeof( int );
    for ( int i = size - 1; i >= 0; ++i )
    {
        delete[] this->matrix[i];
    }
    delete[] this->matrix;
}

/*
void analyzers::Syntactic::analyze();
void analyzers::Syntactic::read();
int analyzers::Syntactic::stackTop();
void analyzers::Syntactic::printStack();
void analyzers::Syntactic::print();
*/
