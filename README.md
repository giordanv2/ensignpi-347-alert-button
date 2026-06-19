# VitalLink Alert Button

Raspberry Pi alert button project for `ensignpi-347`. When the button is pressed,
the script prints an alert message and sends the same message to Telegram.

## Connect to the Pi

```bash
ssh ensign@ensignpi-347.local
```

## Install GPIO Library

```bash
sudo apt-get install python3-rpi.gpio
pip3 install requests
```

## Set Telegram Values

Replace the example values with your Telegram bot token and chat ID:

```bash
export TELEGRAM_BOT_TOKEN="BOT_TOKEN"
export TELEGRAM_CHAT_ID="CHAT_ID"
```

## Run the Script

```bash
python3 alert_button.py
```

When the button connected to physical pin 7 is pressed, the script prints:

```text
Someone pressed the alert button!
```

It also sends that same text through the Telegram API with:

```text
https://api.telegram.org/botBOT_TOKEN/sendMessage
```
