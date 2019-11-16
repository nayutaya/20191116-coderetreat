#include <CppUTest/CommandLineTestRunner.h>
#include <CppUTest/TestHarness.h>
#include "LifegameRule.h"
TEST_GROUP(LifegameRuleTest)
{
};

TEST(LifegameRuleTest, 死んでいるセルに隣接する生きたセルが3つだと誕生する)
{
  LifegameRule::nextGeneration(State::Dead, 0);
}
