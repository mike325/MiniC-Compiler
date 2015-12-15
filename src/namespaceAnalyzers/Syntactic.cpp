
#include <fstream>
#include <algorithm>
#include "../../Include/namespaceAnalyzers/Lexic.h"
#include "../../Include/namespaceAnalyzers/Syntactic.h"
#include "../../Include/namespaceStack/Terminal.h"
#include "../../Include/namespaceStack/State.h"
#include "../../Include/namespaceStack/NonTerminal.h"

typedef std::shared_ptr< stack::State > State_prt;
typedef std::shared_ptr< stack::Terminal > Terminal_prt;

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
            this->rules[i] = NonTerminal_prt(
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
                // check buffer characters
                sscanf( buffer, "%[^\t^\n]s", matrix_buffer );
                this->matrix[i][j] = atoi( matrix_buffer );
            }
            buffer[0] = '\0';
        }
    }
    grammar.close();

    this->stack->push( Terminal_prt( new stack::Terminal( "$" ) ));
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

std::string analyzers::Syntactic::replace( std::string stream, char character, char replacement)
{
    while(stream.find(character) != stream.npos)
    {
        int pos = stream.find_first_of(character);
        std::swap(stream[pos], replacement);
    }
    return stream;
}

void analyzers::Syntactic::analyze(char *file_name)
{
    analyzers::Lexic lexic;
    std::string lines = "", line_tail = "", copy_line_tail = "",stream_name(file_name);
    std::string buffer = "";
    int action = 0, finish = 0, head_state = 0;
    Grammar_ptr stack_head;

    std::ifstream source_code(file_name);

    if(!source_code.good())
    {
        std::cout << "Missing file\n\n";
    }
    else
    {
        while( !source_code.eof() || !std::getline(source_code, buffer) )
        {
            lines.append(buffer);
        }

        this->replace(lines, '\r', '\0');
        lines += '$';

        //this->print();

        lines = lexic.getToken(lines);
        copy_line_tail.assign(lines);

        while(!finish)
        {
            if(!lexic.error)
            {
                head_state = this->stack->top()->state;
                action = this->matrix[head_state][lexic.type];

                if(action == -1)
                {
                    finish = 0;
                }
                else if (action > 0)
                {
                    // stack::Terminal terminal (lexic.symbol);
                    this->stack->push( Terminal_prt(new stack::Terminal(lexic.symbol)) );
                    this->stack->push( State_prt(new stack::State(action)) );
                }
                else if(action < 0)
                {

                }
                else
                {
                    this->error = true;
                    //print syntactic error
                }
            }
            else
            {
                //print lexic error
            }
        }

        if(!lexic.error && this->error)
        {

        }
        else
        {

        }
    }

    source_code.close();
}

void analyzers::Syntactic::printStack()
{
    std::stack<Grammar_ptr> copy (*this->stack);

    std::string tab = "\t";
    std::cout << "Pila:     ";

    if(copy.size() < 7)
    {
        tab.push_back('\t');
    }

    for(unsigned int i = 0; i < copy.size(); i++)
    {
        Grammar_ptr stack_head = copy.top();
        stack_head->print();
        copy.pop();
    }
}


/*

void analyzers::Syntactic::read();
int analyzers::Syntactic::stackTop();
void analyzers::Syntactic::print();
*/
