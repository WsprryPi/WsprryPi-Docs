# UI Build Polling

This page explains installed UI identity, cache invalidation, polling, refresh comparison, dismissal, and convergence behavior. For the resulting refresh dialog and shared modal state, see [Update Prompts and Stored State](prompts_and_state.md).

## Installed UI identity

The installer publishes an immutable `ui-manifest.json` with normalized SHA-256 records for the packaged UI files. Runtime and backup paths are excluded. The UI-owned `/wsprrypi/ui-version.php` endpoint compares the installed files with that manifest and reports one of these states:

* `packaged`: every covered installed file matches the packaged manifest.
* `locally_modified`: the manifest is valid, but covered files were modified, added, or deleted.
* `unknown`: the installed state cannot be compared safely, such as when the old manifest is missing, malformed, unreadable, or uses an unsupported schema.

The endpoint also reports `packaged_ui_build_id`, `installed_ui_build_id`, and the modified, added, and missing file lists. It sends `Cache-Control: no-store`; it is not served through the running-service proxy.

Every rendered page receives:

```js
window.WSPRRYPI_INSTALLED_UI_BUILD_ID
```

from `header.php`. Static asset URLs use `wsprrypiAssetUrl()`, which appends:

```text
?v=<installed_ui_build_id>
```

This busts CSS, JavaScript, and font caches when installed UI content changes.

## Polling and comparison

Runtime polling is controlled by:

```js
const UI_BUILD_POLL_INTERVAL_MS = 60 * 1000;

initUiBuildChangePolling();
checkUiBuildVersion();
maybePromptForUiRefresh();
refreshUiForIdentity();
checkUiRefreshConvergence();
```

`initUiBuildChangePolling()` starts one interval every 60 seconds. It also binds `visibilitychange`; when the document becomes visible again, `checkUiBuildVersion()` runs immediately. `uiBuildPollTimer` prevents duplicate intervals.

`checkUiBuildVersion()` fetches `/wsprrypi/ui-version.php` through:

```js
getJsonWithEndpointFallback(UI_IDENTITY_ENDPOINT)
```

It calls `maybePromptForUiRefresh()` only when the response includes `installed_ui_build_id`. `uiBuildVersionCheckRunning` prevents overlapping checks.

`maybePromptForUiRefresh()` compares the identity embedded in the loaded page only with the current installed identity. It does not compare executable, service, application-version, or packaged-manifest version fields.

If the identities differ, it shows a modal titled:

```text
UI refresh required
```

Confirm calls `refreshUiForIdentity(installedBuildId)`, which reloads with:

```text
current-url?ui_refresh=<installed_ui_build_id>
```

using `window.location.replace()`.

Cancel or modal hidden suppresses repeat prompts for that installed identity during the current page lifetime with `dismissedUiRefreshBuildId`. This suppression is not persisted to `localStorage`.

A stable locally modified installation does not prompt merely because it differs from the packaged manifest: the loaded page and current installed tree have the same installed identity. A prompt occurs only if covered UI files change while that page is open.

If `showConfirmationDialog()` fails to show the modal, it returns `false`; `uiRefreshPromptActive` remains `false`, so the next poll retries. If `#confirmModal` is missing, the prompt is deferred and retried later.

## Refresh convergence

After **Refresh**, the requested identity remains in the `ui_refresh` query parameter until the newly loaded page proves it has that identity. On success, the browser removes the parameter.

If the page still has a different identity, WsprryPi stops prompting and displays a persistent consistency diagnostic. This prevents a refresh loop during an incomplete or continuously changing deployment. Wait for the installation to finish, then reload once.
