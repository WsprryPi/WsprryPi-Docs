# GitHub Update Polling

This page explains GitHub polling, version metadata, comparison flow, and branch-aware release policy. For notification behavior and persisted dismissal state, see [Update Prompts and Stored State](prompts_and_state.md).

GitHub/app update checks are driven by:

```js
const GITHUB_UPDATE_POLL_INTERVAL_MS = 60 * 60 * 1000;

initGithubUpdatePolling();
updateWsprryPiVersion();
checkForWsprryPiUpdate();
buildWsprryPiUpdateResult();
```

`initGithubUpdatePolling()` starts one hourly interval and prevents duplicates with:

```js
githubUpdatePollTimer !== null
```

`pageLoaded()` calls `updateWsprryPiVersion()` immediately, so the first check happens on load. The hourly timer repeats it afterward.

`updateWsprryPiVersion()` fetches `/version`, updates the footer `#versionText`, calls `maybePromptForUiRefresh(response)`, then calls `checkForWsprryPiUpdate(response)`.

Backend `/version` includes structured metadata:

```json
{
  "wspr_version": "... display text ...",
  "ui_version": "...",
  "wspr_version_raw": "...",
  "wspr_version_parsed": {},
  "wspr_branch": "...",
  "wspr_branch_state": "branch|detached|unknown",
  "wspr_display_branch": "...",
  "wspr_exe_version": "...",
  "wspr_commit": "...",
  "wspr_build_dirty": false,
  "wspr_build_dirty_state": {}
}
```

`parseWsprryPiVersionResponse()` prefers structured fields. Display-string parsing is a legacy fallback.

## GitHub Comparison Flow

GitHub API base:

```js
const UPDATE_CHECK_API_BASE = "https://api.github.com/repos/WsprryPi/WsprryPi";
```

Requests use:

```js
fetchGithubJson(url, { cache: "no-store" })
```

with:

```text
Accept: application/vnd.github+json
```

Core functions:

```js
fetchGithubReleases()
summarizeSemanticReleases()
selectGithubUpdateBranch()
lookupGithubBranch()
compareGithubCommits()
buildSemanticVersionUpdateResult()
buildCommitBasedWsprryPiUpdateResult()
```

Successful results are cached for one hour:

```js
UPDATE_CHECK_CACHE_TTL_MS = 60 * 60 * 1000;
```

Failure results are rate-limited for five minutes:

```js
UPDATE_CHECK_FAILURE_RATE_LIMIT_MS = 5 * 60 * 1000;
```

Manual `Check now` uses:

```js
forceUpdateCheckNow()
checkForWsprryPiUpdate(response, { bypassCache: true })
```

This bypasses both success cache and failure rate limit, then writes fresh cache state.

## Update Policy

```js
branchAllowsCommitUpdate(branch)
```

returns `false` only for `main`.

### Main Branch Behavior

* `main` targets upstream `main`
* Commit differences alone do not create an update notification
* `main` requires a newer tagged semantic GitHub release
* If upstream `main` is ahead but no newer release exists, status becomes:

```text
main_commit_diff_without_release
```

### Non-Main Branch Behavior

* `devel` targets upstream `devel`
* If local `devel` commit is reachable from upstream `main`, it targets `main`
* If upstream `devel` is missing, `main` is selected only after proving that it contains the running commit
* Other branches target the same-name upstream branch
* If the same-name upstream branch is missing, `devel` is selected only after proving that it contains the running commit
* If containment cannot be established, the check fails with `unsafe_target` instead of claiming an update
* Non-main branches allow commit-based update notifications

### Detached or Unknown Branch Behavior

* `selectDetachedOrUnknownUpdateBranch()` probes `main`, then `devel`
* It only selects a target if the local SHA is reachable from that upstream branch
* Otherwise it fails with:

```text
detached_target_unknown
```

### SHA Comparison Behavior

* `updateCheckShaMatches()` accepts full SHA equality or short SHA prefix match
* GitHub compare direction is:

```text
currentSha...targetHeadSha
```

* GitHub compare status `ahead` means the target branch contains the installed commit and additional newer commits, so an update is available
* `identical` means no update
* `behind` is reported as local-ahead/no-update
* `diverged` is a distinct no-update state because neither history is a safe upgrade path from the other
* An unavailable comparison, including GitHub HTTP 404, fails with `comparison_unavailable`; differing SHAs alone never establish an update
* Empty commits on a tracked non-main upstream branch are detected because GitHub reports the branch as `ahead`

### Tagged Release Behavior

* Stable local semantic versions compare only against the latest stable GitHub release
* Stable builds do not upgrade to prereleases
* Prerelease builds first compare against newer stable releases
* Then they compare against newer prereleases in the same channel, for example `rc` to newer `rc`
* Different prerelease channels are ignored by default
* Versions with build metadata normally fall back to commit comparison, except where `main` release-only policy applies

### Commit-Based Prerelease Behavior

* Non-main prerelease or build-metadata versions can surface branch/SHA updates
* The UI labels these results `Newer branch build available`, not as a newer released version
* The modal treats these as branch/channel updates, not exact tagged release updates, and identifies the target branch and commit
* The primary action button is hidden unless the result is a tagged semantic release update
