Feature: Calculator
  As a calculator user
  I want to perform basic arithmetic operations

  Scenario Outline: Adding two numbers
    Given I have a calculator
    When I add the numbers <a> and <b>
    Then the result should be <result>

    Examples:
      | a  | b  | result |
      | 2  | 3  | 5      |
      | -1 | 1  | 0      |

  Scenario Outline: Subtracting two numbers
    Given I have a calculator
    When I subtract <b> from <a>
    Then the result should be <result>

    Examples:
      | a  | b  | result |
      | 5  | 3  | 2      |
      | 0  | 4  | -4     |
      | 4  | 1  | 3      |

  Scenario Outline: Multiplying two numbers
    Given I have a calculator
    When I multiply the numbers <a> and <b>
    Then the result should be <result>

    Examples:
      | a  | b  | result |
      | 2  | 3  | 6      |
      | -2 | 3  | -6     |
