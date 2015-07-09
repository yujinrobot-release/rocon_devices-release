Name:           ros-indigo-rocon-devices
Version:        0.0.5
Release:        0%{?dist}
Summary:        ROS rocon_devices package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/rocon_devices
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-rocon-hue
Requires:       ros-indigo-rocon-iot-bridge
Requires:       ros-indigo-rocon-ninjablock-bridge
Requires:       ros-indigo-rocon-python-hue
Requires:       ros-indigo-rocon-rtsp-camera-relay
Requires:       ros-indigo-rocon-smartthings-bridge
BuildRequires:  ros-indigo-catkin

%description
rocon devices meta package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Jul 09 2015 DongWook Lee <dwlee@yujinrobot.com> - 0.0.5-0
- Autogenerated by Bloom

* Mon Jun 15 2015 DongWook Lee <dwlee@yujinrobot.com> - 0.0.4-0
- Autogenerated by Bloom

* Fri Jun 05 2015 DongWook Lee <dwlee@yujinrobot.com> - 0.0.3-0
- Autogenerated by Bloom

* Fri Jun 05 2015 DongWook Lee <dwlee@yujinrobot.com> - 0.0.2-0
- Autogenerated by Bloom

* Tue Jun 02 2015 DongWook Lee <dwlee@yujinrobot.com> - 0.0.1-0
- Autogenerated by Bloom

