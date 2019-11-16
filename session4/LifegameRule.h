
enum class State {
  Alive, Dead
};

class LifegameRule
{
public:
  LifegameRule();
  ~LifegameRule();

public:
   static State nextGeneration(State state, int num_of_alive_neighbours);
};
