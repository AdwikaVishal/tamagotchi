#!/usr/bin/env python3
import json
import time
import random
import os
import sys
from datetime import datetime, timedelta

class Tamagotchi:
    def __init__(self, name="Tama"):
        self.name = name
        self.hunger = 80
        self.energy = 80
        self.happiness = 80
        self.intelligence = 20
        self.age = 0
        self.xp = 0
        self.level = 1
        self.sick = False
        self.messy = False
        self.last_update = datetime.now()
        self.animation_frame = 0
        
        # Evolution stages
        self.stages = ["baby", "teen", "adult", "master"]
        
        # ASCII art for different stages and states
        self.art = {
            "baby": [
                "   ◕   ◕  ",
                "     ω    ",
                "  \\     / ",
                "   ‾‾‾‾‾  "
            ],
            "teen": [
                "  ◉     ◉ ",
                "     ▽    ",
                " \\       /",
                "  ‾‾‾‾‾‾‾ "
            ],
            "adult": [
                " ◉  ___  ◉",
                "    \\_/   ",
                "\\         /",
                " ‾‾‾‾‾‾‾‾‾"
            ],
            "master": [
                "★ ◉ ___ ◉ ★",
                "    \\_/    ",
                " \\       / ",
                "  ‾‾‾‾‾‾‾  "
            ],
            "sleeping": [
                "  ◕   ◕   ",
                "     ω     ",
                " Zzz...    ",
                "  ‾‾‾‾‾‾   "
            ],
            "eating": [
                "  ◕   ◕   ",
                "    ◯ω◯   ",
                " *munch*   ",
                "  ‾‾‾‾‾‾   "
            ],
            "sick": [
                "  ×   ×   ",
                "     ~    ",
                "  \\     / ",
                "   ‾‾‾‾‾  "
            ]
        }

    def get_stage(self):
        if self.level >= 10: return "master"
        elif self.level >= 6: return "adult"
        elif self.level >= 3: return "teen"
        else: return "baby"

    def display(self, state=None):
        os.system('clear' if os.name == 'posix' else 'cls')
        
        # Header
        print(f"\n🐾 {self.name} the Tamagotchi 🐾")
        print("=" * 30)
        
        # Pet display
        art_key = state if state else self.get_stage()
        if self.sick and not state:
            art_key = "sick"
        
        pet_art = self.art[art_key]
        for line in pet_art:
            print(f"    {line}")
        
        # Status indicators
        status = []
        if self.sick: status.append("😷 SICK")
        if self.messy: status.append("💩 MESSY")
        if status:
            print(f"\n    {' '.join(status)}")
        
        # Stats
        print(f"\n📊 Stats:")
        print(f"   Hunger:      {'█' * (self.hunger//10)}{'░' * (10-self.hunger//10)} {self.hunger}%")
        print(f"   Energy:      {'█' * (self.energy//10)}{'░' * (10-self.energy//10)} {self.energy}%")
        print(f"   Happiness:   {'█' * (self.happiness//10)}{'░' * (10-self.happiness//10)} {self.happiness}%")
        print(f"   Intelligence:{'█' * (self.intelligence//10)}{'░' * (10-self.intelligence//10)} {self.intelligence}%")
        print(f"   Level: {self.level} ({self.get_stage().title()}) | Age: {self.age} | XP: {self.xp}")

    def animate_action(self, action, duration=2):
        frames = 3
        for i in range(frames):
            self.display(action)
            time.sleep(duration / frames)
        self.display()

    def feed(self):
        if self.hunger >= 100:
            print("🍽️ I'm already full!")
            return
        
        self.animate_action("eating")
        self.hunger = min(100, self.hunger + 25)
        self.happiness = min(100, self.happiness + 5)
        self.xp += 2
        
        if random.random() < 0.3:
            self.messy = True
        
        print("🍎 Yummy! *munch munch*")
        self.check_evolution()

    def sleep(self):
        if self.energy >= 100:
            print("😴 I'm not tired!")
            return
            
        self.animate_action("sleeping", 3)
        self.energy = min(100, self.energy + 40)
        self.age += 1
        self.xp += 3
        
        print("💤 *yawn* That was a good nap!")
        self.check_evolution()

    def play(self):
        if self.energy < 20:
            print("😪 Too tired to play!")
            return
            
        games = ["rock-paper-scissors", "guess-number", "riddle"]
        game = random.choice(games)
        
        if game == "rock-paper-scissors":
            self.play_rps()
        elif game == "guess-number":
            self.play_guess()
        else:
            self.play_riddle()

    def play_rps(self):
        choices = ["rock", "paper", "scissors"]
        pet_choice = random.choice(choices)
        
        print("🎮 Let's play Rock-Paper-Scissors!")
        user_choice = input("Choose (rock/paper/scissors): ").lower()
        
        if user_choice not in choices:
            print("Invalid choice!")
            return
            
        print(f"You: {user_choice} | Me: {pet_choice}")
        
        if user_choice == pet_choice:
            result = "tie"
        elif (user_choice == "rock" and pet_choice == "scissors") or \
             (user_choice == "paper" and pet_choice == "rock") or \
             (user_choice == "scissors" and pet_choice == "paper"):
            result = "win"
        else:
            result = "lose"
        
        if result == "win":
            print("🎉 You won! Great game!")
            self.happiness = min(100, self.happiness + 15)
            self.xp += 5
        elif result == "tie":
            print("🤝 It's a tie!")
            self.happiness = min(100, self.happiness + 10)
            self.xp += 3
        else:
            print("😄 I won! Good game!")
            self.happiness = min(100, self.happiness + 12)
            self.xp += 4
            
        self.energy = max(0, self.energy - 15)
        self.check_evolution()

    def play_guess(self):
        number = random.randint(1, 10)
        print("🎯 I'm thinking of a number between 1-10!")
        
        try:
            guess = int(input("Your guess: "))
            if guess == number:
                print(f"🎊 Correct! It was {number}!")
                self.happiness = min(100, self.happiness + 20)
                self.intelligence = min(100, self.intelligence + 10)
                self.xp += 8
            else:
                print(f"❌ Nope! It was {number}. Good try!")
                self.happiness = min(100, self.happiness + 8)
                self.intelligence = min(100, self.intelligence + 5)
                self.xp += 3
        except ValueError:
            print("That's not a number!")
            return
            
        self.energy = max(0, self.energy - 10)
        self.check_evolution()

    def play_riddle(self):
        riddles = [
            ("What has keys but no locks?", "keyboard"),
            ("What gets wet while drying?", "towel"),
            ("What has hands but cannot clap?", "clock")
        ]
        
        riddle, answer = random.choice(riddles)
        print(f"🧩 Riddle: {riddle}")
        
        user_answer = input("Answer: ").lower().strip()
        if answer in user_answer:
            print("🧠 Brilliant! You're so smart!")
            self.happiness = min(100, self.happiness + 15)
            self.intelligence = min(100, self.intelligence + 15)
            self.xp += 10
        else:
            print(f"🤔 The answer was '{answer}'. You'll get it next time!")
            self.happiness = min(100, self.happiness + 5)
            self.intelligence = min(100, self.intelligence + 8)
            self.xp += 4
            
        self.energy = max(0, self.energy - 12)
        self.check_evolution()

    def study(self):
        if self.energy < 15:
            print("📚 Too tired to study!")
            return
            
        print("📖 Time to study!")
        subjects = ["Math", "Science", "History", "Art"]
        subject = random.choice(subjects)
        
        print(f"Today's lesson: {subject}")
        time.sleep(1)
        
        self.intelligence = min(100, self.intelligence + 20)
        self.energy = max(0, self.energy - 15)
        self.xp += 6
        
        if self.intelligence > 80:
            print("🎓 Wow! You're getting really smart!")
        else:
            print("🧠 Learning is fun!")
            
        self.check_evolution()

    def clean(self):
        if not self.messy:
            print("✨ I'm already clean!")
            return
            
        print("🧽 *scrub scrub* Much better!")
        self.messy = False
        self.happiness = min(100, self.happiness + 10)
        self.xp += 2

    def check_evolution(self):
        old_level = self.level
        self.level = 1 + (self.xp // 20)
        
        if self.level > old_level:
            old_stage = self.stages[min(old_level-1, len(self.stages)-1)]
            new_stage = self.get_stage()
            
            if old_stage != new_stage:
                print(f"\n🌟 EVOLUTION! 🌟")
                print(f"{self.name} evolved from {old_stage} to {new_stage}!")
                time.sleep(2)

    def update_stats(self):
        now = datetime.now()
        minutes_passed = (now - self.last_update).total_seconds() / 60
        
        if minutes_passed >= 1:  # Decay every minute for demo
            decay = int(minutes_passed)
            self.hunger = max(0, self.hunger - decay * 2)
            self.energy = max(0, self.energy - decay * 1)
            self.happiness = max(0, self.happiness - decay * 1)
            
            # Check if pet gets sick
            zero_stats = sum([self.hunger == 0, self.energy == 0, self.happiness == 0])
            if zero_stats >= 2:
                return "game_over"
            elif zero_stats == 1:
                self.sick = True
            else:
                self.sick = False
                
            self.last_update = now
            
        return "alive"

    def random_event(self):
        if random.random() < 0.1:  # 10% chance
            events = [
                "🎈 I found a balloon! +happiness",
                "🌟 I learned something new! +intelligence", 
                "😴 I feel sleepy... -energy",
                "🍎 I'm getting hungry... -hunger"
            ]
            
            event = random.choice(events)
            print(f"\n{event}")
            
            if "happiness" in event:
                self.happiness = min(100, self.happiness + 10)
            elif "intelligence" in event:
                self.intelligence = min(100, self.intelligence + 5)
            elif "energy" in event:
                self.energy = max(0, self.energy - 10)
            elif "hunger" in event:
                self.hunger = max(0, self.hunger - 10)

    def save_game(self):
        data = {
            "name": self.name,
            "hunger": self.hunger,
            "energy": self.energy,
            "happiness": self.happiness,
            "intelligence": self.intelligence,
            "age": self.age,
            "xp": self.xp,
            "level": self.level,
            "sick": self.sick,
            "messy": self.messy,
            "last_update": self.last_update.isoformat()
        }
        
        with open("tamagotchi_save.json", "w") as f:
            json.dump(data, f)

    @classmethod
    def load_game(cls):
        try:
            with open("tamagotchi_save.json", "r") as f:
                data = json.load(f)
            
            pet = cls(data["name"])
            pet.hunger = data["hunger"]
            pet.energy = data["energy"]
            pet.happiness = data["happiness"]
            pet.intelligence = data["intelligence"]
            pet.age = data["age"]
            pet.xp = data["xp"]
            pet.level = data["level"]
            pet.sick = data["sick"]
            pet.messy = data["messy"]
            pet.last_update = datetime.fromisoformat(data["last_update"])
            
            return pet
        except FileNotFoundError:
            return None

def main():
    print("🐾 Welcome to Terminal Tamagotchi! 🐾")
    
    # Try to load existing pet
    pet = Tamagotchi.load_game()
    
    if pet:
        print(f"Welcome back! {pet.name} missed you!")
    else:
        name = input("What's your pet's name? ") or "Tama"
        pet = Tamagotchi(name)
        print(f"Meet {pet.name}! Take good care of them!")
    
    time.sleep(2)
    
    while True:
        status = pet.update_stats()
        
        if status == "game_over":
            pet.display()
            print(f"\n💔 {pet.name} ran away because you didn't take care of them!")
            print("Game Over. Start a new game by deleting tamagotchi_save.json")
            break
        
        pet.display()
        pet.random_event()
        
        print("\n🎮 Commands:")
        print("  [f]eed  [s]leep  [p]lay  [st]udy  [c]lean  [q]uit")
        
        choice = input("\nWhat do you want to do? ").lower().strip()
        
        if choice in ['f', 'feed']:
            pet.feed()
        elif choice in ['s', 'sleep']:
            pet.sleep()
        elif choice in ['p', 'play']:
            pet.play()
        elif choice in ['st', 'study']:
            pet.study()
        elif choice in ['c', 'clean']:
            pet.clean()
        elif choice in ['q', 'quit']:
            pet.save_game()
            print(f"👋 Goodbye! {pet.name} will miss you!")
            break
        else:
            print("❓ Unknown command!")
        
        pet.save_game()
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()