/*
 * File:   GrammarElement.h
 * Author: Miguel Ochoa Hernandez
 *
 */

#ifndef GrammarElement_H
#define GrammarElement_H

#include <iostream>

namespace stack
{
    class GrammarElement
    {
      public:
        int state;

        GrammarElement();
        virtual ~GrammarElement();

        virtual void print();

      private:
    };
}
#endif /* GrammarElement_H */
