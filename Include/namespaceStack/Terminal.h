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
        std::string terminal;

        Terminal();
        Terminal( std::string temrinal );
        virtual ~Terminal();

        void print();

      private:
    };
}

#endif /* TERMINAL_H */
