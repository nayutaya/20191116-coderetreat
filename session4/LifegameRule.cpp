#include "LifegameRule.h"
LifegameRule::LifegameRule()
{
  
}
LifegameRule::~LifegameRule()
{

}
State LifegameRule::nextGeneration(State state, int num_of_alive_neighbours)
{
  return State::Dead;
}
