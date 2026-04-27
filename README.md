# Local Terminal QR Code Generator

A QR code is essentially binary code expressed as an image, allowing you to generate them locally without relying on third-party services.

## 📝 How to Use

```bash
qr "[Link]" "[Color]" "[Background]" "[Output]"
```
- Color: name or HEX. **You don't need to use quotes unless you're using a hex code.**
- Output: S (save on the desktop) / C (copy to clipboard).

Example using defaults:
```bash
qr "[Link]" default
```
Default will take this values:
- Color: Black.
- Background: White.
- Output: Desktop.

---

## 📋 Dependencies

Press `Cmd + Space`, type **Terminal**, and open the application. Then, run the following commands:

```bash
xcode-select --install
```

Install the library required to generate the QR codes:

```bash
python3 -m pip install qrcode[pil]
```

**If it doesn't work, try:**
```bash
python3 -m ensurepip
python3 -m pip install qrcode[pil]
```


---

## 🖥️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/JordiBurguera/qr-generator
   ```

2. **Create a command for the script:**
   ```bash
   chmod +x ~/qr-generator/main.py
   sudo mv ~/qr-generator/main.py /usr/local/bin/qr #Sudo will ask for your password
   ```

You’re all set! Enjoy your free QR generator.

## 🛠️ Author
Jordi Burguera: Simple tools for a better workflow.

## ⭐ Show your support

If this tool helped you save time and stay away from ad-filled websites, please give this repository a star! It helps the project grow and makes me happy. I hope you didn't need AI to install the project in your mac 😊.

![Star](https://img.shields.io/github/stars/JordiBurguera/qr-generator?style=social)

