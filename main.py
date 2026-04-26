#!/usr/bin/env python3
import sys
import qrcode
import os
import subprocess


def generar_qr():
    link = sys.argv[1]
    if sys.argv[2].upper() == "DEFAULT":
        color_relleno = "black"
        color_fondo = "white"
        opcion = "S"
    elif len(sys.argv) != 5:
        print("❌ Error: Missing arguments.")
        print("Usage: python3 script.py <Link> <Fill_Color> <Background_Color> <C/G>")
        return
    else:
        color_relleno = sys.argv[2]
        color_fondo = sys.argv[3]
        opcion = sys.argv[4].upper()

    
    



    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color=color_relleno, back_color=color_fondo)

    ruta_escritorio = os.path.expanduser("~/Desktop/codigo_qr.png")

    if opcion == "S":
        img.save(ruta_escritorio)
        print(f"✅ Saved locally at: {ruta_escritorio}")

    elif opcion == "C":
        img.save(ruta_escritorio)
        try:
            subprocess.run([
                "osascript", "-e", 
                f'set the clipboard to (read (POSIX file "{ruta_escritorio}") as «class PNGf»)'
            ], check=True)
            os.remove(ruta_escritorio)
            print("✅ Copied to the clipboard and temporary file deleted.")
        except Exception as e:
            print(f"❌ Error copying: {e}")

    else:
        print("‼️ Error: The 4th argument must be 'C' or 'G'.")

if __name__ == "__main__":
    generar_qr()
