%define debug_package   %{nil}
%define import_path     github.com/docker/libcontainer
%define gosrc %{go_dir}/src/pkg/%{import_path}

Name:           golang-libcontainer
Version:        1.2.0
Release:        4
Summary:        Docker libcontainer library
License:        Apache 2.0
URL:            https://%{import_path}
Source0:        https://%{import_path}/archive/v%{version}.tar.gz
BuildRequires:  golang
Requires:       golang
Group:		Development/Other
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/apparmor) = %{version}-%{release}
Provides:       golang(%{import_path}/cgroups) = %{version}-%{release}
Provides:       golang(%{import_path}/cgroups/fs) = %{version}-%{release}
Provides:       golang(%{import_path}/cgroups/systemd) = %{version}-%{release}
Provides:       golang(%{import_path}/console) = %{version}-%{release}
Provides:       golang(%{import_path}/devices) = %{version}-%{release}
Provides:       golang(%{import_path}/label) = %{version}-%{release}
Provides:       golang(%{import_path}/mount) = %{version}-%{release}
Provides:       golang(%{import_path}/mount/nodes) = %{version}-%{release}
Provides:       golang(%{import_path}/namespaces) = %{version}-%{release}
Provides:       golang(%{import_path}/namespaces/nsenter) = %{version}-%{release}
Provides:       golang(%{import_path}/netlink) = %{version}-%{release}
Provides:       golang(%{import_path}/network) = %{version}-%{release}
Provides:       golang(%{import_path}/nsinit) = %{version}-%{release}
Provides:       golang(%{import_path}/security/capbilities) = %{version}-%{release}
Provides:       golang(%{import_path}/security/restrict) = %{version}-%{release}
Provides:       golang(%{import_path}/selinux) = %{version}-%{release}
Provides:       golang(%{import_path}/syncpipe) = %{version}-%{release}
Provides:       golang(%{import_path}/system) = %{version}-%{release}
Provides:       golang(%{import_path}/user) = %{version}-%{release}
Provides:       golang(%{import_path}/utils) = %{version}-%{release}
BuildArch:	noarch

%description
Simple library that implements container support for Linux

%prep
%setup -n libcontainer-%{version}

%build

%install
for d in . apparmor cgroups cgroups/fs cgroups/systemd console devices label mount mount/nodes namespaces namespaces/nsenter netlink network nsinit security/capabilities security/restrict selinux system syncpipe utils user; do
    install -d -p %{buildroot}/%{gosrc}/$d
    cp -av $d/*.go %{buildroot}/%{gosrc}/$d
done

%files
%doc LICENSE README.md
%dir %attr(755,root,root) %{gosrc}
%dir %attr(755,root,root) %{gosrc}/apparmor
%dir %attr(755,root,root) %{gosrc}/cgroups
%dir %attr(755,root,root) %{gosrc}/cgroups/fs
%dir %attr(755,root,root) %{gosrc}/cgroups/systemd
%dir %attr(755,root,root) %{gosrc}/console
%dir %attr(755,root,root) %{gosrc}/devices
%dir %attr(755,root,root) %{gosrc}/label
%dir %attr(755,root,root) %{gosrc}/mount
%dir %attr(755,root,root) %{gosrc}/mount/nodes
%dir %attr(755,root,root) %{gosrc}/namespaces
%dir %attr(755,root,root) %{gosrc}/namespaces/nsenter
%dir %attr(755,root,root) %{gosrc}/netlink
%dir %attr(755,root,root) %{gosrc}/network
%dir %attr(755,root,root) %{gosrc}/nsinit
%dir %attr(755,root,root) %{gosrc}/security/
%dir %attr(755,root,root) %{gosrc}/security/capabilities
%dir %attr(755,root,root) %{gosrc}/security/restrict
%dir %attr(755,root,root) %{gosrc}/selinux
%dir %attr(755,root,root) %{gosrc}/utils
%dir %attr(755,root,root) %{gosrc}/syncpipe
%dir %attr(755,root,root) %{gosrc}/system
%dir %attr(755,root,root) %{gosrc}/user
%{gosrc}/*.go
%{gosrc}/cgroups/*.go
%{gosrc}/cgroups/fs/*.go
%{gosrc}/cgroups/systemd/*.go
%{gosrc}/devices/*.go
%{gosrc}/apparmor/*.go
%{gosrc}/console/*.go
%{gosrc}/label/*.go
%{gosrc}/mount/*.go
%{gosrc}/mount/nodes/*.go
%{gosrc}/namespaces/*.go
%{gosrc}/namespaces/nsenter/*.go
%{gosrc}/netlink/*.go
%{gosrc}/network/*.go
%{gosrc}/nsinit/*.go
%doc sample_configs/*
%{gosrc}/security/*/*.go
%{gosrc}/selinux/*.go
%{gosrc}/system/*.go
%{gosrc}/syncpipe/*.go
%{gosrc}/user/*.go
%{gosrc}/utils/*.go
