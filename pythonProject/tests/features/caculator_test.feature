Feature: Test online calculator scenarios
  As a User I want to execute calculator with operators
  Given I open Calculator Page
  When I switch to default full iframe

  @functionaltest @singleoperator
  Scenario Outline: Verify to calculate when input single operator with Addition,Subtraction, Division
    When I input value into Calculator = "<number1>"
    And I input operator into Calculator = "<operator1>"
    And I input value into Calculator = "<number2>"
    And I input value into Calculator = "KEYS.EQUALS"
    Then It should be shown result "<expected_result>"
    And I switch to default iframe
    Examples:
      | number1 | operator1     | number2 | expected_result |
      | 0       | Keys.ADD      | 0       | 1               |
      | 0       | Keys.ADD      | 9       | 9               |
      | 25      | Keys.ADD      | 25      | 50              |
      | 99999   | Keys.ADD      | 99999   | 199998          |
      | -50     | Keys.ADD      |         | -100            |
      | 0       | Keys.SUBTRACT | 99      | -99             |
      | 0       | Keys.SUBTRACT | -10     | 10              |
      | -100    | Keys.SUBTRACT | 100     | -200            |
      | -50     | Keys.SUBTRACT |         | 0               |
      | 0       | Keys.DIVIDE   | 99999   | 0               |
      | -0      | Keys.DIVIDE   | 99999   | 0               |
      | 10      | Keys.DIVIDE   | 2       | 5               |
      |         | Keys.ADD      |         | 0               |
      | 99      | Keys.ADD      |         | 198             |
      | 99      | Keys.SUBTRACT |         | 0               |
      |         | Keys.SUBTRACT | 99      | -99             |
      |         | Keys.SUBTRACT |         | 0               |
      | 99999   | Keys.DIVIDE   | 0       | Error           |
      |         | Keys.DIVIDE   | 0       | Error           |
      |         | Keys.DIVIDE   | 9999    | 0               |

  @functionaltest @multipleoperator
  Scenario Outline: Verify to calculate when input multiple operator with Addition,Subtraction, Division
    When I input value into Calculator = "<value1>"
    And I input value into Calculator = "<value2>"
    And I input value into Calculator = "<value3>"
    And I input value into Calculator = "<value4>"
    And I input value into Calculator = "<value5>"
    And I input value into Calculator = "<value6>"
    Then It should be shown result "<expected_result>"
    And I switch to default iframe
    Examples:
      | value1        | value2        | value3        | value4        | value5        | value6      | expected_result |
      | Keys.ADD      | 0             | Keys.SUBTRACT | Keys.ADD      | 99            | KEYS.EQUALS | 99              |
      | Keys.SUBTRACT | 99            | Keys.DIVIDE   | 2             | Keys.SUBTRACT | KEYS.EQUALS | 0               |
      | Keys.DIVIDE   | 50            | Keys.ADD      | Keys.SUBTRACT | 5             | KEYS.EQUALS | -5              |
      | Keys.ADD      | 10            | Keys.SUBTRACT | -9            | Keys.DIVIDE   | KEYS.EQUALS | 0               |
      | Keys.SUBTRACT | 99            | KEYS.EQUALS   | KEYS.EQUALS   | KEYS.EQUALS   |             | -297            |
      | Keys.DIVIDE   | 10            | Keys.ADD      | 6             | Keys.SUBTRACT | KEYS.EQUALS | 0               |
      | Keys.ADD      | 10            | KEYS.EQUALS   | KEYS.EQUALS   | KEYS.EQUALS   |             | 30              |
      | 99            | Keys.SUBTRACT | Keys.SUBTRACT | 99            |               | KEYS.EQUALS | 0               |
      | 99            | Keys.SUBTRACT | Keys.ADD      | 99            |               | KEYS.EQUALS | 198             |
      | 100           | Keys.SUBTRACT | Keys.DIVIDE   | 10            |               | KEYS.EQUALS | 10              |
      | 20            | Keys.ADD      | 10            | Keys.DIVIDE   | 4             | KEYS.EQUALS | 22.5            |
      | 100           | Keys.DIVIDE   | 5             | KEYS.EQUALS   | KEYS.EQUALS   |             | 4               |


  @functionaltest @floattype
  Scenario Outline: Verify Calculate with Float Number
    When I input value into Calculator = "<number1>"
    And I input value into Calculator = "<operator1>"
    And I input value into Calculator = "<number2>"
    And I input value into Calculator = "Keys.EQUAL"
    Then It should be shown result "<expected_result>"
    And I switch to default iframe
    Examples:
      | number1  | operator1     | number2 | expected_result |
      | 0.1      | Keys.ADD      | 0       | 0.1             |
      | 0.9      | Keys.SUBTRACT | 0.1     | 0.8             |
      | 1.9      | Keys.SUBTRACT | 2       | -01             |
      | 0.4      | Keys.DIVIDE   | 1000000 | 0.0000004       |
      | 10       | Keys.DIVIDE   | 2       | 5               |
      | 0.999999 | Keys.DIVIDE   | 0       | Error           |

  @functionaltest @boundary
  Scenario Outline: Verify Calculate with Boundary Case
    When I input value into Calculator = "<number1>"
    And I input value into Calculator = "<number2>"
    And I input value into Calculator = "<operator>"
    And I input value into Calculator = "Keys.EQUALS"
    Then It should be shown result "<expected_result>"
    And I switch to default iframe
    Examples:
      | number1   | operator      | number2   | expected_result |
      | 000000000 | Keys.ADD      | 00000001  | 1               |
      | 999999999 | Keys.ADD      | 1         | 1e+9            |
      | 999999999 | Keys.SUBTRACT | 900000000 | 99999999        |
      | 999999999 | Keys.ADD      | 0         | 999999999       |
