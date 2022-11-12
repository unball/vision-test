Feature: Get robot position

    Scenario Outline: Image Extraction
        Given I have the <image>
        When I calc the robot positions
        Then It should have the <position>

        Examples:
            | image       | position              |
            | path1.png   | ((0,0), (0,0), (0,0)) |