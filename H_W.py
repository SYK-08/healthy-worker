from audioplayer import AudioPlayer
import time

def music(file, stopper):
    player = AudioPlayer(file)
    player.play()
    while True:
        inp = input("Type here:")
        inp = inp.lower()
        if inp == stopper:
            player.stop()
            break

def log_water(msg1):
    with open("health-log-water.txt", 'a') as f:
        f.write(f"{msg1}: {time.asctime(time.localtime())}\n")

def log_phy(msg2):
    with open("health-log-ex.txt", 'a') as g:
        g.write(f"{msg2}: {time.asctime(time.localtime())}\n")

def log_eye(msg3):
    with open("health-log-eye.txt", 'a') as i:
        i.write(f"{msg3} {time.asctime(time.localtime())}\n")
    
if __name__ == "__main__":
    watersecs = 30*60 # Drink water every 30 mins
    physecs = 60*60 # Do exercise every 60 mins
    eyeexsecs = 45*60 # Do eye exercise every 45 mins
    init_water = time.time()
    init_eye = time.time()
    init_phy = time.time()

    while True:
        if time.time() - init_eye > eyeexsecs:
            print("Eye exercise time. Type 'eydone' to stop the alarm.")
            music("eyes.mp3", "eydone")
            init_eye = time.time() # eye exercise time reset
            log_eye("Eye exercise done") # logged eye exercise data
        
        if time.time() - init_water > watersecs:
            print("Drink some water. Type 'drank' to stop the alarm.")
            music("water.mp3", "drank")
            init_water = time.time() # water drinking time reset
            log_water("Drank water") # logged water drinking data

        if time.time() - init_phy > physecs:
            print("Exercise time. Type 'exdone' to stop the alarm.")
            music("exercise.mp3", "exdone")
            init_phy = time.time() # Physical exercise time reset
            log_phy("Exercise done")
            log("Drank water") # logged physical exercise data
