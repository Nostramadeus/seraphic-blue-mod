# Corresponding source and library replacement

This test release provides the exact tracked Player/liblcf source export, the included Player working-tree changes, relative build recipes, source hashes and tested Windows cached flags/package versions. The clean liblcf checkout is the Linux source. Windows liblcf 0.8.1-3 has its separate exact MSYS2 source package, including its recipe.

The dependency-source bundle contains 12 exact MSYS2 package-base source archives: readline, termcap, fluidsynth, glib2, libiconv, gettext, lame, mpg123, libsndfile, graphite2, GCC and Windows liblcf. GCC covers libgcc/libgomp/libstdc++. SOURCES.json records immutable versions, upstream mirror routes, archive hashes/sizes, recipes, embedded source/patch checksums and release-asset access. All actual sources/patches were SHA256-checked. Nine detached .sig/.asc inputs are recipe-marked SKIP; no PGP signature-verification claim is made. Recipes were read, never executed during staging.

Sources are supplied with the binary release, not only on request. Keep the matching source assets and hashes alongside each release. Other Windows packages retain exact versions, upstream routes and full available notices; a generic upstream page is not claimed to prove byte-identical reproduction. Ubuntu's other runtime libraries are system-provided; the native package does not bundle them.

Libraries remain dynamically linked. You may replace compatible library files subject to their licenses; this project imposes no restrictive EULA on that replacement. Player remains GPLv3; liblcf is MIT; each dependency retains its own license and notices. Build scripts received syntax checks, not a new dependency rebuild or byte-identical reproduction proof. This is a source/notice packaging record, not a legal warranty.

Player source: https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.6/seraphic-blue-player-source-v0.1.0-test.6.zip

Dependency source: https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.2/seraphic-blue-dependency-sources-v0.1.0-test.2.zip

This test.6 Windows/Proton Player uses the new complete Player source bundle above. Its unchanged dependency source bundle remains the exact test.2 download. Native Linux test.2 is built from the separate test.2 source, not this new Windows build.
