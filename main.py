# KOI JOHNSON
# HUMOROGRAPHY GAME (TAKE 2)

# IMPORTS
import random
import pygame
import os

import textwrap

# For WebAssembly
import asyncio


async def main ():

    # LOAD DAD JOKE FILE

    joke = []
    answer = []

    with open('dadJokes.csv', 'r') as jokeFile:
        for line in jokeFile:
            line = line.strip()
            line = line.split(",")
            joke.append(line[0])
            answer.append(line[1])



    # Initialize Pygame
    pygame.mixer.pre_init(44100, -16, 2, 2048) # Optional: helps reduce sound lag
    
    pygame.init()

    # Screen dimensions
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 640
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("HUMOROGRAPHY")

    assert pygame.display.get_surface() is not None



    # Colors
    BLACK = (0, 0, 0)
    BUTTON1_COLOR = (255, 0, 0)
    BUTTON2_COLOR = (0, 255, 0)
    TEXT_COLOR = (255, 255, 255)

    # Font
    font = pygame.font.SysFont(None, 72)
    sfont = pygame.font.SysFont(None, 40)


    # LOAD RAND IMAGES FILE
    images = []
    try:
        with open('images.txt', 'r') as imgfile:
            for line in imgfile:
                # Strip whitespace/newlines, load image, and add to list
                path = line.strip()
                if os.path.exists(path):
                    img = pygame.image.load(path)
                    if img.get_alpha() is not None:
                        img = img.convert_alpha()
                    else:
                        img = img.convert()
                    images.append(img)
    except FileNotFoundError:
        print("Address file not found.")

    # LOAD STEM MEMES FILE
    stem = []
    try:
        with open('STEMmeme.txt', 'r') as stemfile:
            for line in stemfile:
                # Strip whitespace/newlines, load image, and add to list
                path = line.strip()
                if os.path.exists(path):
                    stem_meme = pygame.image.load(path)
                    if stem_meme.get_alpha() is not None:
                        stem_meme = stem_meme.convert_alpha()
                    else:
                        stem_meme = stem_meme.convert()
                    stem.append(stem_meme)
    except FileNotFoundError:
        print("Address file not found.")

    # LOAD KPOP MEMES FILE
    kpop = []
    try:
        with open('kpop.txt', 'r') as kpopfile:
            for line in kpopfile:
                # Strip whitespace/newlines, load image, and add to list
                path = line.strip()
                if os.path.exists(path):
                    kpop_meme = pygame.image.load(path)
                    if kpop_meme.get_alpha() is not None:
                        kpop_meme = kpop_meme.convert_alpha()
                    else:
                        kpop_meme = kpop_meme.convert()
                    kpop.append(kpop_meme)
    except FileNotFoundError:
        print("Address file not found.")


    # LOAD SFX
    sfx = []
    with open('sfx.txt', 'r') as sfxfile:
        for line in sfxfile:
            line = line.strip()
            sfx.append(line)
                


    # RANDOM
        # Joke
    display = random.choice(joke)
    idx = joke.index(display)

        # Image
    random_image = pygame.transform.smoothscale(random.choice(images), (600, 450))
    random_stem = pygame.transform.smoothscale(random.choice(stem), (600, 450))
    random_kpop = pygame.transform.smoothscale(random.choice(kpop), (600, 450))


        # Sound
    random_sfx = random.choice(sfx)


    # LOAD AUDIO BUTTON
    audio = pygame.image.load('assets/audio.png')
    if audio.get_alpha() is not None:
        audio = audio.convert_alpha()
    else:
        audio = audio.convert()
    audio_rect = audio.get_rect()
    audio_rect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)



    # Button 1 properties (x, y, width, height)
    button_rect1 = pygame.Rect(50, 500, 200, 100)
    button_text1 = font.render("No", True, TEXT_COLOR)
    text_rect1 = button_text1.get_rect(center=button_rect1.center)

    # Button 2 properties (x, y, width, height)
    button_rect2 = pygame.Rect(390, 500, 200, 100)
    button_text2 = font.render("Yes", True, TEXT_COLOR)
    text_rect2 = button_text2.get_rect(center=button_rect2.center)




    # declarations
    non = 0
    laugh = 0

    show = False
    graph = False

    Lpercent = 0
    Npercent = 0

    sound_on = False
    hit = False
    level = 0

    silly_sound = None
    

    # Main game loop
    running = True
    while running:

        color1 = BUTTON1_COLOR  
        color2 = BUTTON2_COLOR

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the click was within the button's rectangle
                if button_rect1.collidepoint(event.pos):
                    non += 1
                    # New joke
                    display = random.choice(joke)
                    idx = joke.index(display)
                    show = False
                    if sound_on == True:
                        silly_sound.stop()
                        sound_on = False
                        hit = False
                    # New Image
                    random_image = pygame.transform.smoothscale(random.choice(images), (600, 450))
                    random_stem = pygame.transform.smoothscale(random.choice(stem), (600, 450))
                    random_kpop = pygame.transform.smoothscale(random.choice(kpop), (600, 450))
                    random_sfx = random.choice(sfx)
                         
                

                if button_rect2.collidepoint(event.pos):
                    laugh += 1
                    # New joke
                    display = random.choice(joke)
                    idx = joke.index(display)
                    show = False
                    if sound_on == True:
                        silly_sound.stop()
                        sound_on = False
                        hit = False
                    # New Image
                    random_image = pygame.transform.smoothscale(random.choice(images), (600, 450))
                    random_stem = pygame.transform.smoothscale(random.choice(stem), (600, 450))
                    random_kpop = pygame.transform.smoothscale(random.choice(kpop), (600, 450))  
                    random_sfx = random.choice(sfx)
                                            

                if hit == True:
                    if audio_rect.collidepoint(event.pos):    
                        silly_sound = pygame.mixer.Sound(random_sfx)
                        silly_sound.play()
                        sound_on = True
                        
                               

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    show = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    graph = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    graph = False

        # Drawing
        screen.fill(BLACK)
        
        pygame.draw.rect(screen, color1, button_rect1)
        pygame.draw.rect(screen, color2, button_rect2)

        # Draw the text on the button
        screen.blit(button_text1, text_rect1)
        screen.blit(button_text2, text_rect2)

        if graph == True:
            screen.fill(BLACK)

            # Graph Title
            title = font.render("Giggle Graph", True, TEXT_COLOR)
            screen.blit(title, (320-(title.get_width()/2), 50))

            total = laugh + non
            if total > 0:
                # percents
                Lpercent = laugh / total
                Npercent = non / total
            else:
                Lpercent = 0
                Npercent = 0
                

            # LAUGH BAR
            Lbar = pygame.Rect(100, 640-round(Lpercent*500), 200, round(Lpercent*500))
            pygame.draw.rect(screen, BUTTON2_COLOR, Lbar)

            # NON BAR
            Nbar = pygame.Rect(350, 640-round(Npercent*500), 200, round(Npercent*500))
            pygame.draw.rect(screen, BUTTON1_COLOR, Nbar)
        
            



        # Draw joke/answer
        # TEXT WRAP

        def wrap(surface, text, sfont, color, x, y, max_width):
            # Split text into lines that fit within max_width
            wrapped_lines = textwrap.wrap(text, width=max_width // (sfont.size(' ')[0] // 2))

            for i, line in enumerate(wrapped_lines):
                line_surf = sfont.render(line, True, color)
                surface.blit(line_surf, (x, y + i * sfont.get_height()))

            
          # change level 
        level = (laugh-non)//10   

        if level < 0:
            level = 0     


        if graph == False:
            if level == 0:
                wrap(screen, display, sfont, TEXT_COLOR, 10, 10, 150)

            if (show == True) and (level == 0):
                wrap(screen, answer[idx], sfont, TEXT_COLOR, 10, 200, 150)


            # DRAW IMAGES
            if level == 1:
                if images:
                    screen.blit(random_image, (10, 10))


            # DRAW STEM
            if level == 2:
                if stem:
                    screen.blit(random_stem, (10, 10))


            # SOUNDS
            if level == 3:
                screen.blit(audio, audio_rect)
                hit = True
                

            
            # DRAW KPOP
            if level >= 4:
                if kpop:
                    screen.blit(random_kpop, (10, 10))
        

        # Update the display
        pygame.display.flip()

        await asyncio.sleep(0)

    # Quit Pygame
    pygame.quit()
   # sys.exit()

asyncio.run(main())
