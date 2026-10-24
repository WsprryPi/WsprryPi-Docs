# Operations Card

The first page along the top of the Navbar is "Operations".  This page serves as the root page, and will be the most commonly monitored page during normal operations.

## Initial Operations

When you open the user interface at `http://{servername}.local`, the Apache configuration will redirect to `http://{servername}.local/wsprrypi/`.  This configuration is in place to avoid a conflict with any other websites you may have on your system.  If the installer detects another website in the root, the redirect will be disabled and you will need to append the `/wsprrypi/` manually.

If you are using a Raspberry Pi 5 or similar, you will see an indicator that the default "GPIO" transmitter is not supported.

![Initial Pi5 Screen](Pi5_GPIO.png)

When you select "Go to Setup" you will be directed to the `/wsprrypi/index.php?page=config&setup_tab=#transmitter-hardware-pane` tab, where the Si5351 will be automatically selected as the output path.  From here you may continue normally.

Within the Operations card are panels intended to be your quick reference to your current broadcast status, as well as a means to enable, disable, or stop transmissions.

![Initial Operations](Initial_Ops.png)

- **Current State:** Gives you a color and textual representation of what the Pi is doing right now. If you are configured with valid parameters and transmissions are enabled, you will see "Ready"

    ![Ready](ready.png)

- **Reboot Behavior:**

    ![Reboot Behavior](reboot_behavior.png)

  - *Disable transmission on (re)boot* means that any time the daemon is restarted (which includes a reboot), the transmission state will be disabled.  This is provided to protect against unexpected transmissions and potential damage to any PA finals.
  - *Follow the last transmission setting* takes the transmission control from the last known state, and follows accordingly on daemon restart,
  - *Restart transmission on (re)boot* will always enable transmissions, if the system can honor the configuration, when the daemon restarts.

  These choices control whether transmission is requested after startup. They do not bypass startup hardware safety. Before WsprryPi starts its web and socket services or creates a transmission schedule, it places the selected transmitter backend in a disabled state:

  - For the **Si5351** backend, all clock outputs are disabled.
  - For the **GPIO** backend, the DMA and clock path is stopped and the selected transmit GPIO is returned to an input state.

  If WsprryPi cannot confirm this safe state, it inhibits every transmission path for the lifetime of that daemon process. The web interface remains available for diagnosis, but changing the transmission switch, reloading the configuration, or changing modes does not clear the inhibition. Correct the hardware or configuration problem and restart the WsprryPi service so the startup safety check can run again.

  The startup check runs when the WsprryPi daemon starts; it cannot control transmitter hardware before the daemon is running. Stations that require guaranteed RF inhibition throughout power-up should also use an independent hardware inhibit or power-control circuit.

- **Transmission Controls:** This panel contains a switch to enable to disable transmissions as well as an emergency stop.

    ![Transmission Control](transmission_controls.png)

  - *Transmit Enabled* switch enables or disables transmission the transmission scheduler.  When enabled, the transmitter will operate on the schedule you have configured.  If you disable it, the configuration will save immediately, however any in-progress transmissions will finish.
  - *Stop transmission* button allows you to halt an ongoing transmission immediately, and it wil disable future transmissions.  It is only enabled during a transmission.

- **USB dial / Next USB dial:** The WSPR panel displays the current or next USB dial frequency. RF center = dial + 1500 Hz + optional random placement. The standard 20m dial is 14,095,600 Hz and its RF center without random placement is 14,097,100 Hz. **Random placement** shows the signed WSPR offset in Hz, separately from the fixed 1,500 Hz placement. CW labels identify **Carrier** for QRSS, **Space** for FSKCW and **Dot** for DFCW; **Positive shift** gives the mark or dash offset. These values describe requested frequencies, not measured RF.

    ![Frequency Panel](frequency.png)

    If a GPIO LPF pin is configured, that pin and the active high/low status will be displayed after the frequency:

    ![Frequency Panel GPIO Status](frequency_gpio.png)

- **Current Plan** or **Message Progression** will display the current (or next if in pause mode) plan to be transmitted.  For WSPR modes, it will show the type of WSPR frame being transmitted, as well as the callsign and locator.  For CW modes it will show the message and a cursor for the character being transmitted.

    ![Current Plan](current_plan.png)

  - *Type1Single* is a standard Type 1 WSPR frame.
  - *Type2Single* is a single Type 2 WSPR frame which sends a callsign with a prefix (`W0/`) or suffix (`/P`) as a hashed component.  The hash is not reversible.  Decoding relies on correlation over time by the receiver with previous full-message decodes from paired transmissions.
  - *Type1Type3Paired* is a paired frane transmission mode, alternating between Type 1 (shown as F1/2) and Type 3 (shown as F2/2) messages. This plan is to support paired transmission support for a long locator but a simple callsign.  This may be thought of as an automated means to assure the receiver can correlate all extended information.
  - *Type3Single* is a single Type 3 frame which sends a reversible callsign as well as a reversible 6-character maidenhead locator.
  - *Type2Type3Paired* is a paired frame transmission mode, alternating between Type 2 (shown as F1/2) and Type 3 (shown as F2/2) messages. This plan is to support paired transmission support for a complex or long callsign and a long locator. This may be thought of as an automated means to assure the receiver can correlate all extended information.
  - *Next Message At* is displayed when in one of the three CW modes, and the scheduler is waiting for a transmission window.  The time is displayed in the local time.
  - *Message Progression* is displayed in CW mode during a transmission. It will show a cursor on the current character.

    ![Message Progression](message_progression.png)
