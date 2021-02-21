#ifndef PREPNTUPLEVARS_H
#define PREPNTUPLEVARS_H

#include "TestbeamReco/interface/Utility.h"

class PrepNTupleVars
{
private:
    void prepNTupleVars(NTupleReader& tr)
    {
        // Create the eventCounter variable to keep track of processed events
        int w = 1;
        tr.registerDerivedVar<int>("eventCounter",w);        
    }
public:
    PrepNTupleVars()
    {
    }

    void operator()(NTupleReader& tr)
    {
        prepNTupleVars(tr);
    }
};

#endif
