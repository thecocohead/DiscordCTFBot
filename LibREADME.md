#How to use CalLib.py
CalLib currently has 4 functions:

- `calendar` is used in other functions.
    - Output: List, three items long. Each item of the list is a sublist for each event. The output is [Start times, End times, Summaries]
        - Example: [[010101T010101Z, 010101T010101Z], [010101T010101Z, 010101T010101Z], [Test Event1, Test Event2]]
- `isEvent` returns the current event.
    - Output: String, current summary of the event. If there is no event, false is returned.
        - Example: 'Test Event'
- `nextEvent` returns the next events.
    - Output: String. Most likely multi-line, meant to be parsed in Discord. Contains times and summaries of the next events. If there are no future events, a blank string is returned.
        - Example: 'Test Event starts in 2 days, 07:01:01 \n Test Event1 starts in 3 days, 05:01:01 \n'
- `startEnd` returns the current event's time since start and end.
    - Output: List, two items long. Index 0 is the time since start, in seconds. Index 1 is the time until end, in seconds. If there is no current event, [0, 0] is returned.
        - Example: [1050, 1029]
       
##Current Limitations
- Two events can't overlap.