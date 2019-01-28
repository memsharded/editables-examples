#include "say.h"
#include "hello.h"

void hello(){
    #ifdef NDEBUG
    say("Hello World Release!");
    #else
    say("Hello World Debug!");
    #endif
}
