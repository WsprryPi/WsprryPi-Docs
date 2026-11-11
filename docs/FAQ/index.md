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

WsprryPi supports the standard two-minute WSPR protocol. WSPR-15 is not supported.

(why-12m-looks-noisy-on-the-raspberry-pi)=
## GPIO Band Capabilities and Signal Quality

See: [GPIO Band Capabilities and Signal Quality](why_12m_looks_noisy.md)

(lpf-justification)=
## Low Pass Filter Requirements

See: [Low Pass Filter Requirements](lowpass-filter-justification.md)
