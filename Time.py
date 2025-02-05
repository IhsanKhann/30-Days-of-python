import time #Learning the Time-Module:

def WhileLoop(n):
    total = 0
    i = 0
    while i<n:
        total = i+1
        i = i+1
    return total

def ForLoop(n):
    total = 0
    for i in range(n):
        total = i+1
    return total
    

start = time.time() #start time calculation
num = 10000000
# time.sleep(2) #2 seconds Delay..
WhileLoop(10000)
end = time.time() #stop time calculation

Elapsed_Time = end - start #Calculated Time.
print(f"The elapsed time is: ", Elapsed_Time)

print(f"The current time is:" , time.localtime())
# Formatting the time: time.strftime(" %Y-%M-%W %H:%M:%S" , t)
t = time.localtime()
Formatted_time = time.strftime(" %Y-%M-%W %H:%M:%S", t) #this is syntax
print("Formatted time is: ", Formatted_time)

st = time.perf_counter() 
ForLoop(1000000) 
ed = time.perf_counter()

print(f"The time is: {(ed-st):2F} ")

#Code: 
def play_song(lyrics):
    """
    Prints song lyrics with time intervals.
    
    :param lyrics: A list of tuples (lyric_line, delay_in_seconds)
    """
    for line, delay in lyrics:
        print(line)
        time.sleep(delay)  # Wait before printing the next line

# Lyrics for "Sanson Ki Mala Pe" with assumed timing (adjust as needed)
lyrics = [
    ("Sanson Ki Mala Pe Simru Main Pi Ka Naam", 4),
    ("Sanson Ki Mala Pe Simru Main Pi Ka Naam", 4),
    ("Apne Mann Ki Main Jaanu Aur Pi Ke Mann Ki Ram", 5),
    ("Sanson Ki Mala Pe Simru Main Pi Ka Naam", 4),
    ("Main Nahi Makhan Khayo", 3),
    ("Main Nahi Gopiyo Sang", 3),
    ("Main To Mari Jogan Re, Mo Se Nain Mila Yo Re", 5),
    ("Sanson Ki Mala Pe Simru Main Pi Ka Naam", 4),
]

# Play the song
play_song(lyrics)
