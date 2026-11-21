# CW and Band GPIO Settings

INI blocks on this page show the one-time import representation. After migration, use Setup or the [local settings command](../../Command_Line_Operations/saved_settings.md); see [Saved Settings and INI Migration](../ini_configuration.md).

Use these sections for QRSS, FSKCW, and DFCW message construction, timing, frequency, fades, scheduling, and per-band switching outputs. For browser configuration, see [Configure CW Modes](../../User_Interface/Setup/Signal_Setup/cw.md). Related references include [CW Mode Options](../../Command_Line_Operations/cw_modes.md), [Configuration Troubleshooting](../configuration_troubleshooting.md), and [Configure Device I/O](../../User_Interface/Setup/Pi_IO/index.md).

(cw-section)=
## CW

The `[CW]` section preserves one shared dot duration, the separate QRSS/FSKCW and DFCW spacing triplets, frequency-shift behavior, fade controls, and scheduled repeat values. Numeric-looking content such as `73` remains a text message.

```{literalinclude} default_wsprrypi.ini
:language: ini
:start-at: [CW]
:end-before: [Band GPIO]
```

(band-gpio-section)=
## Band GPIO

The `[Band GPIO]` section assigns optional BCM GPIO outputs and polarity independently for every listed band. A blank band assignment disables switching for that band. An enabled assignment cannot use the GPIO backend's selected RF output pin. Multiple enabled bands may share one GPIO only when their polarity matches.

```{literalinclude} default_wsprrypi.ini
:language: ini
:start-at: [Band GPIO]
```
