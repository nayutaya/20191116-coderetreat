
enum class State {
  Alive, Dead
};

class LifegameRule
{
public:
  LifegameRule();
  ~LifegameRule();

public:
   static State nextGeneration();
};
