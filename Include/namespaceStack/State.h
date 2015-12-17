/*
 * File:   State.h
 * Author: Miguel Ochoa Hernandez
 *
 */

#ifndef STATE_H
#define STATE_H

#include <iostream>
#include "GrammarElement.h"

namespace stack
{
    class State : public GrammarElement
    {
      public:
        State();
        State( int state );
        ~State() {}

        void print();
        friend std::ostream& operator<<(std::ostream &output, const State &element);

      private:
    };
}

#endif /* STATE_H */
