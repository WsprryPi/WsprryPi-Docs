# Complete Default INI File

This is the complete default configuration maintained by this documentation repository. An installed file may differ after setup or later configuration changes.

{download}`Download default_wsprrypi.ini <default_wsprrypi.ini>`

```{literalinclude} default_wsprrypi.ini
:language: ini
```

## Existing development settings

Do not add an inbound WTP listener or select `backend=wtp`. These execution paths are retired. Existing inactive sections can remain stored, but an unsupported active setting is rejected. See [configuration validation](runtime.md#retired-wtp-configuration).
