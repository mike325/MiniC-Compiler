/*
 * File:   Terminal.h
 * Author: Miguel Ochoa Hernandez
 *
 */

#ifndef TERMINAL_H
#define TERMINAL_H

#include <iostream>
#include "StackElement.h"

namespace stack
{
    class Terminal : StackElement
    {
      public:
        Terminal();
        virtual ~Terminal();

      private:
    };
}

#endif /* TERMINAL_H */
