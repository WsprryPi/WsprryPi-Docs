# Complete Default INI File

This is the complete default configuration maintained by this documentation repository. An installed file may differ after setup or later configuration changes.

{download}`Download default_wsprrypi.ini <default_wsprrypi.ini>`

```{literalinclude} default_wsprrypi.ini
:language: ini
```

## Optional development listener

The standard download above does not include development WTP sections. For a
managed Pi endpoint, add this section to the active INI:

```ini
[WTP Server]
Enabled = true
Port = 31417
Interface = auto
```

These are the listener defaults, not permission to transmit. Local Enable off
makes safe, idle output available for a remote claim; local Enable on reserves
it. Review the [listener and ownership reference](runtime.md#wtp-server)
before changing these controls. For an outbound profile, use the
[WTP endpoint reference](transmitter_backends.md#pico-wtp). Independent Fleet
assignments are saved outside the INI.
