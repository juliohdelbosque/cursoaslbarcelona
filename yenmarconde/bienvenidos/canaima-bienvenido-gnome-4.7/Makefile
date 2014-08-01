# Makefile
#
# ==============================================================================
# PAQUETE: canaima-bienvenido-gnome
# ARCHIVO: Makefile
# DESCRIPCIÓN: intacion de las carpetas en su directo.
# COPYRIGHT:
#  (C) 2013 Sasha Veronica Solano Grosjean <sashasolano@gmail.com>
# LICENCIA: GPL3
# ==============================================================================
#
# Este programa es software libre. Puede redistribuirlo y/o modificarlo bajo los
# términos de la Licencia Pública General de GNU (versión 3).

HELL := sh -e

all: build

test:



	@echo -n "\n===== Comprobando posibles errores de sintaxis en los scripts de mantenedor =====\n\n"

	@for SCRIPT in $(SCRIPTS); \
	do \
		echo -n "$${SCRIPT}\n"; \
		bash -n $${SCRIPT}; \
	done

	@echo -n "\n=================================================================================\nHECHO!\n\n"

build:


	@echo "Nada para compilar!"
install:

	@mkdir -p $(DESTDIR)/usr/bin/
	@mkdir -p $(DESTDIR)/usr/share/canaima-bienvenido-gnome
	@mkdir -p $(DESTDIR)/etc/skel/.config/autostart
	@mkdir -p $(DESTDIR)/etc/skel/.config/canaima-bienvenido-gnome
	@mkdir -p $(DESTDIR)/usr/share/applications
	@cp -r gui/* $(DESTDIR)/usr/share/canaima-bienvenido-gnome
	@cp gui.conf $(DESTDIR)/etc/skel/.config/canaima-bienvenido-gnome/
	@cp canaima-bienvenido-gnome-auto.desktop $(DESTDIR)/etc/skel/.config/autostart
	@cp canaima-bienvenido-gnome.sh $(DESTDIR)/usr/bin/canaima-bienvenido-gnome
	@cp canaima-bienvenido-gnome.desktop $(DESTDIR)/usr/share/applications

uninstall:

	@rm -rf $(DESTDIR)/usr/share/canaima-bienvenido-gnome/
	@rm -rf $(DESTDIR)/usr/share/applications/canaima-bienvenido-gnome.desktop
	@rm -f $(DESTDIR)/etc/skel/.config/autostart/canaima-bienvenido-gnome-auto.desktop
	@rm -f $(DESTDIR)/usr/share/applications/canaima-bienvenido-gnome.desktop
	@rm -f $(DESTDIR)/usr/bin/canaima-bienvenido-gnome/canaima-bienvenido-gnome.sh
	@rm -f $(DESTDIR)/etc/skel/.config/autostart/canaima-bienvenido-gnome-auto.desktop

clean:

	@printf "Cleaning generated images [PNG] ["
	@for IMAGE in $(IMAGES); do \
		rm -rf gui/images/$${IMAGE}.png; \
		printf "."; \
	done

distclean:

reinstall: uninstall install
