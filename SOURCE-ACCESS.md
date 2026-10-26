# Corresponding source and library replacement

## Current and historical Players

[seraphic-blue-player-source-v0.3.6.zip](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.3.6/seraphic-blue-player-source-v0.3.6.zip) contains the current exact source and the historical sb4 tree:

| Binary | Matching source | Player revision |
| --- | --- | --- |
| v0.3.6 Windows/native Linux, 0.8.1.1-sb7 | Current export, Player/ | 77f13975ce79a592286a09eba271136741eb780e |
| v0.3.4 / Altered v0.3.5, 0.8.1.1-sb6 | [Earlier sb6 source](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.3.4/seraphic-blue-player-source-v0.3.4.zip), Player/ | eb421f52e66ccffd0871587a352037c4e31982f6 |
| v0.3.3 Windows/native Linux, 0.8.1.1-sb5 | [Earlier source asset](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.3.3/seraphic-blue-player-source-v0.3.3.zip), Player/ | 0cb855fe592235fdb083ac5c6ac7b946fccc0c87 |
| v0.3.1/v0.3.2 Windows, 0.8.1.1-sb4 | Current export, historical/sb4/Player/ | a13da2571b9e435462023ecf58085c77fc1cebcf |

The historical sb4 Windows Player SHA256 is `fc307c880021e02d9e72266776d8d73a309d86556b5e3b38eb3dfcf7ae735235`. SOURCES.json maps current binary hashes to source revisions. The export separately preserves historical build flags and recipes; sb7 is not substituted for earlier binaries' source.

The native Linux liblcf tree is **92c4450a1bc1acb58bd02bbb99b57e5036919cdf**. Windows liblcf is the separately packaged MSYS2 0.8.1-3 library; its exact source remains in the Windows dependency-source bundle below. Build recipes, the Windows PortAudio patch and timeline asset generators/tables are included; no Git history is exported. No byte-identical rebuild is claimed.

Linux dependencies are listed by exact binary/source version in **native-linux/BUNDLED-LIBS.tsv** and **DEPENDENCY-SOURCES.tsv**, with notices in **native-linux/licenses**. The Linux build uses SDL2 **2.30.9** and FluidLite commit **4a01cf1c67419e71da971d209f2855bbf4f3bab8**; downloaded archives are SHA256-recorded. The corresponding source export includes all 68 matching Linux dependency-source archives, SHA256 hashes, retrieval routes and notices. Its Player and native liblcf files reconstruct their exact committed Git trees; archive timestamps are neutral. System-provided glibc, libstdc++, zlib and display/audio driver libraries are not copied into the native package.

## Windows dependency sources

The [existing exact MSYS2 dependency-source bundle](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.2/seraphic-blue-dependency-sources-v0.1.0-test.2.zip) remains applicable to the unchanged Windows dependency versions. It contains 12 package-base source archives, including Windows liblcf and GCC runtime sources. **SOURCES.json** retains their exact versions, recipe/source hashes, archive sizes and URLs. Nine detached signature inputs were recipe-marked SKIP; no PGP signature-verification claim is made. Recipes were read, not executed here.

From v0.3.3, **libportaudio.dll** has a six-byte **Pa_Initialize** patch, supplied in the current source archive. [AryaNetwork's issue and diagnosis](https://github.com/Nostramadeus/seraphic-blue-mod/issues/1). All other matching Windows DLLs are unchanged.

## Library replacement and notices

Player is GPLv3; liblcf is MIT. Dependencies retain their own licenses and notices. Compatible dynamically linked libraries may be replaced subject to those licenses; the project adds no restrictive EULA. FluidLite is statically linked in the Linux Player; its source/build information accompanies the export. Sources accompany the release rather than relying only on an on-request promise. Keep matching binary/source assets and hashes together.

## Earlier source exports

The [test.8 source export](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.8/seraphic-blue-player-source-v0.1.0-test.8.zip) applies to the earlier test.8 Player, and includes its three-file change note. The [test.6 source export](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.6/seraphic-blue-player-source-v0.1.0-test.6.zip) remains archived. The old test.2 native Player used its own separate source; it is replaced in v0.3.3.
