import gifos

FONT = "./fonts/ShareTechMono-Regular.ttf"
t = gifos.Terminal(width=760, height=356, xpad=24, ypad=18, font_file=FONT, font_size=17, line_spacing=6)
t.set_fps(12)
t.set_prompt("\x1b[91marcanjo\x1b[0m\x1b[90m@\x1b[0m\x1b[93march\x1b[0m \x1b[91m~\x1b[0m \x1b[93m$\x1b[0m ")

RULE = "\x1b[91m" + "=" * 60 + "\x1b[0m"
t.toggle_show_cursor(False)
t.gen_text(RULE, 1)
t.gen_text("\x1b[91m  +\x1b[0m \x1b[97mTHE WIRED\x1b[0m \x1b[90m//\x1b[0m \x1b[90msession opened\x1b[0m", 2)
t.gen_text(RULE, 3)
t.clone_frame(10)
t.toggle_show_cursor(True)

def cmd(row, text, out_row, out):
    t.gen_prompt(row)
    t.gen_typing_text(text, row, contin=True, speed=2)
    t.clone_frame(8)
    t.gen_text(out, out_row)
    t.clone_frame(14)

cmd(5, "whoami", 6, "\x1b[93m>\x1b[0m Software Engineering student \x1b[90m@\x1b[0m \x1b[91mPUCPR\x1b[0m")
cmd(7, "uname -a", 8, "\x1b[93m>\x1b[0m Arch Linux \x1b[90m(btw)\x1b[0m \x1b[90m|\x1b[0m DevSecOps")
cmd(9, "cat langs.txt", 10, "\x1b[93m>\x1b[0m Russian: \x1b[90mBasic\x1b[0m  \x1b[90m|\x1b[0m  English: \x1b[97mFluent\x1b[0m")

t.gen_prompt(11)
t.gen_typing_text("echo 'Connected to the Wired.'", 11, contin=True, speed=2)
t.clone_frame(8)
t.gen_text("\x1b[91mConnected to the Wired.\x1b[0m", 12)
t.clone_frame(6)
t.gen_prompt(13)
t.clone_frame(30)

t.gen_gif()
