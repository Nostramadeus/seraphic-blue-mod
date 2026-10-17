# Release update checklist

- Reproduce one reported bug with sanitized input. Keep raw user data private.
- Patch only the affected source; keep upstream notices. Run its focused regression plus affected installer/runtime checks.
- Update test tag and CHANGELOG. Preserve originals and saves; never publish the private project history.
- Regenerate only explicitly allowlisted patches/runtimes/source/notices. Keep binary behavior changes separate from documentation-only packaging.
- Update exact dependency source archives/recipes if a binary dependency changes. Keep source downloads available beside matching binaries.
- Verify wrapper/runtime/payload hashes, new-copy/save safety, archive paths, notices, fixed-neutral ZIP metadata and privacy. Distinguish legitimate third-party authors from private project data.
- Render changed HTML guides headlessly/muted at desktop/mobile widths and inspect screenshots.
- Review exact artifact names, sizes, hashes, source access and remaining limits. The owner explicitly approves remote commit/push/release actions.
- Publish the reviewed test assets and SHA256SUMS; keep the previous release for rollback. No automated publishing or CI is enabled by this repository.
