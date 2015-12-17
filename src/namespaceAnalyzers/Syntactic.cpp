
#include <fstream>
#include <algorithm>
#include <cstddef>    // std::size_t
#include "../../Include/namespaceAnalyzers/Lexic.h"
#include "../../Include/namespaceAnalyzers/Syntactic.h"
#include "../../Include/namespaceExceptions/FileException.h"

analyzers::Syntactic::Syntactic()
{
    this->error = false;
    // this->rules.clear();
    this->stack = new std::stack< Grammar_ptr >();

    std::ifstream grammar( "MiniC-Compiler/Grammar/compiler.lr" );

    if ( !grammar.good() )
    {
        std::cout << "There's a problem with the grammar file\n";
        std::string file_name( "compiler.lr" );
        throw exceptions::FileException( file_name );
    }
    else
    {
        std::string symbol = "", line = "";
        int nonterminal_id = 0, reductions = 0;
        int rows = 0, colums = 0;
        int rule_number;
        // char buffer[500], matrix_buffer[5];
        getline( grammar, line );
        rule_number = atoi( line.c_str() );

        for ( int i = 0; i < rule_number; ++i )
        {
            getline( grammar, line, '\t' );
            nonterminal_id = atoi( line.c_str() );

            getline( grammar, line, '\t' );
            reductions = atoi( line.c_str() );

            getline( grammar, line );
            symbol.assign( line );

            // try with pointers
            // this->rules[i] = new stack::NonTerminal( nonterminal_id, reductions, simbol );

            // stack::NonTerminal new_nonterminal( nonterminal_id, reductions, simbol );
            // this->rules[i] = new_nonterminal;
            this->rules[i]
                = NonTerminal_prt( new stack::NonTerminal( nonterminal_id, reductions, symbol ) );
        }

        getline( grammar, line, '\t' );
        rows = atoi( line.c_str() );

        getline( grammar, line );
        colums = atoi( line.c_str() );

        // matrix size
        this->matrix = new int *[rows];

        for ( int i = 0; i < rows; ++i )
        {
            this->matrix[i] = new int[colums];
        }

        for ( int i = 0; i < rows; ++i )
        {
            getline( grammar, line );
            // line = this->replace( line, '\t', ' ' );
            // std::cout << line << "\n";
            std::size_t pos = 0;
            for ( int j = 0; j < colums; ++j )
            {
                if ( pos != std::string::npos && pos < line.size() )
                {
                    std::string stream( line.substr( pos, line.find_first_of( " \t\n\r" ) ) );
                    this->matrix[i][j] = atoi( stream.c_str() );
                    pos = line.find_first_not_of( " \t\n\r", line.find_first_of( " \t\n\r" ) );
                    if ( pos != std::string::npos && pos < line.size() )
                    {
                        line = line.substr( pos );
                    }
                }
                else
                {
                    this->matrix[i][j] = atoi( line.c_str() );
                    break;
                }
            }
        }
    }
    grammar.close();

    this->stack->push( Terminal_prt( new stack::Terminal( "$" ) ) );
    this->stack->push( State_prt( new stack::State( 0 ) ) );
}

analyzers::Syntactic::~Syntactic()
{
    this->error = false;
    this->rules.clear();
    delete this->stack;
    // not finished yet
    /*
    int size = sizeof( this->matrix[0] ) / sizeof( int );
    for ( int i = 0; i < size; i++ )
    {
        delete[] this->matrix[i];
    }
    delete[] this->matrix;
      */
}

std::string analyzers::Syntactic::replace( std::string stream, char character, char replacement )
{
    for ( unsigned int i = 0; i < stream.size(); ++i )
    {
        if ( stream[i] == character )
        {
            stream[i] = replacement;
        }
    }
    return stream;
}

void analyzers::Syntactic::analyze( char *file_name )
{
    analyzers::Lexic lexic;
    std::string lines = "", line_tail = "";
    std::string buffer = "";
    int action         = 0;
    bool finish        = false;

    std::ifstream source_code( file_name );

    if ( !source_code.good() )
    {
        std::cout << "Missing file\n\n";
    }
    else
    {
        while ( !source_code.eof() || !std::getline( source_code, buffer ) )
        {
            lines.append( buffer );
        }

        this->replace( lines, '\r', '\0' );
        lines += '$';

        // this->print();

        lines = lexic.getToken( lines );
        line_tail.assign( lines );

        while ( !finish )
        {
            if ( !lexic.error )
            {
                action = this->matrix[this->stackTop()][lexic.type];

                if ( action == -1 )
                {
                    finish = true;
                }
                else if ( action > 0 )
                {
                    // stack::Terminal terminal (lexic.symbol);
                    this->stack->push( Terminal_prt( new stack::Terminal( lexic.symbol ) ) );
                    this->stack->push( State_prt( new stack::State( action ) ) );
                    // this->print();
                    line_tail = lines;
                    lines     = lexic.getToken( lines );
                }
                else if ( action < 0 )
                {
                    int rule_number = ( action * -1 ) - 2;
                    if ( this->rules.find( rule_number ) != this->rules.end() )
                    {
                        NonTerminal_prt rule(
                            new stack::NonTerminal( this->rules.at( rule_number ) ) );

                        /* just for some tests */
                        for ( unsigned int i = 0; i < ( unsigned int )rule->reductions * 2; ++i )
                        {
                            this->stack->pop();
                        }
                        /* just for some tests */

                        action = this->matrix[this->stackTop()][rule->state];

                        this->stack->push( rule );
                        this->stack->push( State_prt( new stack::State( action ) ) );

                        // this->print();
                    }
                    else
                    {
                        std::cout << "Rule " << rule_number << "does not exist\n";
                        this->error = true;
                        finish      = true;
                    }
                }
                else
                {
                    this->error = true;
                    finish      = true;
                    // print syntactic error
                }
            }
            else
            {
                finish = true;
                // print lexic error
            }
        }

        if ( !lexic.error && !this->error )
        {
            // source code correct
            std::cout << "Correct\n";
        }
        else
        {
            std::cout << "Incorrect\n";
            // null
        }
    }

    source_code.close();
}

void analyzers::Syntactic::printStack()
{
    std::stack< Grammar_ptr > copy( *this->stack );

    std::string tab = "\t";
    std::cout << "Stack:     ";

    if ( copy.size() < 7 )
    {
        tab.push_back( '\t' );
    }

    while ( copy.size() > 0 )
    {
        Grammar_ptr stack_head = copy.top();
        stack_head->print();
        copy.pop();
    }
}

int analyzers::Syntactic::stackTop() { return this->stack->top()->state; }
void analyzers::Syntactic::print()
{
    std::cout << " State " << std::endl;
    // unfinished
    this->printStack();
    // unfinished
}

/*
void analyzers::Syntactic::read();
*/
