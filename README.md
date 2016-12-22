## Breakout with Pygame

Breakout is a poorly optimized, buggy, incomplete, poorly coded port ofthe legendary Breakout from the Atari 2600. The only redeeming factor is that you can create custom levels with agonizing effort.

Do I get points for honesty?

### Custom Level format

```markdown

Levels are stored in a list named "blocks":

`blocks = []`

A level is composed of a list of lists. Each individual list inside the list composes a block.

Blocks are formatted as such:

`[x location, y location, set to be destroyed (bool)]`

You can use `blocks.append([x,y,False])` to insert individual blocks into the level.

Level data is contained in the following lines:
`
173. blocks = []
174. lvl1 = []
175. block = pygame.sprite.Sprite()
176. block.image = pygame.image.load("block.png")
177. for x in range(64, 768, 32):
178.     for y in range(96, 256, 32):
179.         lvl1.append([x, y, False])
180. blocks = lvl1
`
Create variable, name it whatever you want. Fill it with your blocks according to the above format.
Set blocks equal to that variable. Now you can play with your custom level.

```

### Support or Contact

Need help? Email me at brianxu01@gmail.com. Putting my email here is probably a bad idea but whatever.
