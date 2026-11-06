# About WSPR

WSPR stands for Weak Signal Propagation Reporter. It’s a digital protocol that amateur radio operators use to study how low-power signals travel over long distances, even when propagation conditions are poor.

WSPR sends information as a sequence of tones in short, controlled bursts. Receiving software can recover the message from noise even when the signal is too weak to hear.

Each WSPR transmission carries one message frame. WsprryPi supports three
message types:

- **Type 1** carries a standard callsign, a four-character Maidenhead locator,
  and reported power.
- **Type 2** carries a supported compound callsign and reported power, without
  a locator.
- **Type 3** carries a callsign hash, a six-character locator, and reported power.
  The hash alone cannot reconstruct the callsign; the receiver needs matching
  callsign context from another decoded message.

WsprryPi can pair Type 1 or Type 2 with Type 3 in separate transmission windows
to send station identity and the extended locator. A message type is a frame
format; a paired plan schedules two frames. See
[WSPR transmission planning](../User_Interface/Setup/Signal_Setup/wspr.md#wspr-transmission-type-selection-examples)
for WsprryPi's choices and the
[WSJT-X protocol reference](https://wsjtx.github.io/wsjtx/guide-full.html)
for the message formats.

WSPR is transmitted on a schedule, allowing multiple stations to share a single frequency. This makes WSPR suitable for various applications, including monitoring and analyzing radio propagation conditions, testing equipment and antennas, and conducting experiments in low-power, long-range communication.

WSPR can operate at very low signal-to-noise ratios. This makes it useful for studying paths that ordinary listening may miss.

WSPR is the software that implements MEPT-JT, which started life in 2008 as a suggestion by Murray ZL1BPU. Joe K1JT took up the challenge, designed the software, and added many improvements. 'MEPT-JT' is derived from 'MEPT' (Manned Experimental Propagation Transmission), a generic term for a range of low-powered techniques, and 'JT' is Joe Taylor's initials. It is one of a general family of D-MEPT (digital MEPT) modes.

The idea was to take a minimal message, code it as tightly as possible, add forward error correction, and then combine this with a known pseudo-random sequence to generate a two-minute message to be sent using 4-FSK modulation and a low baud rate. Joe estimated that the system's theoretical sensitivity would be -30dB S/N.

Transmissions carry a station's callsign, [Maidenhead grid locator](https://en.wikipedia.org/wiki/Maidenhead\_Locator\_System), and transmitter power indicated in dBm. Receiving stations can decode signals with a signal-to-noise ratio [as low as -28 dB in a 2500 Hz bandwidth](https://physics.princeton.edu//pulsar/K1JT/wsprrypi.html). Stations with internet access can automatically upload their reception reports to a central database called [WSPRnet](https://wsprnet.org), which includes a mapping facility.

The basic specifications of the MEPT\_JT mode are as follows:

- Transmitted message: callsign + 4-character-locator + dBm Example: "K1JT FN20 30" (in the case of WSPR1)
- Message length after lossless compression: 28 bits for callsign, 15 for locator, 7 for power level ==\> 50 bits total.
- Forward error correction (FEC): long-constraint convolutional code, K=32, r=1/2.
- Number of channel symbols: nsym = (50+K-1)\*2 = 162.
- Keying rate: 12000/8192 = 1.46 baud.
- Modulation: continuous phase 4-FSK. Tone separation: 1.46 Hz.
- Synchronization: 162-bit pseudo-random sync vector.
- Data structure: each channel symbol conveys one sync bit and one data bit.
- Duration of transmission: 162\*8192/12000 = 110.6 s.
- Transmissions start two seconds into an even UTC minute: i.e., at hh:00:02, hh:02:02, ...
- Occupied bandwidth: about 6 Hz
- Minimum S/N for reception: around -27 dB on the WSJT scale (2500 Hz reference bandwidth).

Like JT65, MEPT\_JT includes efficient data compression and strong forward error correction. Received messages are nearly always the same as the transmitted message or are left blank.
