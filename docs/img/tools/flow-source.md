# Current guide inputs for the battle-flow diagrams

Exact seven-step text from PLAYER-GUIDE.md#original-trip and #arrange-trip.

Regenerate from the repository root: `python docs/img/tools/make_flow.py docs/img/tools/flow-source.md`


### Original rules (Original mode, or extra content with the five ARRANGE switches Off)

1. **You enter the dungeon.** HP is full, the SUP.HP / SUP.TP pools are full (your refill reserve), the bag holds 12 heals.
   - "The pools are my budget for this whole trip. Every point I spend comes out of them."
2. **Fight 1, three weak enemies.** You take 300 damage. After the win, HP stays where it is. If you switched on the game's own Auto Fill option, HP refills and the SUP.HP pool pays for it 1:1 (Auto Fill starts off in both Original and Extra Content modes).
   - "Fine, cheap fight. Refill now from the pool, or carry the damage and save the pool? Pool first, it is early."
3. **Fight 2, a tougher pair.** One enemy inflicts Slow. You weigh curing it or hitting harder.
   - "If I cure, that is an action lost. If I ignore it, I take two more hits. Cure, the boss is still ahead."
4. **Fight 3, an ambush.** You try to escape. The roll fails. You take a round of damage, then it works.
   - "Escape is a dice roll. Burned a turn and 400 HP. The pool will not cover the boss if this keeps up."
5. **Between fights.** The pool is at 30 percent. You check the bag.
   - "Use heals now, or save them for the boss? Turn back to the save tree and refill the pools, or push on?"
   - This is the decision the original game is built around.
6. **Boss.** HP starts wherever you left it. You can throw as many heals as you own. The boss shrugs off your ailment spells; your counterattack sphere triggers now and then, on its roll.
   - "Ailments won't stick on him. It comes down to his elemental weakness, my stats and my heal count. Spam heals, outlast, keep everyone alive."
7. **After the boss.** Pools nearly empty, bag half gone.
   - "Back to a save tree before the next area. I need the refill."


### Arrange rules (BATTLE and MANY on, ARRANGE switches On)

1. **You enter the dungeon.** Full HP, full pools, 12 heals.
   - "HP is not my trip budget here. TP still draws on SUP.TP."
2. **Fight 1, three weak enemies.** You take 300 damage. After the win your HP is full again; the pool is untouched.
   - "HP refills for free; any TP I spend still uses its reserve."
3. **Fight 2, a tougher pair.** Slow lands on you. Your counterattack sphere now triggers whenever it is allowed to, not on a roll; crits land on more moves.
   - "Cure or hit? Hitting is better here, my counters are doing half the work."
4. **Fight 3, an ambush.** You pick Escape. It works whenever escape is allowed at all.
   - "Not worth fighting. Gone."
5. **Between fights.** HP is full; check the TP reserve before the boss.
   - "Enough SUP.TP left? Then straight to the boss."
6. **Boss.** You start at full HP. You may use at most 5 of each item in this fight. Ailments now work on the boss; the chain and break gauges reward attacking in rhythm.
   - "Five of each healing item, so each use must be timed. Can I Slow him? Yes. Break gauge is at 60 percent, two more hits and his guard drops. Pattern, not endurance."
7. **After the boss.** Full HP again.
   - "On to the next area."


### One line each

- Original: the hard part is the journey. You ration a pool across many fights, and the boss is an endurance test you can brute-force with items.
- Arrange: The hard part is each boss. Each fight has a limit of five of each item. HP recovery is free after battle; TP still uses the SUP.TP reserve.
