# 🐾 Terminal Tamagotchi

A nostalgic virtual pet that lives in your command line! Take care of your ASCII pet by feeding, playing, studying, and watching it evolve through different life stages.

## 🎮 Features

- **ASCII Art Pet**: Your pet is displayed using cute ASCII art that changes as it evolves
- **Evolution System**: Watch your pet grow from baby → teen → adult → master
- **Interactive Actions**: Feed, sleep, play games, study, and clean
- **Mini Games**: Rock-Paper-Scissors, number guessing, and riddles
- **Stats System**: Hunger, Energy, Happiness, Intelligence with visual bars
- **Persistence**: Your pet stays alive even when you close the game
- **Random Events**: Surprise events that affect your pet's stats
- **Animations**: Simple frame-based animations for actions

## 🚀 How to Run

```bash
python3 tamagotchi.py
```
https://codespaces.new/AdwikaVishal/tamagotchi


No additional dependencies required - uses only Python standard library!

## 🎯 Controls

- `f` or `feed` - Feed your pet (increases hunger)
- `s` or `sleep` - Let your pet nap (restores energy)  
- `p` or `play` - Play mini-games (increases happiness)
- `st` or `study` - Study session (increases intelligence)
- `c` or `clean` - Clean up messes (removes messy state)
- `q` or `quit` - Save and exit

## 📊 Stats Explained

- **Hunger**: Decreases over time, feed to restore
- **Energy**: Used for activities, sleep to restore  
- **Happiness**: Gained through play and games
- **Intelligence**: Increased through studying and riddles
- **Level/XP**: Gained through all activities, triggers evolution

## 🌟 Evolution Stages

### Baby (Level 1-2)
```
   ◕   ◕  
     ω    
  \     / 
   ‾‾‾‾‾  
```

### Teen (Level 3-5)
```
  ◉     ◉ 
     ▽    
 \       /
  ‾‾‾‾‾‾‾ 
```

### Adult (Level 6-9)
```
 ◉  ___  ◉
    \_/   
\         /
 ‾‾‾‾‾‾‾‾‾
```

### Master (Level 10+)
```
★ ◉ ___ ◉ ★
    \_/    
 \       / 
  ‾‾‾‾‾‾‾  
```

## 🎮 Mini Games

1. **Rock-Paper-Scissors**: Classic game against your pet
2. **Number Guessing**: Guess the number between 1-10
3. **Riddles**: Answer fun riddles to boost intelligence

## ⚠️ Game Over Conditions

- If 2 or more stats reach 0, your pet runs away
- Keep your pet healthy by balancing all stats
- Stats decay over time, so check in regularly!

## 💾 Save System

Your pet's data is automatically saved to `tamagotchi_save.json`. Delete this file to start fresh with a new pet.

## 🎨 Special States

- **😷 SICK**: When one stat hits 0
- **💩 MESSY**: Random chance after feeding (use clean command)
- **Animations**: Eating, sleeping, and evolution sequences

## 🏆 Tips

- Play regularly to keep stats balanced
- Study to unlock higher intelligence for better riddle performance
- Sleep when energy is low to maximize efficiency
- Clean up messes to maintain happiness
- Try different mini-games for varied XP gains

---

*Built for the Open Innovation Sprint - A terminal-based throwback to the classic 90s virtual pets!*