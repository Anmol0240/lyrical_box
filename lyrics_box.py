import time
import sys
lyrics = [
    ("So I'ma love you every night like it's the last night", 0.0),  #   39 seconds
    ("Like it's the last night", 4.0),  #   43 seconds
    ("If the world was ending", 2.0),  #   45 seconds
    ("I'd wanna be next to you", 10.0),  # 9 seconds
    ("If the party was over", 16.0),  #   54 seconds
    ("and our time on earth was through", 3.0),  #   57 seconds
    ("I'd wanna hold you just for a while", 25.0),  #  1:03 minutes
    ("and die with a smile", 30.0),  #   1:08 minutes
    ("If the world was ending I'd wanna be next to you", 34.0),  #   1:12 minutes
    ("............................", 38.0),  #   1:16 minutes
    ("...................................", 42.0),  #   1:20 minutes
]

def print_lyrics_slowly(lyrics, start_offset=0, char_delay=0.08):
    
    start_time = time.time()
    for line, relative_start in lyrics:
        # Calculate the actual start time for this line
        actual_start = start_offset + relative_start
        # Wait until the actual start time for this line
        while time.time() - start_time < actual_start:
            time.sleep(0.01)
        # Print the line character by character
        for char in line:
            print(char, end='', flush=True)
            time.sleep(char_delay)  # Adjust this delay for slower typing
        print()  # Newline after each line

# Call the function to print lyrics slowly
print_lyrics_slowly(lyrics)
