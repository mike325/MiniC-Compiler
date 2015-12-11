/*
 * File:   StackElement.h
 * Author: Miguel Ochoa Hernandez
 *
 */

#ifndef STACKELEMENT_H
#define STACKELEMENT_H

#include <iostream>

namespace stack
{
    class StackElement
    {
      public:
        int state;

        StackElement();
        virtual ~StackElement();

        virtual void print();

      private:
    };
}
#endif /* STACKELEMENT_H */
