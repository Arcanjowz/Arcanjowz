import gifos

t = gifos.Terminal(width=650, height=280, xpad=15, ypad=15)
t.set_prompt("arcanjo@arch ~ $ ")

t.gen_text("whoami", 1)
t.gen_text("> Software Engineering student @ PUCPR", 2)
t.gen_text("> Arch Linux (btw) | DevSecOps", 3)
t.gen_text("> Russian: Basic | English: Fluent", 4)
t.gen_text("echo 'Connected to the Wired.'", 5)

t.gen_gif()
