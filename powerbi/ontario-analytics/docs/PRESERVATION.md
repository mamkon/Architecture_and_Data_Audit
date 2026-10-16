# Preservation and public-copy policy

The original `outputs/ontario-automated/` and `outputs/ontario-powerbi/` working folders were not changed by this organization task. A separate private ZIP records all their files with relative paths and SHA-256 checksums, including the two workbook copies, all CSV extracts, original three preview images, reports, browser companions, model files, Power Query, DAX, theme and validation documentation.

The public folder is a separate presentation copy. Both PBIP entry points, both report directories, all three pages, all 26 visual definitions per report and the semantic model structure are retained. The only semantic-model change is replacing the machine-specific SourceFolder value with a portable example path. It does not replace the analytical model with a simplified demo model. The browser demonstration is separate and cannot overwrite the model's actual source inputs.

Real source inputs and derived observations are intentionally absent from the public copy. Synthetic demonstrations replace only public presentation assets; the original real-data images and HTML remain in the private archive. The original validation records are retained with a current validation note explaining their scope.

Keep the private ZIP and its checksum manifest together in a backed-up location. Before restoring, verify checksums, extract the entire directory structure, configure local source paths and open a copy. Do not upload the private archive or checksum manifest to a public repository. Cached Desktop state, if present in an original, belongs only in the private archive.
