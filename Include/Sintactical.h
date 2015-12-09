/*
 * File:   Sintactical.h
 * Author: Miguel Ochoa Hernandez
 *
 */

#ifndef SINTACTICAL_H
#define SINTACTICAL_H

#include <iostream>

namespace analyzers
{
    class Sintactical
    {
      public:
        Sintactical();
        virtual ~Sintactical();

        void analyze();
        void read();

      private:
    };
}
#endif /* SINTACTICAL_H */
