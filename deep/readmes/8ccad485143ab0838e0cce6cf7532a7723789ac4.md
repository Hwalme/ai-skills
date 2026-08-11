# Puzzle Activity Planner — Claude Code Skill

A Claude Code skill that helps teachers, parents, and event organizers plan engaging puzzle-based activities for classrooms, parties, team-building sessions, and special events.

## What It Does

Describe your event, audience, or goal — and get a complete activity plan including:

- **Puzzle selection** — which puzzle types best fit the occasion
- **Step-by-step timeline** — minute-by-minute activity flow
- **Pre-configured generator links** — one-click links to create each puzzle (with URL parameters pre-filled)
- **Materials & prep checklist** — what to print and prepare
- **Differentiation tips** — adapt for mixed skill levels or age groups

## Supported Puzzle Types

| Type | Best For | Generator |
|------|----------|-----------|
| **Word Search** | Vocabulary building, warm-ups, brain training | [jigsawmake.com/word-search-maker](https://jigsawmake.com/word-search-maker) |
| **Crossword** | Vocabulary review, test prep, party games | [jigsawmake.com/crossword-puzzle-maker](https://jigsawmake.com/crossword-puzzle-maker) |
| **Sudoku** | Math warm-ups, logic training, focus time | [jigsawmake.com/sudoku-puzzle-maker](https://jigsawmake.com/sudoku-puzzle-maker) |
| **Bingo** | Group games, parties, classroom review | [jigsawmake.com/bingo-card-generator](https://jigsawmake.com/bingo-card-generator) |
| **Jigsaw** | Ice-breakers, collaborative activities, crafts | [jigsawmake.com](https://jigsawmake.com/) |

All generators are **100% free**, run client-side in the browser, and require no signup.

## URL Parameters

Generator links include pre-filled parameters so users get ready-to-use puzzles in one click:

```
# Word Search with solar system theme
https://jigsawmake.com/word-search-maker?title=Solar%20System&words=MERCURY,VENUS,EARTH,MARS,JUPITER&gridSize=12

# Crossword with AI-generated clues baked into the URL
https://jigsawmake.com/crossword-puzzle-maker?title=Ocean%20Animals&clues=DOLPHIN:Smart%20marine%20mammal|OCTOPUS:Has%20eight%20arms

# Easy Sudoku, 3 pages, 6 puzzles per page
https://jigsawmake.com/sudoku-puzzle-maker?difficulty=easy&pageCount=3&puzzlesPerPage=6

# Baby shower bingo with 20 cards
https://jigsawmake.com/bingo-card-generator?title=Baby%20Shower%20Bingo&items=First%20Smile,Diaper,Pacifier&cardCount=20

# Heart-shaped jigsaw puzzle
https://jigsawmake.com/?shape=heart&tilesX=10&tilesY=8
```

## Installation

### Option 1: Clone directly

```bash
git clone https://github.com/fruitwyatt/puzzle-activity-planner.git ~/.claude/skills/puzzle-activity-planner
```

### Option 2: Download the skill file

```bash
mkdir -p ~/.claude/skills/puzzle-activity-planner
curl -o ~/.claude/skills/puzzle-activity-planner/SKILL.md \
  https://raw.githubusercontent.com/fruitwyatt/puzzle-activity-planner/main/SKILL.md
```

## Usage

In Claude Code, type:

```
/puzzle-activity-planner Plan a 45-minute puzzle station for my 3rd grade science class about the solar system
```

Or just describe what you need:

```
/puzzle-activity-planner I need activities for a bridal shower with 20 guests
```

### More Examples

- `Plan a rainy day activity for kids ages 5-10`
- `Create a team-building puzzle session for 15 new hires`
- `Help me plan Halloween party games for 30 kids`
- `Plan a puzzle-based review session for middle school history class`

## License

MIT
