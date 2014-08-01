#!/bin/bash
lb config --architecture=i386 --linux-flavours=686-pae 486 --distribution=stable --mode=debian --apt=aptitude --apt-recommends=false --apt-secure=false --boot
loader=syslinux --bootstrap=debootstrap --binary-images=iso --archive-areas=main contrib non-free --mirror-bootstrap=http://172.17.1.116/debian --mirror-chroo
t=http://172.17.1.116/debian --mirror-chroot-security=none --mirror-chroot-backports=none --mirror-binary=http://172.17.1.116/debian --mirror-binary-security=
none --mirror-binary-backports=none --mirror-debian-installer=http://172.17.1.116/debian --security=false --backports=false --source=false --iso-volume=cursoa
sl --iso-publisher=IvanDelgado --iso-application=canaima-cursoasl --debian-installer=true --win32-loader=false --memtest=none --bootappend-live=boot=live live
-config live-config.timezone=America/Caracas live-config.locales=es_VE.UTF-8 live-config.hostname=canaima-cursoasl live-config.username=usuario live-config.us
er-fullname=usuario live-config.keyboard-layouts=latam live-config.keyboard-model=pc105 live-config.hooks=medium quiet splash vga=791 --parent-mirror-bootstra
p=http://172.17.1.116/debian --parent-distribution=stable --parent-archive-areas=main contrib non-free --parent-debian-installer-distribution=stable --parent-
mirror-debian-installer=http://172.17.1.116/debian --parent-mirror-debian-installer=http://172.17.1.116/debian --parent-mirror-chroot=http://172.17.1.116/debi
an --parent-mirror-chroot-security=none --parent-mirror-chroot-updates=none --parent-mirror-chroot-backports=none --parent-mirror-binary=http://172.17.1.116/d
ebian --parent-mirror-binary-security=none --parent-mirror-binary-updates=none --parent-mirror-binary-backports=none --mirror-chroot-updates=none --mirror-bin
ary-updates=none --updates=false --apt-indices=none --cache-indices=false --apt-source-archives=false --system=live --firmware-binary=false --firmware-chroot=
false
