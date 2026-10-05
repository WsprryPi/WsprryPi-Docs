# Ninja Settings

The following settings are in the INI file however are not surfaced in the user interface.  Changing these should be considered experimental, and may render the application non-functional.  For the most part they are used in development and testing.  Use at your own risk.

```ini
[Meta]
debug_logging = False

[Operation]
; Web Port:
; Port used for REST interface.
Web Port = 31415

; Socket Port:
; Port used for WebSocket interface.
Socket Port = 31416


[Experimental]
; Advanced CLI/INI-only frequency policy. These settings do not grant legal
; authority to transmit and are not shown in the Web UI.
Allow Unqualified Frequency = false
; Frequencies outside recognized amateur bands require both settings to be true.
Allow Non-Amateur Frequency = false


[GPIO]
; Transmit Pin:
; BCM GPIO used for RF output when Transmit Backend = gpio.
; GPCLK0 is supported on BCM GPIO 4 or 20.
; The selected pin is reserved from enabled Band GPIO, LED, shutdown, and amp roles,
; even when Operation.Transmit is false.
; Ignored by the Si5351 backend.
Transmit Pin = 4


[Si5351]
; TX Output:
; Si5351 clock output used for transmit RF.
; Valid values:
;   CLK0
;   CLK1
;   CLK2
; Unused outputs are held in a safe non-transmitting state by WsprryPi.
; The internal parked PLL is a synthesis state, not an emitted parked RF output.
; This setting is configurable in INI and CLI; it is not exposed in the web UI.
TX Output = CLK0


[CW]
; Fade Shape:
; Envelope fade shape for QRSS, FSKCW, and DFCW events.
; Valid values: none, linear, raised_cosine.
Fade Shape = raised_cosine

; Fade In Ms:
; RF envelope fade-in duration in milliseconds.
Fade In Ms = 20

; Fade Out Ms:
; RF envelope fade-out duration in milliseconds.
Fade Out Ms = 20

; Fade Slice Ms:
; Advanced envelope approximation control for QRSS, FSKCW, and DFCW fades.
; Smaller values produce smoother duty-gated fades at higher switching cost.
; This does not change Fade In Ms or Fade Out Ms duration.
Fade Slice Ms = 2
```

`Allow Unqualified Frequency` permits a backend, hardware profile, band, and
mode combination whose recorded state is **Untested** or **Unqualified**. It
cannot enable an **Unavailable** output that the selected backend cannot safely
construct. `Allow Non-Amateur Frequency` additionally permits a frequency
outside WsprryPi's recognized US and international amateur-band ranges, but
only when both settings are `true`.

These settings do not grant permission to transmit. The operator remains
responsible for authorization, RF-path safety, filtering, and compliance with
applicable rules.
