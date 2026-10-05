(faq-and-known-errors)=
# FAQ and Known Errors

This section collects common installation issues, compatibility notes, and hardware questions that come up repeatedly when running WsprryPi.

```{toctree}
:maxdepth: 1
:hidden:

GPIO Band Capabilities and Signal Quality <why_12m_looks_noisy>
Low-Pass Filter Requirements <lowpass-filter-justification>
```

- {ref}`Install error: bash syntax error near unexpected token (less-than) <install-error-bash-line-1-syntax-error-near-unexpected-token->`
- {ref}`Install error: curl 404 (requested URL returned error 404) <or-curl-22-the-requested-url-returned-error-404>`
- {ref}`WSPR-15 Support <wspr-15-support>`
- {ref}`GPIO Band Capabilities and Signal Quality <why_12m_looks_noisy>`
- {ref}`Low Pass Filter Requirements <lpf-justification>`

(install-error-bash-line-1-syntax-error-near-unexpected-token-)=
## Install Error ``bash: line 1: syntax error near unexpected token `<'``

(or-curl-22-the-requested-url-returned-error-404)=
## or `curl: (22) The requested URL returned error: 404`

If this happens, the DNS redirect (vanity URL) I use to make the install command shorter and easier to type may have broken.

**Explanation:** The installation command line uses an application called `curl` to download the target URL. The pipe operator (`|`) redirects that to whatever follows, in this case `sudo` and `bash`, so the script runs as soon as it downloads. If the redirect breaks, a normal HTML page may be returned instead of the shell script. Bash does not interpret HTML, so it stops immediately when it sees the leading `<`.

You may use the following longer form instead:

```bash
curl -L https://raw.githubusercontent.com/WsprryPi/WsprryPi/main/scripts/install.sh | sudo bash
```

(wspr-15-support)=
## WSPR-15 Support

I have removed WSPR-15 support in version 2.x.

WSPR-15 ("Weak Signal Propagation Reporter" with a 15-minute transmit/receive cycle) was introduced in January 2013 as part of the experimental WSPR-X software suite. By stretching the standard 2-minute cycle to 15 minutes, WSPR-15 lowers the symbol rate to about 0.183 Hz tone spacing, compared with 1.4648 Hz in standard WSPR, narrowing the occupied bandwidth to about 0.7 Hz. This yields roughly a 9 dB sensitivity improvement and made it attractive for very low-frequency and medium-frequency beacon work where Doppler shifts are minimal.

Sources:

- [https://de.wikipedia.org/wiki/Weak_Signal_Propagation_Reporter](https://de.wikipedia.org/wiki/Weak_Signal_Propagation_Reporter)
- [https://www.scribd.com/document/358388839/WSPR-X-Users-Guide](https://www.scribd.com/document/358388839/WSPR-X-Users-Guide_)

Current Support and Viability

- Software support is scarce. The only decoders that handle WSPR-15 are the legacy WSPRX program and the now-unmaintained WSPR-X client. Mainstream WSJT-X releases implement only the standard 2-minute WSPR protocol.
- Network integration is limited. The central WSPRnet database and most reporting services expect the standard WSPR2 format, so WSPR-15 uploads and mapping generally require unofficial workarounds.
- Modern alternatives outperform it. Within WSJT-X, the FST4W family achieves similar or better sensitivity than standard WSPR while remaining actively developed and widely used on LF and MF bands.

Bottom line: WSPR-15 still works in legacy workflows, but it remains a niche protocol with minimal software and network support. For new weak-signal experiments, FST4W or standard 2-minute WSPR are the more practical choices.

(why-12m-looks-noisy-on-the-raspberry-pi)=
## GPIO Band Capabilities and Signal Quality

> This section has been moved to a separate document for clarity.
> See: [GPIO Band Capabilities and Signal Quality](why_12m_looks_noisy.md)

(lpf-justification)=
## Low Pass Filter Requirements

> This section has been moved to a separate document for clarity.
> See: [Low Pass Filter Requirements](lowpass-filter-justification.md)
