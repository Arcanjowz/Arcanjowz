import gifos

t = gifos.Terminal(width=650, height=280, xpad=15, ypad=15)
t.set_prompt("arcanjo@arch ~ $ ")

t.gen_text("whoami", 1, count=25)

t.gen_text("> Software Engineering student @ PUCPR", 2)
t.clone_frame(15)

t.gen_text("> Arch Linux (btw) | DevSecOps", 3)
t.clone_frame(15)

t.gen_text("> Russian: Basic | English: Fluent", 4)
t.clone_frame(20)

t.gen_text("echo 'Connected to the Wired.'", 5, count=30)
t.clone_frame(60)

t.gen_gif()
