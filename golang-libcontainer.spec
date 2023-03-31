%define debug_package   %{nil}
%define import_path     github.com/docker/libcontainer
%define gosrc %{go_dir}/src/%{import_path}

Name:           golang-libcontainer
Version:        2.2.1
Release:        3
Summary:        Docker libcontainer library
License:        Apache 2.0
URL:            https://%{import_path}
Source0:        https://%{import_path}/archive/v%{version}.tar.gz
BuildRequires:  golang
Requires:       golang
Group:		Development/Other

Provides: golang(%{import_path}) = %{version}-%{release}
Provides: golang(%{import_path}/apparmor) = %{version}-%{release}
Provides: golang(%{import_path}/cgroups) = %{version}-%{release}
Provides: golang(%{import_path}/cgroups/fs) = %{version}-%{release}
Provides: golang(%{import_path}/cgroups/systemd) = %{version}-%{release}
Provides: golang(%{import_path}/configs) = %{version}-%{release}
Provides: golang(%{import_path}/configs/validate) = %{version}-%{release}
Provides: golang(%{import_path}/criurpc) = %{version}-%{release}
Provides: golang(%{import_path}/devices) = %{version}-%{release}
Provides: golang(%{import_path}/integration) = %{version}-%{release}
Provides: golang(%{import_path}/label) = %{version}-%{release}
Provides: golang(%{import_path}/netlink) = %{version}-%{release}
Provides: golang(%{import_path}/nsenter) = %{version}-%{release}
Provides: golang(%{import_path}/selinux) = %{version}-%{release}
Provides: golang(%{import_path}/stacktrace) = %{version}-%{release}
Provides: golang(%{import_path}/system) = %{version}-%{release}
Provides: golang(%{import_path}/user) = %{version}-%{release}
Provides: golang(%{import_path}/utils) = %{version}-%{release}
Provides: golang(%{import_path}/xattr) = %{version}-%{release}

BuildArch:	noarch

%description
Simple library that implements container support for Linux

%prep
%setup -n libcontainer-%{version}

%build
%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go" | egrep -v "./vendor/src") ; do
    echo "%%dir %%{gopath}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list
done
sort -u -o devel.file-list devel.file-list

%files -f devel.file-list
%doc LICENSE README.md
%doc sample_configs/*
