# Alert Button

Raspberry Pi alert button project for `ensignpi-347`.

## Connect to the Pi

```bash
ssh ensign@ensignpi-347.local
```

## Install GPIO Library

```bash
sudo apt-get install python3-rpi.gpio
```

## Run the Script

```bash
python3 alert_button.py
```

When the button connected to physical pin 7 is pressed, the script prints:

```text
Someone pressed the alert button!
```
