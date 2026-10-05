# User Interface

The web interface is the primary day-to-day control surface for WsprryPi. It provides configuration, status, logs, and recent spots in one responsive layout.

```{toctree}
:maxdepth: 1
:hidden:

Operate Transmissions <Operations/index>
Setup Overview <Setup/index>
Configure WSPR and CW <Setup/Signal_Setup/index>
Configure Transmitter <Setup/Transmitter/index>
Configure Raspberry Pi I/O <Setup/Pi_IO/index>
View Logs <Logs/index>
View Reception Reports <Spots/index>
Maintenance <Maintenance/index>
```

![WsprryPi UI](WsprryPi_UI.png)

Use the web UI in this order:

- Confirm the application is connected to the backend via the header indicators.
- Review or change configuration on the Setup page.
- Check Logs if the daemon does not behave as expected.
- Review recent reception reports on the Spots page.
- Monitor typical operations from the Operation page.

## Navbar

The navbar is the blue bar pinned to the top of the page.

### Transmission Indicator

![Transmission Indicator](Transmission_Indicator.png)

The antenna icon turns color depending on the status of the application:

- **Red:** Indicates the web page is disconnected from the application. The page has just opened and the Web Socket connection has not yet been negotiated. If it remains red, the daemon may not be running.
- **Orange:** Indicates the web page is negotiating the connection to the application.
- **Yellow/Gold:** Indicates the web page is connected to the application, but no transmission is in progress.
- **Green:** Indicates a transmission is in progress.

### Main Application Links

![WSPR Navbar Links](Navbar.png)

- **Operation:** The landing page and main view for active operations.
- **Setup:** Configure the transmission parameters and hardware interface.
- **Logs:** View the WsprryPi logs via a live interface to the Pi's `journald` daemon.
- **Spots:** Open reception-report resources for WSPR or QRSS.
- **Maintenance:** Configuration recovery, test-tone controls, update checks, and support-bundle creation.

#### Spots Menu

![The Spots menu with WSPR spots and QRSS Plus choices](Spots_Menu.png)

The **Spots** menu provides two reception-report destinations:

- **WSPR spots:** Opens the WsprryPi Spots page in the current browser tab. This page shows recent WSPR reception reports for your callsign.
- **QRSS Plus:** Opens the external [QRSS Plus](https://swharden.com/qrss/plus/) website in a new browser tab.

#### WsprryPi Links Dropdown

![WSPR Links](Links.png)

Three pages are available here:

- **Documentation:** This documentation, hosted at Read The Docs.
- **GitHub:** The main GitHub organization, containing all of the repositories supporting this project.
- **TAPR:** TAPR is a non-profit 501(c)(3) organization of amateur radio (“ham”) operators who are interested in advancing the state of the radio art.  TAPR offers pre-built Pi HATs for WsprryPi in their store, among other items.
- **WSPRNet Database:** The WSPRNet.or's database interface, where you may perform lookups on WSPR reports.

### Web Page Mode

![Web Page Mode](Mode_Switch.png)

WsprryPi supports a light and dark presentation mode in the web interface.

![Light/Dark Mode](Split_Screen.png)

## Card Header

Each page contains a card with a shared header area. The header is the shaded region at the top of the main content card.

### Card Info

Contextual information about the current page appears on the left side of the card header.

#### Server Control

On the top right side before the clock are server control icons:

![Server Control Buttons](Server_Control.png)

The icon on the left reboots the Raspberry Pi. When selected, the transmission LED, if configured, flashes twice and the system reboots.

The icon on the right powers off the Raspberry Pi. When selected, the transmission LED, if configured, flashes three times and the system shuts down immediately. In many setups you will need to remove and reapply power before the Pi can start again.

#### Clock

On the far right side of the card header is a clock displaying both local and UTC time:

![Local and UTC Clock](Clock.png)

## Application Pages / Card Bodies

The card body contains the page-specific controls and data. You may need to scroll to see all options. The layout is responsive and is intended to remain usable on both phones and desktop browsers.

Changes are saved as you make them.  The status of the save is shown in the card header.

![Save OK](Save_OK.png)

Any errors will be indicated there, with text directing you to the issue.

![Save Error](Save_Error.png)

Information related to each page follows.

<!-- if-wsprrypico -->
## Local control and remote ownership

In the development WTP workflow, this Pi can run its own schedule while
controlling other Pi or Pico outputs. Local **Enable**, this Pi's inbound WTP
listener, and each remote output's schedule are independent controls.

To reclaim a remotely owned Pi, open **that Pi's** web interface and select
**Enable**. Confirm removal of remote ownership and future schedule assignments.
For an armed or running remote job, choose:

- **End now** to stop the job immediately.
- **Let it finish** to allow the current job to finish before local output starts.
- **Cancel** to keep the existing ownership and saved Enable setting.

Both accepted choices prevent replacement remote jobs immediately. The central
controller cannot approve, delay, or veto this local action. Saved assignments
on the controller are removed when it next observes the takeover, including
when it was offline during the takeover.

With **Let it finish**, Enable is saved immediately, but effective local output
stays inhibited until the current job ends and output-off is confirmed. If
output state remains unknown, local transmission and new remote claims stay
inhibited. Review the status beside the control and use **Reconcile local
output** to request a local stop/reset; successful recovery requires confirmed
inactive output.

A direct HTTP configuration write explicitly setting `Operation.Transmit=true`,
or an external enabled INI transaction, is noninteractive and immediately
cancels remote work. It does not offer the browser's finish-current choice.
See [Fleet and listener setup](Setup/index.md#pi-and-pico-fleet-setup).
<!-- endif-wsprrypico -->
