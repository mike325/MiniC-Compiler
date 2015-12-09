/*
 * File:   Read.h
 * Author: Miguel Ochoa Hernandez
 *
 */

#ifndef READ_H
#define READ_H

#include <iostream>

class Read
{
  public:
    std::string name;
    Read();
    virtual ~Read();
    void readFile();
    char* assingName( char* name );

  private:
};

#endif /* READ_H */
