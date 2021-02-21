#include "TestbeamReco/interface/SATException.h"

#include <iostream>

SATException::SATException(const int line, const std::string function, const std::string file, const std::string message) : line_(line), funcion_(function), file_(file), message_(message)
{
}

void SATException::print() const
{
    std::cout << file_ << ":" << line_ << ", in function \"" << funcion_ << "\" -- " << message_ << std::endl;
}

std::ostream& operator<<(std::ostream& out, const SATException& e)
{
    return out << e.getFileName() << ":" << e.getLineNumber() << ", in function \"" << e.getFunctionName() << "\" -- " << e.getMessage();
}
