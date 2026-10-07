Name:           ootty
Version:        0.1.0
Release:        1%{?dist}
Summary:        TTY capability inspection, pseudo-terminal allocation, and raw mode controller.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ootty
Source0:        ootty-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ootty is a sovereign, capability-bounded TERMINAL DETECTOR written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ootty
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ootty-uninstall

%files
/usr/bin/ootty
/usr/bin/ootty-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
