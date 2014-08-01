#!/bin/bash/
debmirror --host=http.us.debian.org --root=debian --cleanup --nosource --progress --ignore-release-gpg --arch=i386 --dist=stable --method=http --section=main,contrib,non-free /home/usuario/control/debian
