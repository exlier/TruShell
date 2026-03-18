def clock_ascii_1(hour, minutes):
    template1 = """
     ___
    |---|
    |_|_|
    |   |
    |   |
    |   |
    |   |
    |   |
    |___|
   /_____\\
   |HH:MM|
   |_____|
   |.....|
   \ ___ /
    |   |
    |   |
    |   |
    | . |
    | . |
    | . | 
    | . |
    | . |
    | . |
    | . |
    | . |
    |___|

        """
    clock_ascii = template1.replace("HH", f"{hour}")
    clock_ascii = clock_ascii.replace("MM", f"{minutes}")

    return clock_ascii
