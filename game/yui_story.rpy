label yui_start_case_1:
    image kitchen = im.Scale("images/bg kitchen.webp", 1920, 1080)
    image outside = im.Scale("images/bg outside.webp", 1920, 1080)
    image aerial = im.Scale("images/school aerial.webp", 1920, 1080)
    image hallway = im.Scale("images/hallways.webp", 1920, 1080)
    image pools = im.Scale("images/pool.webp", 1920, 1080)
    image classroom lunch1 = im.Scale("images/classroom lunch.webp", 1920,1080)
    image classroom2 = im.Scale("images/classroom_2.webp",1920,1080)
    image classroom morning = im.Scale("images/classroom_morning.webp",1920,1080)
    image walk = im.Scale("images/walk1.webp", 1920, 1080)
    image school gate = im.Scale("images/school gate1.webp", 1920, 1080)

    define kk = Character('Kurtney',color='#51ceff')
    define y = Character('Yui',color='#f9b3ff')
    define t = Character('Teacher Clarisse')
    define b = Character('Butch')
    define o = Character('Officer Greg', color='#30ff45')
    define mc = Character("Mark")
    define m = Character("Me",color='#00ffea')

    default notebookOpen = False
    default hbbpoints = 0
    default yuiStoryProgress = 0
    default notebookIndex = 0
    define mm = Character('Mom',color='#00ff2a')
    default badEndingGame = False
    default kurtneyHelp = False
    default achievementList = [False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    default persistent.unlockroom = False
    default persistent.unlockTrain = False
    default persistent.unlockJeep = False
    default persistent.unlockHallway = False
    default persistent.unlockTrain2 = False
    default persistent.unlockWalk = False
    default persistent.unlockCafeteria = False
    default persistent.unlockClass = False
    default persistent.unlockYui = False
    default persistent.unlockKurtney = False
    define config.voice_filename_format = "audio/voice/{id}.ogg"

    init python:
        
        def subtractPoints():
            global hbbpoints
            if hbbpoints >= 1:
                hbbpoints -= 1
                play_sound(subPoints)
                "Your points are deducted by 1 HBB Point"

    #START OF YUI STORY
    stop music
    hide screen displayHBBPoints
    scene school gate with fade
    play music "audio/music/Piano6.ogg"
    show screen titleYui with dissolve
    pause 0.5
    
    $ persistent.unlockJeep = False
    $ persistent.unlockroom = False
    
    #Play iphone alarm tone
    pause 2.0
    hide screen titleYui with dissolve
    pause 0.5
    stop music
    
    $ play_sound (phone) 

    scene bg room2 with fade

    "{i}7:00 AM....{/i}"

    play sound "audio/voice/case1/blnk/line1.ogg"
    "Ugh...."

    python:

        if achievementList[0] == False:
        
            achievement.grant("A New Leaf")
            renpy.notify("Achievement Unlocked: A New Leaf")
            renpy.play("audio/sfx/achievement.ogg",channel="sound")
            achievementList[0] = True

    $ persistent.unlockroom = True


    play sound "audio/voice/case1/blnk/line2.ogg"
    "Shut up Siri."

    "......"
    $ timeout_label = "snooze"
    $ timeout = 10

    menu:

        "Snooze alarm for 5 minutes":
            jump snooze
            
        
        "Get up and fix the bed":
            
            $ play_music (rest, fadein=0.3) 
            
            scene bg room2 with dissolve

            play voice "audio/voice/case1/blnk/line3.ogg"
            "Another day, another dollar..."

            jump breakfastWithMom


label snooze:
    scene black

    play sound "audio/voice/case1/blnk/line4.ogg"
    "Just a few more minutes...."

    "Zzzzzz...."

    pause 2.0
    $ play_sound (phone)

    scene bg room2 with dissolve

    "{i}7:27 AM....{/i}"

    $ play_music (rest, fadein=0.3) 
    play sound "audio/voice/case1/me/m1.ogg"
    m "NO WAY!!! I ALMOST SLEPT FOR ANOTHER 30 MINUTES!"

    jump breakfastWithMom


label breakfastWithMom:

    scene bg room2 with fade

    play sound "audio/voice/case1/blnk/line5.ogg"
    "My name is {color=#00ffea}Markkuss{/color}. I know it is a weird name so I told my friends and family to just call me {color=#00ffea}Mark.{/color}"
    play sound "audio/voice/case1/blnk/line6.ogg"
    "Today is the day of me being a Second-Year highschool student."
    play sound "audio/voice/case1/blnk/line7.ogg"
    "I am your average highschool boy if you wanna know."
    play sound "audio/voice/case1/blnk/line8.ogg"
    "I barely pass my subjects but I'm also quite decent at sports."
    play sound "audio/voice/case1/blnk/line9.ogg"
    "Gotta brag when you gotta brag. Hahaha~"
    play sound "audio/voice/case1/blnk/line10.ogg"
    "Becoming an Attorney is my dream."
    play sound "audio/voice/case1/blnk/line11.ogg"
    "You know why?"
    play sound "audio/voice/case1/blnk/line12.ogg"
    "Cause I have played lots of detective games!"
    play sound "audio/voice/case1/blnk/line13.ogg"
    "Hahaha I know its nonsense but still..."
    play sound "audio/voice/case1/blnk/line14.ogg"
    "Anyways! My hobbies are sleeping and watching anime."
    play sound "audio/voice/case1/blnk/line15.ogg"
    "Wait is this even called hobbies? It's more of a \"I've got nothing else to do in life.\""
    play sound "audio/voice/case1/blnk/line16.ogg"
    "Well...."
    #play sound "audio/voice/case1/blnk/line16n17.ogg"
    "Nothing eventful has happened yet in my life."
    play sound "audio/voice/case1/blnk/line17.ogg"
    "I haven't even experienced the so called \"romance of highschool.\""
    play sound "audio/voice/case1/blnk/line18.ogg"
    "I wonder if it starts now? Hahaha~"

    "....."

    mm "Mark! Are you awake?"

    $ play_sound (doorknock) 
    pause 0.5
    with hpunch
    
    "....."
    $ play_sound (doorknock)
    pause 0.5
    with hpunch

    pause 3.0

    $ play_sound(yawn)
    play sound "audio/voice/case1/me/m2.ogg"
    m "Oh yes. It definitely starts with my mom's yelling in the morning."
    play sound "audio/voice/case1/me/m3.ogg"
    m "Yes mom... Please stop knocking on the door."

    show mom worried at left with dissolve

    mm "It's your first day at school honey..."

    mm "I told you to sleep early last night. Did you play games all night again?"
    play sound "audio/voice/case1/me/m4.ogg"
    m "Ehehe......"

    scene kitchen with fade
    show mom happy at left with dissolve

    mm "Go now and eat breakfast with me. Your father left early for work."
    play sound "audio/voice/case1/me/m5.ogg"
    m "What did you cook for breakfast [mm]?"

    show mom happy closed at left with dissolve
    mm "I made your favorite foods! A scrambled egg, tocino and some bacon."
    $ timeout_label = None
    hide mom happy with dissolve

    menu: 
        
        mm "What do you wanna eat?"

        "Scrambled eggs.":
            play sound "audio/voice/case1/me/m6.ogg"
            m "Nothing beats [mm]'s scrambled eggs."

        "Tocino":
            play sound "audio/voice/case1/me/m7.ogg"
            m "The sweet taste of tocino means a very good morning."

        "Bacon":
            play sound "audio/voice/case1/me/m8.ogg"
            m "Crispy and juicy bacon. The best breakfast food invented."

        "Of course, all of it!":
            m "All of these dishes in one plate..."
            play sound "audio/voice/case1/me/m9.ogg"
            m "I hope my stomach won't hurt when I'm outside. Haha...."

            python:
                if achievementList[1] == False:


                    achievement.grant("I Love Mom's Breakfast")
                    renpy.notify("Achievement Unlocked: I Love Mom's Breakfast")
                    renpy.play("audio/sfx/achievement.ogg",channel="sound")
                    achievementList[1] = True

            show mom worried with dissolve
            mm "I hope so too! Ahahaha~"
            hide mom worried with dissolve

    $ play_sound(eat,fadein=0.5)
    "{i}Munch munch munch....{\i}"
    pause 8
            
    play sound "audio/voice/case1/me/m10.ogg"
    m "Thank you for the food, Mom!"

    show mom happy at left with dissolve
    
    mm "No worries! It's gonna be a big day for you honey."

    "...."

    hide mom happy with dissolve
    $ law = ''
    menu:
        "I should first look at some news before leaving..."

        "Grab the newspaper.":
            $ play_sound (paper)
            pause 0.5
            $ law = 'paper'
            
            python:

                if achievementList[2] == False:
                
                    achievement.grant("Newspaper Guy")
                    renpy.notify("Achievement Unlocked: Newspaper Guy")
                    renpy.play("audio/sfx/achievement.ogg",channel="sound")
                    achievementList[2] = True

            jump law

        "Open the TV.":
            $ play_sound (tv)
            pause 0.5
            $ law = 'tv'
            python:

                if achievementList[3] == False:
                
                    achievement.grant("TV Guy")
                    renpy.notify("Achievement Unlocked: TV Guy")
                    renpy.play("audio/sfx/achievement.ogg",channel="sound")
                    achievementList[3] = True
            jump law


label law:
    
    scene black

    $ yuiStoryProgress += 1

    if law == 'paper':

        show image "images/paper1.png" with dissolve
        pause 5.0
        hide image "images/paper1.png" with dissolve
        play sound "audio/sfx/newspaper.wav" 
        show image "images/ssacover.jpg" with dissolve
        pause 8.0
        play sound "audio/sfx/newspaper.wav"
        hide image "images/ssacover.jpg"
        show image "images/cnnssa.jpg" with dissolve
        pause 12.0
        play sound "audio/sfx/newspaper.wav"
    
    else:
        show image "images/tv.jpg" with pixellate
        pause 3.0
        hide image "images/tv.jpg" with dissolve
        show image "images/ssacover.jpg" with dissolve
        pause 10.0
        show image "images/cnnssa.jpg" with dissolve
        pause 12.0
        hide image "images/cnnssa.jpg"
        show image "images/duterte.jpg" with dissolve
        pause 5.0 
        hide image "images/duterte.jpg" 
         
    
    # Show punishments

    show image "images/punishment1.jpg" with dissolve
    pause 30.0
    show image "images/punishment2.jpg" with dissolve
    pause 20.0




    # centered "\“On the 17th of April Year 2019, a new law called {color=#f00}{b}Republic Act No. 11313{/b}{/color} 
    # or also known as {color=#f00}{b}Safe Spaces Act{/b}{/color} has been approved by the President.\""

    # centered "The Safe Spaces Act is an act defining gender-based sexual harassment 
    # in streets, public spaces, online, workplaces, and educational or training institutions."  

    # centered "This law stated that both men and women must have equality, 
    # security and safety not only in private, but also on the streets, public spaces, online, workplaces 
    # and educational and training institutions."

    scene kitchen with fade

    play sound "audio/voice/case1/blnk/line19.ogg"
    "This is a really great law. I should probably take some notes of this law..."

    show screen newNote with fade

    pause 1.5

    show natasha talk with dissolve

    n "Hey its me again~"

    show screen showNotesButton with dissolve

    n "If you look at the top right part of the screen, there is a button."

    n "This button will log important parts of the law. So always check it out~"

    n "Bye now!"

    stop music fadeout 0.5

    $ renpy.end_replay()
    

label goingToSchool:

    scene outside with fade

    $ play_music(poppy)

    play sound "audio/voice/case1/blnk/line20.ogg"
    "Well, that was a great law. Hopefully I can teach someone about it."
    play sound "audio/voice/case1/blnk/line21.ogg"
    "Hmmm. As expected, there will be a class introduction soon. How should I introduce myself?"
    play sound "audio/voice/case1/blnk/line22.ogg"
    "Ehem....."
    play sound "audio/voice/case1/blnk/line23.ogg"
    "\"How y'all doin' everyone! The greatest future attorney is in this class. The name's Mark!\""
    play sound "audio/voice/case1/blnk/line24.ogg"
    "How's that? Hmmm..."
    play sound "audio/voice/case1/blnk/line25.ogg"
    "No... that's... way too embarassing."
    play sound "audio/voice/case1/blnk/line26.ogg"
    "How about..."
    play sound "audio/voice/case1/blnk/line27.ogg"
    "\"Pleased to meet you everyone. Please call me Mark.\""

    "...."
    play sound "audio/voice/case1/blnk/line28.ogg"
    "Yeah that'll work. Short and simple."
    play sound "audio/voice/case1/blnk/line29.ogg"
    "They don't need to know that I am dreaming to be an attorney someday."

    "{i}8:15 AM...{/i}"

    $ play_sound(carleave,fadein=1.5)
    play sound "audio/voice/case1/blnk/line30.ogg"
    "Oh!!! I didn't notice the time at all."
    play sound "audio/voice/case1/blnk/line31.ogg"
    "Should I take a jeep or train today?"
    $ timeout = 8
    $ timeout_label = "meetWithKurt"
    show screen displayHBBPoints 
    menu:
        # Story will diverge from this point. Will converge at some point.
        "Should I take a jeep or train today?"
        
        # Meet Yui
        "Take the train.":

            
            $ metYui = True
            $ renpy.end_replay()
            jump meetWithYui

        # Meet Kurt(friend)
        "Ride a jeep.":

            $ renpy.end_replay()
            jump meetWithKurt

    


label meetWithKurt:
    stop music
    pause 0.5
    play sound "audio/music/Piano2.ogg"fadein 0.3
    scene school gate 
    show screen jeepTransition 
    with fade
    pause 3.0
    hide screen jeepTransition with dissolve
    $ play_music(relax, fadein=8)
    $ metYui = False
    scene bg jeep n with fade
    $ persistent.unlockJeep = True
    python:

        if achievementList[5] == False:
                
            achievement.grant("Bayad Po")
            renpy.notify("Achievement Unlocked: Bayad Po")
            renpy.play("audio/sfx/achievement.ogg",channel="sound")
            achievementList[5] = True

    pause 0.5
    $ renpy.music.set_volume(0.5,channel="sound")
    $ play_sound(people,fadein=0.2,fadeout=5.0) 
    pause 5
    
    "Mark!"

    "Mark!!!"

    "Dude!!"

    $ play_sound(carleave,fadein=0.5)

    play sound "audio/voice/case1/blnk/line32.ogg"
    "Uhmm someone is calling me?"
    play sound "audio/voice/case1/blnk/line33.ogg"
    "From where?"

    "???" "Dude! Are you deaf?"

    $ play_sound(punch,fadein=0.5)
    "Bam!!" with vpunch
    play sound "audio/voice/case1/blnk/line34.ogg"
    "Ouch that hurts..."
    play sound "audio/voice/case1/me/m11.ogg"
    m "Oh.. it is you [kk]!"

    show kurtney happy teeth with dissolve
    play sound "audio/voice/case1/me/m12.ogg"
    m "Why'd you hit me in the back of my head?"

    show kurtney angry talk with dissolve

    kk "Dude you almost rode the jeep without me."
    play sound "audio/voice/case1/me/m13.ogg"
    m "Sorry I didn't notice you at all."

    show kurtney smile with dissolve

    kk "Well its fine. Atleast I'm going to school with you."
    play sound "audio/voice/case1/blnk/line35.ogg"
    "This is [kk]. My weird childhood friend."
    play sound "audio/voice/case1/blnk/line36.ogg"
    "We have been friends since elementary school. She is a little boyish and sometimes annoying."
    play sound "audio/voice/case1/blnk/line37.ogg"
    "But I don't hate it at all."

    show kurtney talk opened with dissolve

    kk "Did you know? Something crazy happened to me today. Good thing I found you."
    play sound "audio/voice/case1/me/m14.ogg"
    m "What happened?"

    kk "There was this guy... standing at the corner of our street."

    kk "He looked unfamiliar to me so I asked him if he was looking for someone or he got lost."
    play sound "audio/voice/case1/me/m15.ogg"
    m "So? Was he lost or what?"

    show kurtney angry talk with dissolve

    kk "Crazy freaking dude told me, \"You look beautiful today as well.\""
    play sound "audio/voice/case1/me/m16.ogg"
    m "That's sexual harassment..."
    play sound "audio/voice/case1/me/m17.ogg"
    m "What does he look like?"

    kk "He wears a hoodie and a sweat pants."
    play sound "audio/voice/case1/me/m18.ogg"
    m "Let me know when you see this guy again."

    show kurtney happy teeth with dissolve

    kk "Thanks dude! I'm lucky I have someone like you."

    kk "Ohhhh and speaking of you..."

    kk "Dude we're already 2nd year in highschool. When are you getting a girlfriend?"
    play sound "audio/voice/case1/me/m19.ogg"
    m "Why are you even asking me that. Even if I wanted to have one, no one likes me at all!"

    show kurtney happy teeth with dissolve

    kk "You poor little thing. Don't worry, I'll always be here for you so you don't look like a loser."
    play sound "audio/voice/case1/me/m20.ogg"
    m "Well, don't even talk like you have one."

    kk "Hahaha~ Don't worry about me. I'm more worried about your future."
    play sound "audio/voice/case1/me/m21.ogg"
    m "I'm not a child for you to worry about."

    kk "Haha!!"
    play sound "audio/voice/case1/me/m22.ogg"
    m "Hey, do you wanna hear something interesting?"
    play sound "audio/voice/case1/me/m23.ogg"
    m "It is related to what happened to you earlier."

    show kurtney talk opened with dissolve

    kk "What? If it's boring then I'm not listening to you."

    #show kurt without headphone
    play sound "audio/voice/case1/me/m24.ogg"
    m "I saw the news this morning. There was a new law.."

    kk "What kind of law?"

    hide kurtney talk opened with dissolve

    $ firstTryWrong = False
    $ timeout = 15
    $ timeout_label = "kurtFirstQuestionTimerOut"

    menu kurtFirstQuestion:
        "Aaaaah... What is it again? The law that was approved on 17th of April, 2019?"

        "Re-semiprivate Act No. 11313":
            "Wrong answer!"
            $ firstTryWrong = True
            jump kurtFirstQuestion

        "Reprivate Act No. 11313":
            "Think again..."
            $ firstTryWrong = True
            jump kurtFirstQuestion

        "Republic Act No. 11313":
            "Correct!!"
            if firstTryWrong is False:

                $ hbbpoints += 3
                $ play_sound(addPoints)
                "You received {color=#40ff00}3 HBB Points.{/color}"
            jump kurtIntroSecond

        "Rebuild Act No. 11313":
            "Not the right answer."
            $ firstTryWrong = True
            jump kurtFirstQuestion

    label kurtFirstQuestionTimerOut:
        $ firstTryWrong = True
        play sound "audio/voice/case1/me/m25.ogg"
        m "Republic Act No. 11313"

    #######################################

    label kurtIntroSecond:
        show kurtney happy teeth with dissolve
        kk "That's cool. Tell me more about it."

        play sound "audio/voice/case1/me/m26.ogg"
        m "Yeah its a great law."

        play sound "audio/voice/case1/me/m27.ogg"
        m "It is also known as ...."

        hide kurtney happy teeth with dissolve

        $ firstTryWrong = False
        $ timeout = 15
        $ timeout_label = "kurtSecondQuestionTimerOut"

    menu kurtSecondQuestion:
        "It is also known as ...."
        
        "Safe Spaces Act":
            "Great answer!"
            if firstTryWrong is False:
                $ hbbpoints += 3
                $ play_sound(addPoints)
                "You received {color=#40ff00}3 HBB Points.{/color}"
            jump kurtIntroThird
            
        "Safe Pace Act":
            "Wait this is wrong."
            $ firstTryWrong = True
            $ subtractPoints()
            "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"
            jump kurtSecondQuestion
        
        "Safe Guardian Act":
            "Not the right answer."
            $ firstTryWrong = True
            $ subtractPoints()
            "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"
            jump kurtSecondQuestion
       
        "Safe Insurrance Act":
            "Not the greatest answer."
            $ firstTryWrong = True
            $ subtractPoints()
            "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"      
            jump kurtSecondQuestion

    label kurtSecondQuestionTimerOut:
        $ firstTryWrong = True
        $ subtractPoints()
        "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"
        #play sound "audio/voice/case1/me/m.ogg"
        m "Safe Spaces Act"

    label kurtIntroThird:

        show kurtney talk opened with dissolve
        kk "So it is called \"Safe Spaces Act\"?"

        play sound "audio/voice/case1/me/m28.ogg"
        m "Yeah! It's a cool name right."

        #show kurt open mouth
        kk "Sure. But what does it mean?"

        $ firstTryWrong = False
        $ timeout = 10
        $ timeout_label = "kurtInfo"

        hide kurtney talk opened with dissolve 

    menu kurtThirdQuestion:
        "Wait, what does the Safe Spaces Act mean again?"

        "To protect Earth from aliens.":
            $ subtractPoints()
            "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"        

            play sound "audio/voice/case1/me/m29.ogg"
            m "To protect Earth from aliens."

            show kurtney angry talk with dissolve

            kk "Dude are you serious?"

            kk "Stop spouting nonsense."
            
            play sound "audio/voice/case1/me/m30.ogg"
            m "Hahaha~ I'm just kidding!"

            play sound "audio/voice/case1/me/m31.ogg"
            m "The law was created to..."
            

            jump kurtInfo

        #See Space Spaces Act Implementing rules Section 5.  https://pcw.gov.ph/assets/files/2020/03/IRR-of-the-Safe-Spaces-Act.pdf?x98095
        # Implement some kind of notes system
        "To protect men and women from gender-based sexual harassment.":
            "Nice job! Correct answer."
            $ hbbpoints += 3
            $ play_sound(addPoints)
            "You received {color=#40ff00}3 HBB Points.{/color}"

            pause 0.5 

            if hbbpoints == 9:
                python:

                    if achievementList[6] == False:
                    
                        achievement.grant("Ace Attorney")
                        renpy.notify("Achievement Unlocked: Ace Attorney")
                        renpy.play("audio/sfx/achievement.ogg",channel="sound")
                        achievementList[6] = True
            
            label kurtInfo:
                $ yuiStoryProgress += 1

                hide kurtney angry talk with dissolve

                #play sound "audio/voice/case1/me/m.ogg"
                m "To protect men and women from gender-based sexual harassment."

                play sound "audio/voice/case1/me/m32.ogg"
                m "Gender-based streets and public spaces sexual harassment include..."

                play sound "audio/voice/case1/me/m33.ogg"
                m "a) Catcalling, wolf-whistling, unwanted invitations, misogynistic, transphobic, homophobic, and sexist slurs."

                play sound "audio/voice/case1/me/m34.ogg"
                m "b) Persistent uninvited comments or gestures on a person's appearance."

                play sound "audio/voice/case1/me/m35.ogg"
                m "c) Relentless requests for personal details."

                play sound "audio/voice/case1/me/m36.ogg"
                m "d) Statement of sexual comments and suggestions."

                play sound "audio/voice/case1/me/m37.ogg"
                m "e) Public masturbation or flashing of private parts, groping, making offensive body gestures 
                at someone, and other similar lewd sexual actions."

                play sound "audio/voice/case1/me/m38.ogg"
                m "f) Any advances, whether verbal or physical, that is unwanted and has threatened one's sense of personal space and physical safety. 
                This may include cursing, leering and intrusive gazing, and taunting."

                play sound "audio/voice/case1/me/m39.ogg"
                m "g) Persistent telling of sexual jokes, use of sexual names."

                play sound "audio/voice/case1/me/m40.ogg"
                m "And last but not the least."
                
                play sound "audio/voice/case1/me/m41.ogg"
                m "h) Stalking."

                show screen newNote with fade
                pause 1.0

                show kurtney talk opened with dissolve

                kk "That was a lot! How'd you memorize it?"

                play sound "audio/voice/case1/me/m42.ogg"
                m "Well you know... I wanted to be an attorney. So this much is not that big deal."

                show kurtney happy teeth with dissolve

                kk "Attorney Mark? Sounds nice haha~"

                play sound "audio/voice/case1/me/m43.ogg"
                m "Stop mocking me dude."

                show kurtney talk opened with dissolve

                kk "So what happens when I do any of those things?"

                play sound "audio/voice/case1/me/m44.ogg"
                m "Let's continue later dude. We are close to the school."

                show kurtney smile with dissolve

                kk "Tell me about it okay? It's an interesting law."

                

        "To protect public and online spaces from danger.":
            $ subtractPoints()
            "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"

            play sound "audio/voice/case1/me/m45.ogg"
            m "To protect public and online spaces from danger."

            show kurtney angry talk with dissolve

            kk "What danger? Explain it clearly."

            play sound "audio/voice/case1/me/m46.ogg"
            m "Uhhhh.. wait let me remember..."

            play sound "audio/voice/case1/me/m47.ogg"
            m "Errr... it is to..."

            jump kurtInfo

        ########################################
    $ renpy.end_replay()

    label confrontation:

        stop music
        pause 0.5
        play sound "audio/music/Piano5.ogg"fadein 0.3
        scene walk
        show screen stalkerTransition 
        with fade
        pause 3.0
        hide screen stalkerTransition with dissolve
        $ play_music(Lurking, fadein=8)
        $ persistent.unlockWalk = True

        $ play_sound(walking,fadein=0.3,fadeout=5.0)
        scene black with fade

        "A peaceful morning for a first day of school."

        "Or so I thought..."
        scene walk with fade

        show kurtney happy teeth with dissolve

        kk "Hahaha~ I miss summer vacation."

        play sound "audio/voice/case1/me/m48.ogg"
        m "Oh shut up. All you do is play games and watch anime."

        kk "Are you talking about yourself? Ahahaha~"

        play sound "audio/voice/case1/me/m49.ogg"
        m "Whatever."

        scene walk with fade

        "While peacefully chatting ang walking to school, [kk] saw something she doesn't want to see."

        show kurtney talk opened with dissolve

        kk "Hey, Mark..."

        play sound "audio/voice/case1/me/m50.ogg"
        m "Hmmm?"

        kk "Look behind our back..."

        play sound "audio/voice/case1/me/m51.ogg"
        m "Back?"

        hide kurtney talk opened

        show stalker neutral with fade

        pause 3.0

        hide stalker neutral with fade

        play sound "audio/voice/case1/me/m52.ogg"
        m "What the hell? Is that the stalker guy from what you've said earlier?"

        show kurtney smile with dissolve

        kk "Watch your mouth. He might hear you and do something bad."

        play sound "audio/voice/case1/me/m53.ogg"
        m "And now you're concerned for me?"

        play sound "audio/voice/case1/me/m54.ogg"
        m "I should be the one worrying for you."

        show kurtney blush close with dissolve

        kk "Of course, you're my precious childhood friend."

        play sound "audio/voice/case1/me/m55.ogg"
        m "Hahaha~ whatever. I got this."

        scene walk with fade

        menu:
            "What should I do?"

            "Run straight to the school gate.":
                pause 0.5
                $ subtractPoints()
                "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"
                play sound "audio/voice/case1/me/m56.ogg"
                m "[kk]..."

                pause 0.5

                python:

                    if achievementList[7] == False:
                    
                        achievement.grant("Escape Artist")
                        renpy.notify("Achievement Unlocked: Escape Artist")
                        renpy.play("audio/sfx/achievement.ogg",channel="sound")
                        achievementList[7] = True

                show kurtney talk opened with dissolve

                kk "Yeah?"

                play sound "audio/voice/case1/me/m57.ogg"
                m "Hold my hand."

                show kurtney blush small with dissolve

                kk "Wha? Are you st-stupid?"

                play sound "audio/voice/case1/me/m58.ogg"
                m "Do it!"

                show kurtney blush close with dissolve

                kk "O-o-okayyy...."

                scene black with fade

                $ play_sound(running)

                "With all my might and strength reserved for this day, I grabbed [kk]'s hand and ran like a mad dog."

                "What a crazy person!"

                scene school gate with fade

                "Looking at my back, the guy is nowhere to be seen."

                play sound "audio/voice/case1/me/m59.ogg"
                m "Pant pant pant..."

                show kurtney blush close with dissolve

                kk "Hey tell me what're you trying to do before doing that..."

                kk "Stupid..."

                play sound "audio/voice/case1/me/m60.ogg"
                m "Hahaha~ I just want to get away though. Why did you suddenly become red?"


                
            "Pick a fight with the stalker.":
                pause 0.5
                $ subtractPoints()
                "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"

                play sound "audio/voice/case1/me/m61.ogg"
                m "Hey, what do you want?"

                show stalker talk with fade

                "???" "Hmmm.. Are you her boyfriend?"

                play sound "audio/voice/case1/me/m62.ogg"
                m "No! She's my friend."

                "???" "Then take this."

                $ play_sound(punch)

                "BAM!" with vpunch

                $ play_sound(punch)

                "AAHHH!" with hpunch

                $ play_sound(punch)

                "PAAAK!" with vpunch

                play sound "audio/voice/case1/me/m63.ogg"
                m "AAAAAAH!!!"

                scene black with fade
                pause 1.0
                scene walk with fade

                pause 0.5

                python:

                    if achievementList[8] == False:
                    
                        achievement.grant("Punching Bag")
                        renpy.notify("Achievement Unlocked: Punching Bag")
                        renpy.play("audio/sfx/achievement.ogg",channel="sound")
                        achievementList[8] = True

                show kurtney worry with dissolve

                kk "Heyyyyyyy..."

                kk "Wake up Mark..."

                play sound "audio/voice/case1/me/m64.ogg"
                m "What the heck happened?"

                show kurtney happy teeth with dissolve

                kk "Well, he knocked the soul out of you. Hahaha~"

                play sound "audio/voice/case1/me/m65.ogg"
                m "This is no laughing matter. What happened to him?"

                show kurtney smile with dissolve

                kk "He ran away when a lot of people were looking at us."

                play sound "audio/voice/case1/me/m67.ogg"
                m "O-ohhh I see... Ughhhh my head hurts."

                

            "Confront the stalker and tell him that you'll report him to the police.":
                    pause 0.5
                    $ hbbpoints += 3
                    $ play_sound(addPoints)
                    "You received {color=#40ff00}3 HBB Points.{/color}"

                    scene walk with fade

                    play sound "audio/voice/case1/me/m68.ogg"
                    m "Excuse me. Stop whatever you're doing. You're disrupting our lives."

                    show stalker talk with dissolve

                    "???" "Who the hell are you?"

                    "???" "What's your deal, huh?"

                    "???" "Stupid kid standing up to me huh."

                    play sound "audio/voice/case1/me/m69.ogg"
                    m "I am her friend. I will not hesitate to report you to the police this instant!"

                    hide stalker talk
                    show stalker angry 
                    with dissolve

                    "???" "Calm down buddy. No reason to be angry. I'll leave now. Enjoy your day."

                    "???" "I won't forget this! Be careful from now on."

                    hide stalker angry 

                    scene walk 
                    
                    with fade

                    "After a few minutes, the stalker was out of sight."

                    stop music

                    play sound "audio/voice/case1/me/m70.ogg"
                    m "Sighhhh. Hopefully this doesn't happen to you again."

                    show kurtney worry with dissolve

                    $ play_music(evans,fadein=1.5)

                    kk "I hope so. You'll be there to protect me right?"

                    play sound "audio/voice/case1/me/m71.ogg"
                    m "Nope. Not me. But the police. Haha~"

                    show kurtney angry talk with dissolve

                    kk "Wha?! Stupid."

                    hide kurtney angry talk with dissolve

        
    label kurtneyOfficerScene:
        stop music fadeout 2.0
        scene black with fade

        pause 1.0 

        scene walk with fade

        show officer with dissolve 

        $play_music(garden) 

        "???" "Excuse me!"

        kk "Ehhh? A police officer?"

        play sound "audio/voice/case1/me/m72.ogg"
        m "Oh great. This makes things easy."

        "The police officer was running towards us with a confused look on his face."

        o "Excuse me young ones... I just saw what happened earlier. Can you tell me more about the event?"

        play sound "audio/voice/case1/me/m73.ogg"
        m "Uhmmmm my friend here was getting stalked by someone..."

        o "A stalker huh?"

        o "Did you know that stalking is a grave crime? According to the Safe Spaces Act that is."

        play sound "audio/voice/case1/me/m74.ogg"
        m "Yes sir, I've read a bit about that law."

        hide officer
        show kurtney talk opened 
        with dissolve

        kk "Hey Mark. It was that law that you told me earlier right?"

        play sound "audio/voice/case1/me/m75.ogg"
        m "Yeah it is."

        hide kurtney talk opened
        show officer
        with dissolve

        o "Stalking is a serious crime. Do you guys want to learn about the punishment for violating the Safe Spaces Act?"

        $ yuiStoryProgress += 1

        hide officer with dissolve

        menu :
            
            o "Do you want to learn more about the punishments of Safe Spaces Act?"

            "Yes, please tell me about the punishments.":
                hide officer with dissolve
                pause 0.5
                $ play_sound(addPoints)
                $ hbbpoints += 3
                "You received {color=#40ff00}3 HBB Points.{/color}"
                
                show kurtney happy teeth with dissolve

                python:

                    if achievementList[9] == False:
                    
                        achievement.grant("Teach Me About Punishments")
                        renpy.notify("Achievement Unlocked: Teach Me About Punishments")
                        renpy.play("audio/sfx/achievement.ogg",channel="sound")
                        achievementList[9] = True

                kk "!!!!"

                kk "I-I-I want to learn it too..."

                hide kurtney happy teeth
                show officer
                with dissolve
                o "Sure thing. Lemme just take out my handbook."

                pause 2.0

                o "Uhhh it says here..."

                o "On Section 12 of the Safe Spaces Act, 
                it states the Specific Acts and Penalties for Gender-Based Sexual Harassment in Streets and Public Spaces."

                o "This is quite long so listen carefully okay?"

                with fade

                
                o "a) For acts such as cursing, wolf-whistling, catcalling, leering and intrusive gazing. taunting, cursing, unwanted invitations, misogynistic, transphobic, homophobic, and sexist slurs;" 
                
                o"Persistent unwanted comments on one's appearance, relentless requests for one's personal details such as name, contact and social media details or destination;" 
                
                o "The use of words, gestures or actions that ridicule on the basis of sex, gender or sexual orientation, identity and/or expression including sexist, homophobic, and transphobic statements and slurs;" 
                
                o "The persistent telling of sexual jokes, use of sexual names, comments and demands, and any statement that has made an invasion on a person's personal space or threatens the person's sense of personal safety." 

                o "The penalties will be...!"
                
                o "{color=#30ff45}First Offence{/color}: Fine of One thousand pesos (P 1,000.00) and community service of twelve (12) hours inclusive of attendance to a Gender Sensitivity Seminar conducted by PNP."

                o "{color=#30ff45}Second Offence{/color}: Arresto menor (6 to 10 days) or a fine of Three thousand pesos (P3,000.00)"

                o "{color=#30ff45}Third Offence{/color}: Arresto menor (11 to 30 days) and a fine of Ten thousand pesos (P10, 000.00)"

                o "The next on the list!"

                with fade

                o "b) For acts such as making offensive body gestures at someone, and exposing private parts for the sexual gratification of the perpetrator with the effect of demeaning, harassing, threatening;"
                
                o "Or intimidating the offended party including flashing of private parts, public masturbation, groping, and similar lewd sexual actions."

                o "The penalties you will face is...!"
                
                o "{color=#30ff45}First Offence{/color}: Fine of Ten thousand pesos (P 10,000.00) and community service of twelve (12) hours inclusive of attendance to a Gender Sensitivity Seminar conducted by PNP."

                o "{color=#30ff45}Second Offence{/color}: Arresto menor (11 to 30 days) or a fine of Fifteen thousand pesos (P15,000.00)"

                o "{color=#30ff45}Third Offence{/color}: Arresto mayor (1 month and 1 day to 6 months) and a fine of Twenty thousand pesos (P20, 000.00)"

                o "Moving on!"

                with fade

                o "c) For acts such as stalking, and any of the acts mentioned in paragraphs (a) and (b), when accompanied by touching, pinching or brushing against the body of the offended person;"

                o "Or any touching, pinching, or brushing against the genitalia, face, arms, anus, groin, breasts, inner thighs, face, buttocks or any part of the victim's body even when not accompanied by acts mentioned in paragraphs (a) and (b)."

                o "You will face the penalties of...!"

                o "{color=#30ff45}First Offence{/color}: Arresto menor (11 to 30 days) or a fine of Thirty thousand pesos (P 30,000.00) and completion of community service conducted by PNP."

                o "{color=#30ff45}Second Offence{/color}: Arresto mayor (1 month and 1 day to 6 months) or a fine of Fifty thousand pesos (P 50,000.00)"
                
                o "{color=#30ff45}Third Offence{/color}: Arresto mayor in its maximum period or a fine of One hundred thousand pesos (P100,000.00)"

                hide officer with fade

                m "......"

                play sound "audio/voice/case1/me/m76.ogg"
                m "My head hurts... Ahahaha!"

                show kurtney talk opened with dissolve

                kk "Wait, that's a really good law, Officer!"
                
                hide kurtney talk closed

            "No, I don't really care.":
                pause 0.5
                $ subtractPoints()
                "Your points have been deducted by 1 HBB Point."
                
        $ renpy.end_replay()
        show screen newNote with fade
        pause 2.0
        stop music
        jump schoolCeremony


label meetWithYui:
    stop music
    pause 1.5
    play sound "audio/music/Transition1.ogg" fadein 1.0
    scene bg train 
    show screen trainTransition 
    with fade
    pause 3.0
    hide screen trainTransition
    $ persistent.unlockTrain = True
    $ persistent.unlockTrain2 = True
    scene train landscape with fade

    python:

        if achievementList[4] == False:
                
            achievement.grant("Beep Card")
            renpy.notify("Achievement Unlocked: Beep Card")
            renpy.play("audio/sfx/achievement.ogg",channel="sound")
            achievementList[4] = True

    pause 0.5

    $play_sound(trainambience,fadein=0.1)

    pause 5.0

    "Aaaaaaah~ The landscape is so nice."

    "I wish every morning was something like this..."

    "But that's a pointless wish."
    
    scene trainpeople with fade
    pause 2.0
    
    "Eh, it is surprisingly quiet today..."

    "Even though its the first day of class?"

    "Well, I shouldn't be complaining about this."

    stop sound fadeout 5.0
    
    $ play_music(evans,fadein=1.0)

    "I kinda like this atmosphere."

    "Hopefully, this day goes successful."

    "...."

    $ play_sound(operator, fadein=3.0,fadeout=0.5)

    scene bg train with fade

    pause 2.0

    "Operator" "Arriving at station. Please check your belongings before getting out. Thank you."

    pause 3.0

    scene bg train test with fade

    $ play_sound(people,fadein=3.0,fadeout=1.0)

    "{i}Crowd noises...{/i}"

    "Moving closer towards the exit... I hear some conversation."

    "???" "Hey there sexy little miss. Are you free tonight and have a drink." 

    "???" "Don't worry, we won't do anything do bad to you hehehe..."

    "???" "Do you need money or anything? Just tell us."

    "I can see three old men sexually harassing a young student girl."

    "I notice that the girl is trembling and shaking."

    show yui worry with dissolve

    "Girl" "Plea-please l-l-leave me alo-lone..."

    pause 2.0

    hide yui worry with dissolve 

    "???" "Hahaha!! She's scared like a child."

    "???" "Hey, you're teasing her too much. She might report us."

    "???" "Boss, don't worry. She can't even say the sentence straight."

    show yui worry closed with dissolve
    pause 3

    hide yui worry closed with dissolve 
    $ timeout = 10
    $ timeout_label = "notSaveYui"
    $ deathFlag = False
    $ metYui = True
    menu trainScene:
        "What should I do?"


        "I'll pick a fight with them." if deathFlag is False:
            pause 0.5

            $ deathFlag = True

            play sound "audio/voice/case1/me/m77.ogg"
            m "Hey you bastards! Stop sexually harrassing that girl."

            "???" "Who the hell are you? His boyfriend perhaps?"

            "???" "You little punk talking to me like that. I'll crush you."

            "???" "Take this you pesky little boy."

            $ play_sound(punch)

            "BAM!" with vpunch

            $ play_sound(punch)

            "AAHHH!" with hpunch

            $ play_sound(punch)

            "PAAAK!" with vpunch

            with fade

            play sound "audio/voice/case1/me/m78.ogg"
            m "AAAAAAH!!!"

            pause 0.5

            python:

                if achievementList[8] == False:
                    
                    achievement.grant("Punching Bag")
                    renpy.notify("Achievement Unlocked: Punching Bag")
                    renpy.play("audio/sfx/achievement.ogg",channel="sound")
                    achievementList[8] = True

            "....Officer!"

            jump withOfficer

        "I'll go and inform the train security.":
            "Good choice!"
            $ play_sound(addPoints)
            $ hbbpoints += 3
            "You received {color=#40ff00}3 HBB Points.{/color}"
            hide yui worry closed
            play sound "audio/voice/case1/me/m79.ogg"
            m "Officer! Officer!!"

            play sound "audio/voice/case1/me/m80.ogg"
            m "I saw three old men catcalling and sexually harassing a girl student! Please help me."

            show officer with dissolve

            o "I see. Bring me to them."

            label withOfficer:

                hide officer with dissolve

                with fade

                play sound "audio/voice/case1/me/m81.ogg"
                m "Officer! Here!"

                play sound "audio/voice/case1/me/m80.ogg"
                m "These old men are catcalling and making unwanted invitations to this girl."

                show officer with dissolve

                o "HEY YOU BASTARDS!"

                o "Face the consequences of your crimes!"

                with hpunch

                "???" "What the hell. Run guys!!"

                "???" "Holy crap don't leave me."

                "???" "Dammnit!"

                with vpunch

            #show Yui

            hide officer
            scene bg train morning
            show yui wow 
            with fade
            "Girl" "Uwaaaaah! Thank y-y-you sooo much!!"

            play sound "audio/voice/case1/me/m82.ogg"
            m "Ohhh... I didn't really do anything..."

            show yui smile close with dissolve

            "Girl" "You saved my life...."

            play sound "audio/voice/case1/me/m83.ogg"
            m "Life?"

            show yui smile opened with dissolve

            "Girl" "Uhmm..."

            "Girl" "Can you tell me your name?"

            play sound "audio/voice/case1/me/m84.ogg"
            m "Ohhh. My name is Mark. How about you?"

            show yui blush with dissolve

            "Girl" "Y-Y-Yu.."

            play sound "audio/voice/case1/me/m85.ogg"
            m "Yu?"

            show yui surprised blush with dissolve

            "She's gotten a bit red of a sudden..."

            show yui blush closed with dissolve

            "Girl" "Ple-please call me Yui."

            play sound "audio/voice/case1/me/m86.ogg"
            m "[y], huh? What a cute name."

            show yui surprised blush with dissolve

            y "EHHH?!! Cute?"

            show yui blush closed with dissolve

            y "{i}......waaah!{/i}"

            play sound "audio/voice/case1/me/m87.ogg"
            m "Hey, [y]. I saw you earlier that you were shaking and trembling."

            show yui worry with dissolve

            y "Yeah that was embarassing to see...."

            show yui worry closed with dissolve

            y "You see, when I was a child... I had a trauma."

            play sound "audio/voice/case1/me/m88.ogg"
            m "A trauma? Can I hear more of this?"

            y "Uhmmm y-yes..."

            show yui worry opened with dissolve

            y "When I was in 4th Grade, my boy classmates would make fun of my appearance."

            y "It made me stop going to school... And I was homeschooled since then."

            play sound "audio/voice/case1/me/m89and90.ogg"
            m "I can't imagine how you must feel. My heart hurts for you."

            show yui worry closed with dissolve

            play sound "audio/voice/case1/me/m89.ogg"
            m "You know what? I have something interesting to tell you!"

            show yui wow with dissolve

            y "What is it?"

            play sound "audio/voice/case1/me/m90.ogg"
            m "It's about a law."

            y "A law? What kind of law?"

            play sound "audio/voice/case1/me/m91.ogg"
            m "It is something related to what you experienced earlier."
            $ timeout = 15
            $ timeout_label = "yuiFirstQuestionTimerOut"
            $ yuiFirstAnswer = True
            hide yui wow with dissolve
            menu yuiFirstQuestion:
                "Aaaaah... What is it again? The law that was approved on 17th of April, 2019?"

                "Re-semiprivate Act No. 11313":
                    m "Re-semiprivate Act No. 11313"

                    play sound "audio/voice/case1/me/m92.ogg"
                    "Wrong answer!"

                    if hbbpoints >= 1:
                        $ subtractPoints()
                        "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"

                    $ yuiFirstAnswer = False
                    jump yuiFirstQuestion

                "Reprivate Act No. 11313":
                    m "Reprivate Act No. 11313"
                    
                    play sound "audio/voice/case1/me/m93.ogg"
                    "Not this... Think again..."
                    if hbbpoints >= 1:
                        $ subtractPoints()
                        "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"
                    $ yuiFirstAnswer = False
                    jump yuiFirstQuestion

                "Republic Act No. 11313":
                    m "Republic Act No. 11313"
                    
                    play sound "audio/voice/case1/me/m94.ogg"
                    "Great answer!"

                    if yuiFirstAnswer:

                        $ hbbpoints += 3
                        $ play_sound(addPoints)
                        "You received {color=#40ff00}3 HBB Points.{/color}"
                        
                    jump yuiIntroSecond
                    

                "Rebuild Act No. 11313":
                    m "Rebuild Act No. 11313"
                    
                    play sound "audio/voice/case1/me/m95.ogg"
                    "Not the right answer."
                    if hbbpoints >= 1:
                        $ subtractPoints()
                        "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"
                    $ yuiFirstAnswer = False
                    jump yuiFirstQuestion

            #######################################

            label yuiFirstQuestionTimerOut:
                #play sound "audio/voice/case1/me/m.ogg"
                m "Correct Answer: Republic Act No. 11313"

            label yuiIntroSecond:

            play sound "audio/voice/case1/me/m96.ogg"
            m "The law is Republic Act No. 11313."

            show yui wow with dissolve

            y "What is that law?"

            play sound "audio/voice/case1/me/m97.ogg"
            m "This law is..."
            $ timeout_label = "yuiSecondQuestionTimerOut"
            $ yuiSecondAnswer = True
            hide yui wow with dissolve
            menu yuiSecondQuestion:
                "It is also known as ...."
                
                "Safe Spaces Act":
                    m "Safe Spaces Act"
                    
                    play sound "audio/voice/case1/me/m98.ogg"
                    "Correct!!"

                    if yuiSecondAnswer:

                        $ hbbpoints += 3
                        $ play_sound(addPoints)
                        "You received {color=#40ff00}3 HBB Points.{/color}"
                    jump yuiThirdIntro
                    
                "Safe Pace Act":
                    m "Safe Pace Act"
                    
                    play sound "audio/voice/case1/me/m99.ogg"
                    "Wait this is wrong."
                    $ yuiSecondAnswer = False
                    $ subtractPoints()
                    "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"
                    

                    jump yuiSecondQuestion
                
                "Safe Guardian Act":
                    m "Safe Guardian Act"
                    
                    play sound "audio/voice/case1/me/m100.ogg"
                    "Not the right answer."
                    $ yuiSecondAnswer = False
                    $ subtractPoints()
                    "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"
                    
                    jump yuiSecondQuestion
            
                "Safe Insurrance Act":
                    m "Safe Insurance Act"
                    
                    play sound "audio/voice/case1/me/m101.ogg"
                    "Not the greatest answer."
                    $ yuiSecondAnswer = False
                    $ subtractPoints()
                    "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"
                         
                    jump yuiSecondQuestion

            label yuiSecondQuestionTimerOut:
                $ subtractPoints()
                "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"
                
                play sound "audio/voice/case1/me/m98.ogg"
                m "Safe Spaces Act"
            
            label yuiThirdIntro:

                show yui wow with dissolve

                y "So it is called \"Safe Spaces Act\"?"

                play sound "audio/voice/case1/me/m102.ogg"
                m "Yeah! It's a cool name right?"

                #show kurt open mouth
                y "Uhm. But what does it mean?"

                $ yuiThirdAnswer = True
                $ timeout_label = "yuiInfo"

                hide yui wow with dissolve

            menu yuiThirdQuestion:
                "Wait, what does the Safe Spaces Act mean again?"

                "To protect Earth from aliens.":
                    pause 0.5
                    $ subtractPoints()
                    "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"
                    
                    show yui smile close with dissolve

                    y "Wait that's really funny~"

                    y "Please tell it to me seriously..."
                    
                    play sound "audio/voice/case1/me/m30.ogg"
                    m "Hahaha~ I'm just kidding!"

                    play sound "audio/voice/case1/me/m31.ogg"
                    m "The law was created to..."
                    $ yuiThirdAnswer = False
                    jump yuiThirdQuestion

        #See Space Spaces Act Implementing rules Section 5.  https://pcw.gov.ph/assets/files/2020/03/IRR-of-the-Safe-Spaces-Act.pdf?x98095
        # Implement some kind of notes system
                "To protect men and women from gender-based sexual harassment.":
                    "Nice job! Correct answer."
                    if yuiThirdAnswer:
                        $ play_sound(addPoints)
                        $ hbbpoints += 3
                        "You received {color=#40ff00}3 HBB Points.{/color}"

                        if hbbpoints == 9:
                        
                            python:

                                if achievementList[6] == False:
                                
                                    achievement.grant("Ace Attorney")
                                    renpy.notify("Achievement Unlocked: Ace Attorney")
                                    renpy.play("audio/sfx/achievement.ogg",channel="sound")
                                    achievementList[6] = True
                        
                    
                    show yui neutral with dissolve
                    label yuiInfo:
                        $ yuiStoryProgress += 1
                        

                        #play sound "audio/voice/case1/me/m.ogg"
                        m "To protect men and women from gender-based sexual harassment."

                        play sound "audio/voice/case1/me/m32.ogg"
                        m "Gender-based streets and public spaces sexual harassment include..."

                        play sound "audio/voice/case1/me/m33.ogg"
                        m "a) Catcalling, wolf-whistling, unwanted invitations, misogynistic, transphobic, homophobic, and sexist slurs."

                        play sound "audio/voice/case1/me/m34.ogg"
                        m "b) Persistent uninvited comments or gestures on a person's appearance."

                        play sound "audio/voice/case1/me/m35.ogg"
                        m "c) Relentless requests for personal details."

                        play sound "audio/voice/case1/me/m36.ogg"
                        m "d) Statement of sexual comments and suggestions."

                        play sound "audio/voice/case1/me/m37.ogg"
                        m "e) Public masturbation or flashing of private parts, groping, making offensive body gestures 
                        at someone, and other similar lewd sexual actions."

                        play sound "audio/voice/case1/me/m38.ogg"
                        m "f) Any advances, whether verbal or physical, that is unwanted and has threatened one's sense of personal space and physical safety. 
                        This may include cursing, leering and intrusive gazing, and taunting."

                        play sound "audio/voice/case1/me/m39.ogg"
                        m "g) Persistent telling of sexual jokes, use of sexual names."

                        play sound "audio/voice/case1/me/m40.ogg"
                        m "And last but not the least."

                        play sound "audio/voice/case1/me/m41.ogg"
                        m "h) Stalking."

                        show screen newNote with fade
                        pause 1.0

                        show yui wow with dissolve

                        y "That was a lot! How'd you memorize it?"

                        play sound "audio/voice/case1/me/m42.ogg"
                        m "Well you know... I wanted to be an attorney. So this much is not that big deal."

                        show yui smile opened with dissolve

                        y "You wanted to be an attorney? That sounds really nice~"

                        play sound "audio/voice/case1/me/m103.ogg"
                        m "Thank you ehehe..."

                        jump yuiConflictResolved


                "To protect public and online spaces from danger.":
                    pause 0.5
                    $ subtractPoints()
                    "Your points are deducted by {color=#c0ff73}1 HBB Point!{/color}"
                    
                    y "What danger? Please explain it clearly."

                    #play sound "audio/voice/case1/me/m.ogg"
                    m "Uhhhh.. wait let me remember..."

                    #play sound "audio/voice/case1/me/m.ogg"
                    m "Errr... it is to..."

                    $ yuiThirdAnswer = False

                    jump yuiThirdQuestion

                    

        "I'll pretend that I didn't hear the conversation.":
            pause 0.5
            $ play_sound(subPoints)
            "Your have lost all your points!"
            $ hbbpoints -= hbbpoints
            jump notSaveYui
            

            
    label notSaveYui:
        $ badEndingGame = True
        "I'll pretend that I didn't hear the conversation."

        "I should just ignore them..."

        "I don't wanna get in trouble."

        jump yui_end

        # IMPLEMENT BAD ENDING!

    
    label yuiConflictResolved:
        hide yui smile opened
        show officer with fade       
        o "Hey kids. You better get going now. I'll clean this mess up."

        o "Based on the Implementing Rules and Regulation of Republic Act No. 11313..."

        o "Those guys broke the law by (1) Catcalling and making unwanted invitations."

        o "(2) Making statements of sexual comments and suggestions."

        o "(3) Making advances, whether verbal or physical, that is unwanted and has threatened one's sense of personal space and physical safety." 

        o "This may include cursing, leering and intrusive gazing, and taunting."

        play sound "audio/voice/case1/me/m104.ogg"
        m "WOW! That's a really great law."

        o "I know kid."

        o "Do you want to learn more about the punishments of Safe Spaces Act?"

        $ yuiStoryProgress += 1

        $ timeout = 10
        $ timeout_label = "ignorePunishment"

        hide officer with dissolve

    menu punishments:
        
        o "Do you want to learn more about the punishments of Safe Spaces Act?"

        "Yes, please tell me about the punishments.":
            hide officer with dissolve
            pause 0.5
            $ hbbpoints += 3
            $ play_sound(addPoints)
            "You received {color=#40ff00}3 HBB Points.{/color}"
            
            show yui smile close with dissolve

            y "!!!!"

            y "I-I-I want to learn it too..."

            python:

                if achievementList[9] == False:
                    
                    achievement.grant("Teach Me About Punishments")
                    renpy.notify("Achievement Unlocked: Teach Me About Punishments")
                    renpy.play("audio/sfx/achievement.ogg",channel="sound")
                    achievementList[9] = True

            hide yui smile close
            show officer
            with dissolve
            o "Sure thing. Lemme just take out my handbook."

            pause 2.0

            o "Uhhh it says here..."

            o "On Section 12 of the Safe Spaces Act, 
            it states the {color=#30ff45}Specific Acts and Penalties{/color} for Gender-Based Sexual Harassment in Streets and Public Spaces."

            o "This is quite long so listen carefully okay?"

            with fade

            o "a) For acts such as cursing, wolf-whistling, catcalling, leering and intrusive gazing. taunting, cursing, unwanted invitations, misogynistic, transphobic, homophobic, and sexist slurs;" 
            
            o"Persistent unwanted comments on one's appearance, relentless requests for one's personal details such as name, contact and social media details or destination;" 
            
            o "The use of words, gestures or actions that ridicule on the basis of sex, gender or sexual orientation, identity and/or expression including sexist, homophobic, and transphobic statements and slurs;" 
            
            o "The persistent telling of sexual jokes, use of sexual names, comments and demands, and any statement that has made an invasion on a person's personal space or threatens the person's sense of personal safety." 

            o "The penalties will be...!"
            
            o "{color=#30ff45}First Offence{/color}: Fine of One thousand pesos (P 1,000.00) and community service of twelve (12) hours inclusive of attendance to a Gender Sensitivity Seminar conducted by PNP."

            o "{color=#30ff45}Second Offence{/color}: Arresto menor (6 to 10 days) or a fine of Three thousand pesos (P3,000.00)"

            o "{color=#30ff45}Third Offence{/color}: Arresto menor (11 to 30 days) and a fine of Ten thousand pesos (P10, 000.00)"

            o "The next on the list!"

            with fade

            o "b) For acts such as making offensive body gestures at someone, and exposing private parts for the sexual gratification of the perpetrator with the effect of demeaning, harassing, threatening;"
            
            o "Or intimidating the offended party including flashing of private parts, public masturbation, groping, and similar lewd sexual actions."

            o "The penalties you will face is...!"
             
            o "{color=#30ff45}First Offence{/color}: Fine of Ten thousand pesos (P 10,000.00) and community service of twelve (12) hours inclusive of attendance to a Gender Sensitivity Seminar conducted by PNP."

            o "{color=#30ff45}Second Offence{/color}: Arresto menor (11 to 30 days) or a fine of Fifteen thousand pesos (P15,000.00)"

            o "{color=#30ff45}Third Offence{/color}: Arresto mayor (1 month and 1 day to 6 months) and a fine of Twenty thousand pesos (P20, 000.00)"

            o "Moving on!"

            with fade

            o "c) For acts such as stalking, and any of the acts mentioned in paragraphs (a) and (b), when accompanied by touching, pinching or brushing against the body of the offended person;"

            o "Or any touching, pinching, or brushing against the genitalia, face, arms, anus, groin, breasts, inner thighs, face, buttocks or any part of the victim's body even when not accompanied by acts mentioned in paragraphs (a) and (b)."

            o "You will face the penalties of...!"

            o "{color=#30ff45}First Offence{/color}: Arresto menor (11 to 30 days) or a fine of Thirty thousand pesos (P 30,000.00) and completion of community service conducted by PNP."

            o "{color=#30ff45}Second Offence{/color}: Arresto mayor (1 month and 1 day to 6 months) or a fine of Fifty thousand pesos (P 50,000.00)"
            
            o "{color=#30ff45}Third Offence{/color}: Arresto mayor in its maximum period or a fine of One hundred thousand pesos (P100,000.00)"

            hide officer with fade

            m "......"

            #play sound "audio/voice/case1/me/m.ogg"
            m "My head hurts... Ahahaha!"

            show yui wow with dissolve

            y "Wait, that's a really good law, Officer!"

            scene bg train morning with fade

            jump trainEndScene
            

        "No, I don't really care.":
            jump ignorePunishment
    
    label ignorePunishment:

        play sound "audio/voice/case1/me/m105.ogg"
        m "No, I don't really care."

        show officer with dissolve

        o "Ohhhh that's a shame."
        $ subtractPoints()
        $ hbbpoints -= 3
        "Your {color=#30ff45}HBB Points{/color} have been deducted by 3!"
        
    
    label trainEndScene:


        show screen newNote 
        pause 2.0

        show officer

        o "Now go on your way. I'll take care of them. In jail of course."
        
        #play sound "audio/voice/case1/me/m.ogg"
        m "Sir, can I ask for your name?"

        o "Oh it's Greg. Find me whenever you are troubled."

        #play sound "audio/voice/case1/me/m.ogg"
        m "Thank you very much sir!"

        hide officer with fade

        show yui worry opened with dissolve

        y "Uhmmm..."

        y "See you Mark! Thank you again..."

        #play sound "audio/voice/case1/me/m.ogg"
        m "Bye Yui. No worries. I just can't stand it when I see someone getting harassed."

        show yui blush with dissolve

        y "Uhhhm.. I hope I..." 
        
        y "I can see you aga--"

        scene black with fade

        $ play_sound(trainpass,fadein=3.0,fadeout=2.0)

        pause 5.0

        #Train sound

        scene bg train morning with fade
        "{i}A train passed by.{/i}"

        #play sound "audio/voice/case1/me/m.ogg"
        m "What?"

        show yui surprised blush with dissolve

        y "No, you heard nothing!!! Goodbye!"

        scene black with fade

        stop music fadeout 1.0

        $ renpy.end_replay()

        jump schoolCeremony

label schoolCeremony:

    scene aerial 
    show screen schoolTransition
    with fade
    play sound "audio/music/Piano2.ogg"

    pause 5.0
    hide screen schoolTransition
    with fade

    $ play_music(quirky,fadein=0.2)
    "Borneul Highschool. A prestigious school where only the best can enter."

    scene school building with fade

    "I'm so lucky to be here."

    "...."

    scene audi1 with fade

    pause 1.0 

    $ play_sound(speaker,fadein=0.5,fadeout=0.5)

    "President" "To all the newcomer students, I welcome you!"

    "President" "I hope that you can achieve your dreams in this school."

    scene audi2 with dissolve

    "President" "To all those that are nearing graduation, I hope you achieved what you wanted here."

    scene audi3 with dissolve

    $ play_sound(clap,fadein=2.0)

    "President" "That is all for my speech. Thank you!"

    "{i}Students clapping{/i}"

    show kurtney happy teeth with dissolve
    

    if metYui is True:
        kk "Dude! I hope we are classmates in this new school year."

        play sound "audio/voice/case1/me/m108.ogg"
        m "Oh please no."

        show kurtney angry talk with dissolve

        kk "Why? I'm fun to hang out with right?"

        play sound "audio/voice/case1/me/m1.ogg"
        m "Yeah yeah whatever you say."

        "This is [kk]. My weird childhood friend."

        "We have been friends since elementary school. She is a little boyish and sometimes annoying."

        "But I don't hate it at all."

        show kurtney happy teeth with dissolve

        kk "Dude we're already 2nd year in highschool. When are you getting a girlfriend?"

        play sound "audio/voice/case1/me/m1.ogg"
        m "Why are you even asking me that. Even if I wanted to have one, no one likes me at all!"

        show kurtney smile with dissolve

        kk "You poor little thing. Don't worry, I'll always be here for you so you don't look like a loser."

        play sound "audio/voice/case1/me/m1.ogg"
        m "Well, don't even talk like you have one."

        show kurtney happy teeth with dissolve

        kk "Hahaha~ Don't worry about me. I'm more worried about your future."

        play sound "audio/voice/case1/me/m1.ogg"
        m "I'm not a child for you to worry about."

        kk "Haha!!"

    else:
        kk "Dude! I hope we are classmates in this new school year."

        play sound "audio/voice/case1/me/m108.ogg"
        m "Oh please no."

        show kurtney angry talk

        kk "Why? I'm fun to hang out with right?"

        play sound "audio/voice/case1/me/m1.ogg"
        m "Yeah yeah whatever you say."


    
    $ renpy.end_replay()
    jump afterCeremony

label afterCeremony:

    scene audi4 

    show kurtney smile
    with fade
    kk "Lemme check the school bulletin to know our section."

    play sound "audio/voice/case1/me/m109.ogg"
    m "Sure dude. Gonna go to the bathroom first."

    kk "Meet me near the school bulletin okay?"
    
    play sound "audio/voice/case1/me/m110.ogg"
    m "Yeah just go."

    scene football with fade

    "A new school year..."

    "I hope it is fun..."

    scene pools with fade

    "Last year, I was a loner in my class."

    "But thankfully, I have [kk]. She's a really good childhood friend."

    

    #Flag to check if USER accepts lunch invite
    $ lunchWithYui = True
    stop music fadeout 2.0
    pause 1.0
    scene hallway 
    show screen lostTransition
    play sound "audio/music/Transition2.ogg"
    with fade
    pause 3.0
    hide screen lostTransition
    $ persistent.unlockHallway = True
    $ play_music(legends,fadein=2.0)

    if metYui is True:

        "???" "Hey..."

        "???" "M-M-Mark!"

        show yui blush closed with dissolve

        play sound "audio/voice/case1/me/m111.ogg"
        m "Ehhhhh!!!?"

        play sound "audio/voice/case1/me/m112.ogg"
        m "Yui?! You go to my school?"

        show yui blush with dissolve

        y "Y-Yeah! Did you not no-notice my uniform?"

        play sound "audio/voice/case1/me/m113.ogg"
        m "I did not notice it at all. Oh my!"

        #play sound "audio/voice/case1/me/m.ogg"
        m "So you are a First Year student."

        play sound "audio/voice/case1/me/m114.ogg"
        m "Why didn't you tell me?"

        play sound "audio/voice/case1/me/m115.ogg"
        m "No.. sorry. It's my fault."

        show yui smile close with dissolve

        y "No... it's fine! I forgot to tell you we go to the same school."

        show yui worry opened with dissolve

        y "Uhm... M-M-Mark?"

        play sound "audio/voice/case1/me/m116.ogg"
        m "Yeah?"

        y "Can you help me get to my classroom?"

        play sound "audio/voice/case1/me/m117.ogg"
        m "Are you perhaps lost?"

        show yui smile close with dissolve

        y "Yeah... this school is really big."

        play sound "audio/voice/case1/me/m118.ogg"
        m "No wonder. It's just like me when I was a First Year student."

        play sound "audio/voice/case1/me/m119.ogg"
        m "So, you're currently in the Second Year's building."

        scene hallway with fade



        # This choice will determine who will eat lunch with MC
        $ timeout_label = "leaveYui"
        menu findRoomWithYui:
    
            "Go and find the classroom with Yui.":

                scene school building with fade
                #play sound "audio/voice/case1/me/m.ogg"
                m "Haaa.."

                show yui blush closed with dissolve

                y "Waaaah.. I'm so sweaty."

                play sound "audio/voice/case1/me/m120.ogg"
                m "Yeah it's kinda far from our building. Hahaha~"

                play sound "audio/voice/case1/me/m121.ogg"
                m "Just go inside there. All First Year classes are in this building."

                show yui blush with dissolve

                "{i}8:50 AM...{/i}"

                play sound "audio/voice/case1/me/m122.ogg"
                m "The first bell is gonna ring now."

                play sound "audio/voice/case1/me/m123.ogg"
                m "I'm going back now [y]!"

                play sound "audio/voice/case1/me/m124.ogg"
                m "Have fun in there!"

                show yui blush closed with dissolve

                y "W-w-waaaait Mark!"

                y "Uhm...."

                show yui blush with dissolve

                y "If it's fine with you.."

                y "Can I treat you later in lunch? As a thanks for helping me..."

                $ timeout_label = "notLunch"

                menu:
                    "Ehhhh? I've never been invited by a girl to lunch. What should I do?"

                    "Sure I'll go eat with you.":
                        $ persistent.unlockCafeteria = True
                        play sound "audio/voice/case1/me/m125.ogg"
                        m "Sure I'll go eat with you."

                        show yui wow with dissolve

                        y "For real? Waaaah!"

                        show yui smile close with dissolve

                        python:

                            if achievementList[13] == False:
                                    
                                achievement.grant("Lunch Date")
                                renpy.notify("Achievement Unlocked: Lunch Date")
                                renpy.play("audio/sfx/achievement.ogg",channel="sound")
                                achievementList[13] = True

                        play sound "audio/voice/case1/me/m126.ogg"
                        m "Wait why are you so happy?"

                        play sound "audio/voice/case1/me/m127.ogg"
                        m "Ready your money though. I'm a big eater."

                        y "Ehehe.. sure! You can choose whatever you want."

                        $ play_sound(bell) 

                        "{i}♫ Kin kon kan kon ♫{/i}"

                        show yui worry with dissolve

                        pause 2.0

                        play sound "audio/voice/case1/me/m128.ogg"
                        m "Oh crap that's the bell!"

                        play sound "audio/voice/case1/me/m129.ogg"
                        m "I'll be going now [y]!"

                        show yui smile opened with dissolve

                        y "See you later.... M-Mark."

                        jump lunch

                    "Sorry, maybe next time?":

                        label notLunch:
                            
                            play sound "audio/voice/case1/me/m130.ogg"
                            m "Sorry, maybe in another day."

                            show yui worry with dissolve

                            y "Oh.... that's... a shame."

                            show yui worry closed with dissolve

                            y "I... I see..."

                            show yui smile close with dissolve

                            y "See you..."

                            scene school building with fade

                            "She left running while her hands is in her eyes."

                            "...."

                            jump lunch

            "Go to [kk] in the school bulletin and leave Yui":

                label leaveYui:
                    $ lunchWithYui = False
                    
                    play sound "audio/voice/case1/me/m131.ogg"
                    m "I'm sorry [y]. I can't help you. I have somewhere to go with my friend."

                    show yui worry with dissolve

                    y "Ah.... Is that so?"

                    show yui worry closed with dissolve

                    y "That's a real shame."

                    show yui smile close with dissolve

                    y "I'll be going now Mark."

                    scene hallway with fade

                    "She left running with a troubled expression on her face."

                    "...."

                    jump lunch
    else:

        "???" "Uhmmm..."

        "???" "Excu-cuse m-m-me....!"

        "Looking at my back, there is someone pull my sleeves..."

        show yui smile close with fade

        #play sound "audio/voice/case1/me/m.ogg"
        m "Uhhhh.. Hello?"

        #play sound "audio/voice/case1/me/m.ogg"
        m "You are?"

        "Girl" "Can you help me get to my classroom?"

        play sound "audio/voice/case1/me/m117.ogg"
        m "Are you perhaps lost?"

        show yui worry opened with dissolve

        "Girl" "Yeah... this school is really big."

        #play sound "audio/voice/case1/me/m.ogg"
        m "No wonder. It's just like me when I was a First Year student. Haha~"

        play sound "audio/voice/case1/me/m.ogg"
        m "You are currently in the Second Year's building."

        show yui neutral with dissolve

        "Girl" "Uhmm..."

        "Girl" "Can you tell me your name?"

        #play sound "audio/voice/case1/me/m.ogg"
        m "Ohhh. My name is Mark. How about you?"

        show yui blush with dissolve

        "Girl" "Y-Y-Yu.."

        #play sound "audio/voice/case1/me/m.ogg"
        m "Yu?"

        show yui surprised blush with dissolve

        "She's gotten a bit red of a sudden..."

        show yui blush closed with dissolve

        "Girl" "Ple-please call me Yui."

        #play sound "audio/voice/case1/me/m.ogg"
        m "[y], huh? What a cute name."

        show yui surprised blush with dissolve

        y "EHHH?!! Cute?"

        show yui blush closed with dissolve

        y "{i}......waaah!{/i}"

        # ADD MORE

        scene hallway with dissolve

        jump findRoomWithYui

label lunch:

    stop music fadeout 1.0

    pause 1.0

    $ play_music(relax, fadein=2.0)

    if lunchWithYui is True:

        scene black with fade

        pause 2.0

        scene class1 with fade

        t "To get the answer of this equation..."

        t "You must first..."

        $ play_sound(bell) 

        "{i}♫ Kin kon kan kon ♫{/i}"

        show clarrise talk with dissolve

        t "Okay Class! You may now take your lunch."

        t "We will have a quiz after your lunch."

        with vpunch

        "Everyone" "WHAT?!!"

        pause 1.0

        scene class1
        show kurtney talk opened 
        with fade

        kk "Hey dude wanna go to cafeteria?"

        play sound "audio/voice/case1/me/m132.ogg"
        m "Sorry dude. I'm meeting someone today."

        show kurtney happy teeth with dissolve

        kk "Meeting someone? Hey hey hey what's happening to Mr. Mark, huh?"

        play sound "audio/voice/case1/me/m133.ogg"
        m "I'm going ahead. Eat with yourself."

        show kurtney angry talk with dissolve

        kk "Wah! This little punk."

        scene black with fade
        
        pause 1.0

        scene bg cafeteria with fade

        show yui smile close with dissolve

        pause 2.0

        $ play_sound(people,fadein=2.0,fadeout=0.5)

        y "Hey Mark! Here!"

        

        play sound "audio/voice/case1/me/m134.ogg"
        m "Sorry [y]. Did you wait?"

        show yui neutral with dissolve

        y "No... I just got here..."

        play sound "audio/voice/case1/me/m135.ogg"
        m "Is that so? Then it's fine."

        show yui smile opened with dissolve

        y "So what do you want to eat?"

        y "Just tell me. I got everything covered."
        $ persistent.unlockCafeteria = True

        scene bg cafeteria with fade

        $ timeout_label = None
        menu:
            "What should I eat?"

            "Tonkotsu(Pork) Ramen. {image=ramen.png}":
                play sound "audio/voice/case1/me/m1.ogg"
                m "I want the Tonkotsu Ramen."

                show yui wow with dissolve

                y "Eh, you like Japanese dishes?"

                play sound "audio/voice/case1/me/m136.ogg"
                m "Yeah they taste good."

                y "I... I see."

            "Quarter Pound Burger with Large Fries. {image=burger.jpg}":
                
                play sound "audio/voice/case1/me/m1.ogg"
                m "I want the Quarter Pounder Burger."

                show yui wow with dissolve

                y "Eh, you like American fast-food?"

                play sound "audio/voice/case1/me/m136.ogg"
                m "Yeah they taste good."

                y "I... I see."

            "12\" All Meat Pizza with Thin Crust. {image=pizza.jpg}":
                
                play sound "audio/voice/case1/me/m137.ogg"
                m "I want the All Meat Pizza."

                show yui wow with dissolve

                y "Eh, you like pizza huh?"

                play sound "audio/voice/case1/me/m136.ogg"
                m "Yeah they taste good."

                y "I... I see."

            "Apple Risotto. {image=risotto.jpg}":
                
                play sound "audio/voice/case1/me/m138.ogg"
                m "I want the Risotto."

                show yui wow with dissolve

                y "Eh, you like Italian food huh?"

                play sound "audio/voice/case1/me/m136.ogg"
                m "Yeah they taste good."

                y "I... I see." 

            "All of it. All in. Just do it.":
                
                play sound "audio/voice/case1/me/m139.ogg"
                m "I want everything in today's menu."

                show yui wow with dissolve
                y "Ehhh? There's no way you can finish all of it."

                play sound "audio/voice/case1/me/m140.ogg"
                m "I've done it once. With my friend of course."

                play sound "audio/voice/case1/me/m141.ogg"
                m "The moment you said \"I've got everything covered\", I already knew what to do."

                show yui smile close with dissolve

                y "Hahaha~ Okay I get it!"

                python:

                    if achievementList[14] == False:
                            
                        achievement.grant("Big Eater")
                        renpy.notify("Achievement Unlocked: Big Eater")
                        renpy.play("audio/sfx/achievement.ogg",channel="sound")
                        achievementList[14] = True
                pause 0.5
    
    else:
        scene black with fade

        pause 2.0

        scene class1 with fade

        t "To get the answer of this equation..."

        t "You must first..."

        $ play_sound(bell) 

        "{i}♫ Kin kon kan kon ♫{/i}"

        show clarrise talk with dissolve

        t "Okay Class! You may now take your lunch."

        t "We will have a quiz after your lunch."

        with hpunch

        "Everyone" "WHAT?!!"

        pause 1.0

        scene class1
        show kurtney talk opened 
        with fade

        kk "Hey dude wanna go to cafeteria?"

        play sound "audio/voice/case1/me/m142.ogg"
        m "Yeah sure. Are you going to treat me?"

        show kurtney happy teeth with dissolve

        kk "Keep on dreaming. Maybe I'll treat you when you get a girlfriend~"

        scene bg cafeteria with fade
        
        #play sound "audio/voice/case1/me/m.ogg"
        m "Dude this sucks."

        show kurtney talk opened with dissolve

        kk "What?"

        play sound "audio/voice/case1/me/m144.ogg"
        m "Nothing."

        show kurtney happy teeth with dissolve

        kk "Okay I'll treat to something just for today!"

        kk "And while you still don't have a girlfriend, I'll eat with you so don't look like a loser!"

        play sound "audio/voice/case1/me/m145.ogg"
        m "Whatever!!! Arghhhh..."

        $ timeout_label = None

        menu:
            "What should I eat?"

            "Tonkotsu(Pork) Ramen. {image=ramen.png}":
                
                #play sound "audio/voice/case1/me/m.ogg"
                m "I want the Tonkotsu Ramen."

                show kurtney talk opened with dissolve

                kk "Eh, you like Japanese dishes?"

                play sound "audio/voice/case1/me/m136.ogg"
                m "Yeah they taste good."

                kk "I... I see."

            "Quarter Pound Burger with Large Fries. {image=burger.jpg}":
                
                #play sound "audio/voice/case1/me/m.ogg"
                m "I want the Quarter Pounder Burger."

                show kurtney talk opened with dissolve

                kk "Eh, you like American fast-food?"

                play sound "audio/voice/case1/me/m136.ogg"
                m "Yeah they taste good."

                kk "I... I see."

            "12\" All Meat Pizza with Thin Crust. {image=pizza.jpg}":
                
                play sound "audio/voice/case1/me/m137.ogg"
                m "I want the All Meat Pizza."

                show kurtney talk opened with dissolve

                kk "Eh, you like pizza huh?"

                play sound "audio/voice/case1/me/m136.ogg"
                m "Yeah they taste good."

                kk "I... I see."

            "Apple Risotto. {image=risotto.jpg}":
                
                play sound "audio/voice/case1/me/m138.ogg"
                m "I want the Risotto."

                show kurtney talk opened with dissolve

                kk "Eh, you like Italian food huh?"

                play sound "audio/voice/case1/me/m136.ogg"
                m "Yeah they taste good."

                kk "I... I see." 

            "All of it. All in. Just do it.":
                
                play sound "audio/voice/case1/me/m139.ogg"
                m "I want everything in today's menu."

                show kurtney talk opened with dissolve
                kk "Ehhh? There's no way you can finish all of it."

                #play sound "audio/voice/case1/me/m.ogg"
                m "Of course you'll help me. HAHAHA~"

                play sound "audio/voice/case1/me/m141.ogg"
                m "The moment you said \"I've got everything covered\", I already knew what to do."

                show kurtney talk opened with dissolve

                kk "Hahaha~ Okay I get it!"

                python:

                    if achievementList[14] == False:
                            
                        achievement.grant("Big Eater")
                        renpy.notify("Achievement Unlocked: Big Eater")
                        renpy.play("audio/sfx/achievement.ogg",channel="sound")
                        achievementList[14] = True

        "...."
        scene black with fade
        pause 2.0
    $ renpy.end_replay()
    jump socialStudiesQuiz

label socialStudiesQuiz:
    stop music fadeout 1.0
    scene class1
    show clarrise talk 
    with fade

    $ play_music(everyone,fadein=3.0)
    t "Okay Class! Listen up!"

    

    t "There will be a surprise quiz today."
    

    show clarrise talk close with dissolve

    t "It is a 10 item quiz. Make sure to review your notes."

    t "The topic is about the Republic Act No. 11313 also known as \"Safe Spaces Act.\""

    scene class1 with fade

    # Implement notes

    if metYui is True:
        "No way!!! I know this law. I could ace this test."

        show kurtney talk opened with dissolve

        kk "Hey future Attorney Mark. Do you know this law?"

        play sound "audio/voice/case1/me/m146.ogg"
        m "Of course. Leave it to me."
    else:
        "No way!!! I know this law. I could ace this test."

        show kurtney talk opened with dissolve

        kk "Hey dude. Isn't this what you've just told me earlier in the jeep?"

        play sound "audio/voice/case1/me/m147.ogg"
        m "Yeah dude. Did you remember what I said?"

        show kurtney happy teeth with dissolve

        kk "I'll try to remember it haha~"

    jump quiz

label quiz:
    $ quizPoints = 0
    $ quizNum = []
    scene class1
    show natasha talk 
    with fade
    n "Hey its me again!"

    n "Your goal in this quiz to score high points! At the end of the quiz, your correct points will be added to HBB Points!"

    n "Don't worry! Getting wrong answers will not reduce your points!"

    n "Goodluck!"
    hide natasha talk with dissolve
    pause 2.0

    show clarrise talk
    with fade
    hide screen showNotesButton
    show screen displayScore
    
    t "Okay Class! Ready or not, here I go!"
    show clarrise talk close with dissolve
    t "First Question!"
    hide clarrise talk close with dissolve
    $ timeout = 20
    $ timeout_label = "one"
    menu:
        
        "It is the law that recognizes that both men and women must have equality, security, and safety not only 
        in private but also on the streets, public spaces, online, workplaces and educational and training institutions."

        "Republic Act No. 11616":
            ""
        "Republic Act No. 11313":
            $ quizNum.append(1)
            $ quizPoints += 1
            pause 0.5
            $ play_sound(addPoints)
            play sound "audio/voice/case1/me/m148.ogg"
            m "Alright! That was an easy one."
        "Republic Act No. 11717":
            ""
        "Republic Act No. 11919":
            ""
    label one:
    $ timeout_label = "two"
    show clarrise talk with dissolve
    t "Second Question!"
    show clarrise talk close with dissolve
    hide clarrise talk close with dissolve
    menu:
        
        "Republic Act No. 11313 is commonly known as \"S____ S______ A__\""

        "Save Spaceship Act":
            ""
        "Safe Spaces Act":
            play sound "audio/voice/case1/me/m149.ogg"
            m "Okay got that one in the bag!"
            $ quizNum.append(1)
            $ quizPoints += 1
            pause 0.5
            $ play_sound(addPoints)
        "Sale Summer Act":
            ""
        "Super Smash Act":
            ""
    label two:
    $ timeout = 10
    show clarrise talk with dissolve
    t "Third Question!"
    show clarrise talk close with dissolve
    hide clarrise talk close with dissolve
    $ timeout_label = "three"
    menu:
        
        "Catcalling is a gender-based sexual harassment covered in Safe Spaces Act."
        "True":

            #play sound "audio/voice/case1/me/m.ogg"
            m "That is a freebie."
            $ quizNum.append(1)
            $ quizPoints += 1
            pause 0.5
            $ play_sound(addPoints)
        "False":
            ""
    label three:
    show clarrise talk with dissolve
    t "Fourth Question!"
    show clarrise talk close with dissolve
    hide clarrise talk close with dissolve
    $ timeout_label = "four"
    menu:
        
        "Making unwanted invitations is a gender-based sexual harassment covered in Safe Spaces Act."
        "True":
            
            play sound "audio/voice/case1/me/m150.ogg"
            m "Easy."
            $ quizNum.append(1)
            $ quizPoints += 1
            pause 0.5
            $ play_sound(addPoints)
        "False":
            ""
    label four:
    show clarrise talk with dissolve
    t "Fifth Question!"
    show clarrise talk close with dissolve
    hide clarrise talk close with dissolve
    $ timeout_label = "five"
    menu:
        
        "Stalking is included as a gender-based sexual harassment in Safe Spaces Act."
        "True":
            
            play sound "audio/voice/case1/me/m151.ogg"
            m "Okay doing good!"
            $ quizNum.append(1)
            $ quizPoints += 1
            pause 0.5
            $ play_sound(addPoints)
        "False":
            ""
    label five:
    show clarrise talk with dissolve
    t "Sixth Question!"
    show clarrise talk close with dissolve
    hide clarrise talk close with dissolve
    $ timeout_label = "six"
    menu:
        
        "Situation: You see your classmate in the classroom getting sexually harassed by a teacher. What do you do?"
        "Do nothing.":
            ""
        "Join in the act.":
            ""
        "Confront the teacher.":
            ""
        "Record the evidence and report to the faculty/police.":
            
            play sound "audio/voice/case1/me/m152.ogg"
            m "Nice going!"
            $ quizNum.append(1)
            $ quizPoints += 1
            pause 0.5
            $ play_sound(addPoints)
    label six:
    show clarrise talk with dissolve
    t "Seventh Question!"
    show clarrise talk close with dissolve
    hide clarrise talk close with dissolve
    $ timeout_label = "seven"
    menu:
        
        "Gender-based sexual harassment can also be commited in Public Utility Vehicles(PUV)."
        "True":
            
            play sound "audio/voice/case1/me/m153.ogg"
            m "That wasn't hard."
            $ quizNum.append(1)
            $ quizPoints += 1
            pause 0.5
            $ play_sound(addPoints)
        "False":
            ""
    label seven:    
    show clarrise talk with dissolve
    t "Eight Question!"
    show clarrise talk close with dissolve
    hide clarrise talk close with dissolve
    $ timeout_label = "eight"
    menu:
        
        "Gender-based sexual harassment can also be commited in Streets and Public Spaces."
        "True":
            
            play sound "audio/voice/case1/me/m154.ogg"
            m "The easiest."
            $ quizNum.append(1)
            $ quizPoints += 1
            pause 0.5
            $ play_sound(addPoints)
        "False":
            ""
    label eight:
    show clarrise talk with dissolve
    t "Ninth Question!"
    show clarrise talk close with dissolve
    hide clarrise talk close with dissolve
    $ timeout_label = "nine"
    menu:
        
        "The cyberspace is also covered in Safe Spaces Act."
        "True":
            
            play sound "audio/voice/case1/me/m155.ogg"
            m "Got it in the bag."
            $ quizNum.append(1)
            $ quizPoints += 1
            pause 0.5
            $ play_sound(addPoints)
        "False":
            ""
    label nine:
    show clarrise talk with dissolve
    t "Last Question!"
    show clarrise talk close with dissolve
    hide clarrise talk close with dissolve
    $ timeout_label = "ten"
    menu:
        
        "Public masturbation or flashing of private parts, groping, making offensive body gestures at someone, 
        and other similar lewd sexual actions is a gender-based sexual harassment in Safe Spaces Act."
        "True":
            
            play sound "audio/voice/case1/me/m156.ogg"
            m "Easy money."
            $ quizNum.append(1)
            $ quizPoints += 1
            pause 0.5
            $ play_sound(addPoints)
        "False":
            ""
    label ten:
    
    # Check quiz score
        

    scene class1 with fade

    "Class" "WAAAAAAA!"

    "Everyone is turning their heads. Asking if they did well."

    show kurtney talk opened with dissolve

    kk "What the hell. That was hard."

    hide kurtney talk opened

    play sound "audio/voice/case1/me/m157.ogg"
    m "Was it? I don't think so. Haha~"

    python:
        for i in quizNum: 
            if quizNum[i] == 1:
                hbbpoints += 1

    play sound "audio/voice/case1/me/m158.ogg"
    m "I got [quizPoints] points baby."

    python:
        if quizPoints == 10:

            if achievementList[15] == False:
                            
                achievement.grant("Galaxy Brain")
                renpy.notify("Achievement Unlocked: Galaxy Brain")
                renpy.play("audio/sfx/achievement.ogg",channel="sound")
                achievementList[15] = True

    pause 0.5

    $ play_sound(addPoints)

    "[quizPoints] points have been added to your HBB Points!"



    "Mark with a smile on his face, knew he did well."

    hide screen displayScore

    $ renpy.end_replay()

    show screen showNotesButton

    stop music fadeout 2.0
    pause 2.0

    

    # Show achievement if perfect
    # Show test result



label pervTeacher:
    
    scene class2
    show screen pervTransition
    play sound "audio/music/Piano5.ogg"
    $ persistent.unlockClass = True
    pause 3.0

    hide screen pervTransition

    scene black with fade

    centered "1 Week Later..."
    
    scene class2 with fade

    $ play_sound(people,fadein=0.2,fadeout=3.0)

    "Classroom noises...."
    pause 2.0

    show kurtney talk opened with dissolve

    $ play_music(doll,fadein=3.0)

    kk "Hey Mark, did you hear the news?"

    #play sound "audio/voice/case1/me/m.ogg"
    m "What news?"

    kk "It's about [t]."

    play sound "audio/voice/case1/me/m159.ogg"
    m "What happened to [t]."

    kk "Based on what I heard, she got sick and is in the hospital."

    kk "The school faculty doesn't know when she's going back."

    play sound "audio/voice/case1/me/m160.ogg"
    m "She's in critical condition?"

    kk "I don't know dude. That's all I know."

    kk "Ohh! I almost forgot."

    kk "There will be someone substituting [t]."

    play sound "audio/voice/case1/me/m162.ogg"
    m "Who?"

    $ play_sound(walking,fadein=0.5,fadeout=3.0)

    show kurtney angry talk with dissolve

    kk "They say he's a nasty person."

    play sound "audio/voice/case1/me/m161.ogg"
    m "O-ohh..."

    hide kurtney angry talk with dissolve

    "Noise of footsteps towards the door."

    $ play_sound(doorcreak)

    pause 2.0

    $ play_sound(pervlaugh,fadein=1.0)

    pause 1.0

    "???" "Hwehehehe... How you doin' everyone?"

    stop sound fadeout 0.5

    with hpunch

    "Everyone in the classroom gasped."

    show teacher smile1 at right with dissolve

    "???" "I hope we all get along, everyone hehehe~"

    "???" "I will be your substitute teacher for this class."

    "???" "Call me Professor Butch."

    b "These are some nice looking girls, huh?"

    b "Hehehehe... perfect for my taste."

    "What the hell did he just say?"

    "Looking at [kk], she is about to stand up."

    show kurtney talk angry at left with dissolve

    kk "What did you say?!"

    play sound "audio/voice/case1/me/m162.ogg"
    m "You idiot..."

    show teacher closed1 with dissolve

    b "Oh did I ask you to talk? You'll be receiving a failing grade."

    b "Hehehe~"

    hide teacher closed1 with dissolve

    show kurtney talk opened at center with dissolve

    kk "Wha-?"

    show kurtney talk angry at center with dissolve

    "I whispered in Kurt's ears."

    play sound "audio/voice/case1/me/m163.ogg"
    m "Just let it slide dude. I will find a way to report this nasty professor."

    show kurtney smile with dissolve

    kk "O-O-Okaay..."

    jump talkOnHarass


label talkOnHarass:
    $ helpedYui = False
    scene black with fade
    centered "A few days later..."

    if lunchWithYui is True:
        scene school building with fade
        
        "What a nice landscape."

        "I see [y] walking across the ground. With a sad expression on her face."

        show yui worry closed with fade
        play sound "audio/voice/case1/me/m164.ogg"
        m "Hey [y]! How's your class doing?"

        play sound "audio/voice/case1/me/m165.ogg"
        m "You called me out to talk about something?"

        show yui worry opened with dissolve

        y "Y-yeah..."

        show yui worry with dissolve

        y "It's about that law you talked about."

        play sound "audio/voice/case1/me/m166.ogg"
        m "The Safe Spaces Act? What about it?"

        y "I have something to talk about related to it...."

        play sound "audio/voice/case1/me/m167.ogg"
        m "Tell me about it."

        hide yui worry with dissolve

        "While clasping her hands firmly for a while, she finally opened her mouth."

        show yui worry opened with dissolve

        y "It's about my professor..."

        y "He's doing something bad... And I can't do anything to stop it."

        play sound "audio/voice/case1/me/m168.ogg"
        m "Who's this professor? Is he teaching here?"

        show yui angry with dissolve

        y "Y-yeah... I hate him. That disgusting person."

        y "When he gave a test the other day... He stares at the girls in a lascivious manner."

        y "When we are in the laboratory, he sneakily touches the butt of some of the girls."

        y "Then he says, \"It's not my fault that you are sexy.\""

        y "And then one time, he..."

        show yui crying with fade

        y "He suddenly touched my shoulders... and pinched it in a manner that is so disgusting. Then he whispered something to my ear."

        play sound "audio/voice/case1/me/m169.ogg"
        m "WHAT?!" with vpunch

        show yui angry with dissolve

        y "Aaaaah! I hate him. Just remembering it makes me puke."

        y "I was almost close to crying in the classroom. I was really shaking and trembling."

        y "The girls in my class can't speak up to him. Also when the boys stand up for us, he gives them a failing mark."

        play sound "audio/voice/case1/me/m170.ogg"
        m "Tell me who is this nasty person?"

        show yui worry opened with dissolve

        y "H-h-his name is Butch..."

        y "They said he was a new faculty teacher..."

        play sound "audio/voice/case1/me/m174.ogg"
        m "I see. So he's also teaching the First Year students. That damned bastard."

        show yui worry with dissolve

        y "M-Mark! I have a favor! Please help me out."

        play sound "audio/voice/case1/me/m172.ogg"
        m "Ahhhh..."

        $ badEndingGame = False
        $ helpedYui = False
        $ timeout = 10
        $ timeout_label = "ignorePerv"
        menu:
            "Should I help her out?"

            "Help her.":
                $ helpedYui = True
                pause 0.5

                $ hbbpoints += 5
                $ play_sound(addPoints)
                "You received {color=#40ff00}5 HBB Points.{/color}"

                python:

                    if achievementList[16] == False:
                                    
                        achievement.grant("Lending A Helping Hand")
                        renpy.notify("Achievement Unlocked: Lending A Helping Hand")
                        renpy.play("audio/sfx/achievement.ogg",channel="sound")
                        achievementList[16] = True


                play sound "audio/voice/case1/me/m173.ogg"
                m "Okay [y]! I will help you."

                y "Thank you so much!"

                y "Also before I forget to say... There was someone who took a video when he was doing the crime."

                play sound "audio/voice/case1/me/m174.ogg"
                m "Really? Then this will be easy. It should be a solid evidence for his disgusting act."

                jump arrestButch

            "Don't help her.":
                jump ignorePerv
                
        label ignorePerv:
            $ badEndingGame = True

            play sound "audio/voice/case1/me/m175.ogg"
            m "I'm afraid I cannot help. I might get in trouble."

            if not kurtneyHelp:
                kk "Is that so? That's a real shame..."

            else:
                y "Is that so? That's a real shame..."

            jump badEndStory

    else:
        scene class2
        show kurtney talk opened
        with fade

        kk "Dude... I have something to talk about."

        kk "It's about that law you talked about."

        play sound "audio/voice/case1/me/m176.ogg"
        m "The Safe Spaces Act? What about it?"

        show kurtney smile with dissolve

        kk "I think we can use this law against that professor."

        play sound "audio/voice/case1/me/m177.ogg"
        m "Tell me more about it."

        show kurtney angry talk with dissolve

        kk "Just the other day, one of our girl classmate got sexually harassed."

        play sound "audio/voice/case1/me/m178.ogg"
        m "Really? That's bad."

        show kurtney talk opened with dissolve

        kk "I've also got stories from other girls in First Year. According to them..."

        show kurtney angry talk with dissolve

        kk "When he gave a test the other day... He stares at the girls in a lascivious manner."

        kk "When they are in the laboratory, he sneakily touches the butt of some of the girls."

        kk "Then he says, \"It's not my fault that you are sexy.\""

        kk "And then one time, he... he tried to grope someone."

        play sound "audio/voice/case1/me/m179.ogg"
        m "Dude this is getting worse."

        play sound "audio/voice/case1/me/m180.ogg"
        m "We really need to do something."

        kk "Yeah I know. Here comes the good part dude."

        play sound "audio/voice/case1/me/m181.ogg"
        m "What is good in this?"

        kk "Someone took a video of that nasty bastard doing the crime."

        play sound "audio/voice/case1/me/m182.ogg"
        m "Really? That's a solid evidence then!"

        kk "I know right! That disgusting creep should rot in jail forever."

        show kurtney happy teeth with dissolve

        kk "Now will you help me out?"

        show kurtney smile with dissolve

        kk "Because of you, I learned of the Safe Spaces Act. I knew of the things which a person shouldn't ever do."

        kk "You wanted to be an Attorney right? Help me use this \"Safe Spaces Act\" to arrest that nasty piece of ****."

        $ timeout_label = "ignorePerv"
        menu:
            "Should I help her?"

            "Help her.":
                pause 0.5

                $ hbbpoints += 5
                $ play_sound(addPoints)
                "You received {color=#40ff00}5 HBB Points.{/color}"

                python:

                    if achievementList[16] == False:
                                    
                        achievement.grant("Lending A Helping Hand")
                        renpy.notify("Achievement Unlocked: Lending A Helping Hand")
                        renpy.play("audio/sfx/achievement.ogg",channel="sound")
                        achievementList[16] = True



                play sound "audio/voice/case1/me/m183.ogg"
                m "Okay [kk]! I will help you."

                kk "Thank you so much!"

                $ renpy.end_replay()

                jump arrestButch

            "Don't help her.":
                $ kurtneyHelp = False
                $ renpy.end_replay()
                jump ignorePerv

    $ renpy.end_replay()

label arrestButch:
    stop music fadeout 0.5
    scene school gate with fade
    play sound "audio/music/Transition2.ogg"
    show screen arrestTransition
    pause 3.0
    hide screen arrestTransition

    scene black
    centered "A few days later..."

     

    $ play_music(fight,fadein=0.9)

    if helpedYui is True:
        scene class2
        show teacher smile1
        with fade

        b "Bring out a pen and paper. We will be having a surprise quiz."

        $ play_sound(pervlaugh,fadein=1.0)

        b "Hwehehehehewehweh"

        "Everyone" "What?!!"

        with hpunch

        pause 2.0

        hide teacher smile1 with dissolve

        pause 2.0

        with fade

        $ play_sound(siren,fadein=1.0)

        #play sound "audio/voice/case1/me/m.ogg"
        m "Hey [kk]! Something good will happen today."

        show kurtney talk opened with dissolve

        kk "What? There's nothing good happening when there's a surprise quiz."

        kk "Police sirens?! Whaaaat?"

        play sound "audio/voice/case1/me/m185.ogg"
        m "Just wait and see dude. Haha~"

        kk "Whatever Attorney Mark."

        play sound "audio/voice/case1/me/m186.ogg"
        m "Shut up."

        scene black

        centered "A few minutes later..."

        scene hallway

        $ play_sound(walking,fadein=0.5)

        "Footsteps can be heard in the hallway."

        pause 3.0

        scene class2

        $ play_sound(doorknock)

        "???" "Excuse me. Please open the door."

        $ play_sound(radio,fadein=0.5)

        show teacher closed1 with dissolve

        b "Who the hell is disturbing my class!!!"

        hide teacher closed

        $ play_sound(doorknock)

        "Continuous knocking on the door."

        $ play_sound(doorcreak)

        "Creeeeek. The door opens."

        show officer with fade

        "Uniformed personnels came in. They appear to be police."

        play sound "audio/voice/case1/me/m187.ogg"
        m "Officer Greg!!!"

        hide officer with dissolve

        show teacher closed1 with dissolve

        b "Why is there police here?!!"

        hide teacher closed1 with dissolve

        $ play_sound(people,fadein=4.0)

        "Everyone" "What's happening? Why are they here? Did someone kill?"

        show police with fade

        "Policeman Carl" "Everyone please calm down."

        "Policeman Carl" "We have received a complaint that someone is sexually harassing a student."

        $ play_sound(radio)

        "The policeman looks at Butch."

        hide police 

        show teacher closed1 

        with dissolve

        b "What the hell are you looking at? I don't know anything about that."

        hide teacher closed1 

        show police

        with dissolve

        "Policeman Carl" "Don't explain to me. Everything that you say will be used against you."

        "Policeman Carl" "The complainant showed a solid proof of evidence."

        "Policeman Carl" "You will be coming with us. Do not resist."

        hide police with fade

        $ play_sound(people,fadein=4.0)

        "Everyone" "*gasps*"

        show officer with fade

        o "Hey future Attorney! It looks like it went fine."

        play sound "audio/voice/case1/me/m188.ogg"
        m "Waaah! Officer Greg you actually came."

        o "It's because of you, we caught this disgusting molester. Thank you."

        play sound "audio/voice/case1/me/m189.ogg"
        m "Are you praising me? Hahaha~ No big deal. I am destined to be the greatest Attorney anyways."

        o "Hahaha! I like that attitude. Keep doing good things young man."

        play sound "audio/voice/case1/me/m190.ogg"
        m "Yes Sir!"

    # Kurt scene
    else:
        scene class2
        show teacher smile1
        with fade

        b "Bring out a pen and paper. We will be having a surprise quiz."

        $ play_sound(pervlaugh,fadein=1.0)

        b "Hwehehehehewehweh"

        "Everyone" "What?!!"

        with hpunch

        pause 2.0

        hide teacher smile1 with dissolve

        pause 2.0

        with fade

        $ play_sound(siren,fadein=1.0)

        #play sound "audio/voice/case1/me/m.ogg"
        m "Hey [kk]! Something good will happen today."

        show kurtney talk opened with dissolve

        kk "What? There's nothing good happening when there's a surprise quiz."

        kk "Police sirens?! Whaaaat?"

        play sound "audio/voice/case1/me/m185.ogg"
        m "Just wait and see dude. Haha~"

        kk "Whatever Attorney Mark."

        play sound "audio/voice/case1/me/m186.ogg"
        m "Shut up."

        scene black

        centered "A few minutes later..."

        scene hallway

        $ play_sound(walking,fadein=0.5)

        "Footsteps can be heard in the hallway."

        pause 3.0

        scene class2

        $ play_sound(doorknock)

        "???" "Excuse me. Please open the door."

        $ play_sound(radio,fadein=0.5)

        show teacher closed1 with dissolve

        b "Who the hell is disturbing my class!!!"

        hide teacher closed

        $ play_sound(doorknock)

        "Continuous knocking on the door."

        $ play_sound(doorcreak)

        "Creeeeek. The door opens."

        show officer with fade

        "Uniformed personnels came in. They appear to be police."

        play sound "audio/voice/case1/me/m187.ogg"
        m "Officer Greg!!!"

        hide officer with dissolve

        show teacher closed1 with dissolve

        b "Why is there police here?!!"

        hide teacher closed1 with dissolve

        $ play_sound(people,fadein=4.0)

        "Everyone" "What's happening? Why are they here? Did someone kill?"

        show police with fade

        "Policeman Carl" "Everyone please calm down."

        "Policeman Carl" "We have received a complaint that someone is sexually harassing a student."

        $ play_sound(radio)

        "The policeman looks at Butch."

        hide police 

        show teacher closed1 

        with dissolve

        b "What the hell are you looking at? I don't know anything about that."

        hide teacher closed1 

        show police

        with dissolve

        "Policeman Carl" "Don't explain to me. Everything that you say will be used against you."

        "Policeman Carl" "The complainant showed a solid proof of evidence."

        "Policeman Carl" "You will be coming with us. Do not resist."

        hide police with fade

        $ play_sound(people,fadein=4.0)

        "Everyone" "*gasps*"

        show officer with fade

        o "Hey future Attorney! It looks like it went fine."

        play sound "audio/voice/case1/me/m188.ogg"
        m "Waaah! Officer Greg you actually came."

        o "It's because of you, we caught this disgusting molester. Thank you."

        play sound "audio/voice/case1/me/m189.ogg"
        m "Are you praising me? Hahaha~ No big deal. I am destined to be an Attorney anyways."

        o "Hahaha! I like that attitude. Keep doing good things young man."

        play sound "audio/voice/case1/me/m190.ogg"
        m "Yes Sir!"
        hide officer
        show kurtney talk opened 
        with dissolve

        kk "Hey! Don't forget about me!!"

        show officer 
        hide kurtney talk opened
        with fade

        o "Oh yes, the Attorney's friend. You will also receive compensation."

        hide officer
        show kurtney angry talk with dissolve

        kk "Nevermind compensation, why is my name \"Attorney's friend\"?!!!"

        hide officer

        with dissolve

        $ play_sound(crowdlaugh,fadein=1.5)

        "Everyone" "HAHAHAHA!!!"

        # $ friendEnding = True
    
    jump goodEndStory

label goodEndStory:

    $ goodEnding = True

    scene black

    pause 3.0

    centered "[b] was thrown into court later on to be imprisoned."

    centered "Mark was awarded a badge of honor of the school."

    centered "But that's not all!"

    centered "Mark became famous in school and many girls talked to him."

    centered "As in the words of Mark...."

    centered "\"Justice will always prevail!\" ....Thus! You shall receive girls!"

    centered "--Greatest Attorney That Ever Lived."

    centered "GOOD END"

    python:

        if achievementList[11] == False:
                    
            achievement.grant("Good End")
            renpy.notify("Achievement Unlocked: Good End")
            renpy.play("audio/sfx/achievement.ogg",channel="sound")
            achievementList[11] = True

    stop music fadeout 3.0

    pause 3.0

    $ renpy.end_replay()

    jump yui_end




label badEndStory:

    scene black

    centered "[b] went on to harass lots of students. This went on without anyone stopping him because of his position."

    centered "When the police caught on to the news, [b] went on to hiding. Never getting caught for his crimes."

    centered "BAD END"

    python:

        if achievementList[10] == False:
                    
            achievement.grant("Bad End")
            renpy.notify("Achievement Unlocked: Bad End")
            renpy.play("audio/sfx/achievement.ogg",channel="sound")
            achievementList[10] = True

    $ renpy.end_replay()

    jump yui_end

    return
