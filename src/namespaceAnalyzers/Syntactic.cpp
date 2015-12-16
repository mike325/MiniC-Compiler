
#include <fstream>
#include <algorithm>
#include "../../Include/namespaceAnalyzers/Lexic.h"
#include "../../Include/namespaceAnalyzers/Syntactic.h"

analyzers::Syntactic::Syntactic()
{
    this->error = false;
    // this->rules.clear();
    this->stack = new std::stack< Grammar_ptr >();

    std::ifstream grammar( "../../Grammar/compiler.lr" );

    if ( !grammar.good() )
    {
        std::cout << "There's a problem with the grammar file\n";
    }
    else
    {
        std::string simbol = "";
        int nonterminal_id = 0, reductions = 0;
        int colums = 0, rows = 0;
        int rule_number;
        char buffer[500], matrix_buffer[5];
        grammar.getline( buffer, 10, '\n' );
        rule_number = atoi( buffer );

        for ( int i = 0; i < rule_number; ++i )
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
            this->rules[i] =
                NonTerminal_prt( new stack::NonTerminal( nonterminal_id, reductions, simbol ) );
        }

        grammar.getline( buffer, 20, '\t' );
        colums = atoi( buffer );

        grammar.getline( buffer, 30, '\n' );
        rows = atoi( buffer );

        // matrix size
        this->matrix = new int *[rows];

        for ( int i = 0; i < colums; ++i )
        {
            this->matrix[i] = new int[colums];
        }

        for ( int i = 0; i < rows; ++i )
        {
            grammar.getline( buffer, 500, '\n' );
            // std::istringstream matrix_buffer( buffer );
            for ( int j = 0; j < colums; ++j )
            {
                // check buffer characters
                sscanf( buffer, "%[^\t^\n]s", matrix_buffer );
                this->matrix[i][j] = atoi( matrix_buffer );
            }
            buffer[0] = '\0';
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
    int size = sizeof( this->matrix[0] ) / sizeof( int );
    for ( int i = size - 1; i >= 0; ++i )
    {
        delete[] this->matrix[i];
    }
    delete[] this->matrix;
}

std::string analyzers::Syntactic::replace( std::string stream, char character, char replacement )
{
    while ( stream.find( character ) != stream.npos )
    {
        unsigned long pos = stream.find_first_of( character );
        std::swap( stream[pos], replacement );
    }
    return stream;
}

void analyzers::Syntactic::analyze( char *file_name )
{
    analyzers::Lexic lexic;
    std::string lines = "", line_tail = "";
    std::string buffer = "";
    int action = 0;
    bool finish = false;

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
                action     = this->matrix[this->stackTop()][lexic.type];

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

int analyzers::Syntactic::stackTop()
{
    return this->stack->top()->state;
}

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
