/*
 * File:   Terminal.h
 * Author: Miguel Ochoa Hernandez
 *
 */

#ifndef TERMINAL_H
#define TERMINAL_H

#include <iostream>
#include "GrammarElement.h"

namespace stack
{
    class Terminal : public GrammarElement
    {
      public:
        std::string symbol;

        Terminal();
        Terminal( std::string symbol );
        virtual ~Terminal();

        void print();
        friend std::ostream& operator<<(std::ostream &output, const Terminal &element);

      private:
    };
}

#endif /* TERMINAL_H */
