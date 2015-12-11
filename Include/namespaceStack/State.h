/*
 * File:   State.h
 * Author: Miguel Ochoa Hernandez
 *
 */

#ifndef STATE_H
#define STATE_H

#include <iostream>
#include "StackElement.h"

namespace stack
{
    class State : public StackElement
    {
      public:
        State();
        virtual ~State();

      private:
    };
}

#endif /* STATE_H */
