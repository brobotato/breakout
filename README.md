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

`173. blocks = []`
`174. lvl1 = []`
`175. block = pygame.sprite.Sprite()`
`176. block.image = pygame.image.load("block.png")`
`180. blocks = lvl1`
```
### To create a custom level:

```markdown

Create a custom level by making a custom variable and filling it with block data as shown above.

ex.

`customlvl = []`

`for x in range(64, 768, 32):`
`     for y in range(96, 256, 32):`
`         customlvl.append([x, y, False])`

Then, go into main() and insert this piece of code somewhere in the loop

`if (pygame.key.get_pressed()[pygame.YOUR-KEY] != 0) & (playing == False):`
  `blocks = customlvl`
  `level_name = "Level Name"`
  
Replace YOUR-KEY with the key that should designate your level.
Replace customlvl with the level variable's name
Replace Level Name with the Level's name.

```
