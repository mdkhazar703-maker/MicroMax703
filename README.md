# MacroMax703

A QMK-powered macro pad built around a Seeeduino XIAO, with a 3×3 switch matrix and two rotary encoders for volume and screen brightness. It also packs a hidden feature nobody outside this repo knows about yet.

<img width="569" height="409" alt="MacroMax703 assembled macro pad" src="https://github.com/user-attachments/assets/d4bc3f80-abf4-427e-9ad2-a4d565ee620f" />

## The Circuit Board

The heart of MacroMax703. This board is the platform that connects every part together into one seamless, clean-looking macro pad. At a glance it might look like a simple green rectangle, but it's actually packed with intricate wiring and several electronic components, forming a small, bustling network of data and electricity.
**[Click here for the KICanvas →](https://kicanvas.org/?repo=https%3A%2F%2Fgithub.com%2Fmdkhazar703-maker%2FMicroMax703%2Fblob%2Fmain%2Fpcb%2FMacroMax703_pcb.kicad_pro)**

<img width="697" height="350" alt="Close-up of MacroMax703 PCB tracing detail" src="https://github.com/user-attachments/assets/1175a00d-ecad-4119-8a96-bd9a9fdd52d1" />

*↑ The fine detailing that went into the routing.*

## The Case

To house this board properly, it needed a case worthy of it.

<a href="https://www.printables.com/model/1764776-macromax">
  <img width="663" height="343" alt="MacroMax703 case design" src="https://github.com/user-attachments/assets/5930fb0b-c5ab-42cf-8820-82fbe04ec72b" />
</a>

**[Click here for the case files on Printables →](https://www.printables.com/model/1764776-macromax)**

## The Firmware

Every piece of hardware needs a brain — ours runs on QMK Firmware.

<img width="907" height="464" alt="QMK firmware configuration for MacroMax703" src="https://github.com/user-attachments/assets/6bb1b602-57fa-47d9-9d4e-58e0fbf220ce" />

## For the Curious

**Hardware**
- MCU: Seeeduino XIAO (SAMD21)
- Keys: 9× mechanical switches in a 3×3 matrix, 1× 1N4148 diode per switch
- Encoders: 2× rotary encoders with integrated push-button switches (SW10, SW11)

**Software**
- KiCad — PCB design
- Onshape — Case design
- QMK Firmware — Macro pad firmware development

<details>
<summary>Psst — about that hidden feature</summary>

We're not saying what it does here. Build one, dig through the firmware, and find out for yourself.

</details>

## Want to Make Your Own MacroMax703?

1. Install KiCad: https://www.kicad.org/download/
2. Open the schematics and get familiar with the circuit
3. Route your own PCB traces
4. Order and assemble your board
5. Download QMK Firmware and program your own macro pad
