# Spots Card

The Spots card displays reception reports from WSPRnet. It refreshes the past 60 minutes of reports for your callsign every five minutes.

It defaults to the [downloader API](https://wspr.live/wspr_downloader.php), but if configured or if the initial pull fails, it falls back to the [ClickHouse URL](https://db1.wspr.live/).

![Download API Options](download_selector.png)
