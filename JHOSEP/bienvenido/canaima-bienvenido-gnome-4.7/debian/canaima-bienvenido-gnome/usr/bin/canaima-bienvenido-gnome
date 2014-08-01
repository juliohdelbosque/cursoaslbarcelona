#!/bin/sh -e

case ${1} in
	auto)
		. ${HOME}/.config/canaima-bienvenido-gnome/gui.conf

		if [ ${MOSTRAR} -eq 1 ]; then
			python /usr/share/canaima-bienvenido-gnome/canaima-bienvenido.py
		fi
	;;

	start|*)
		python /usr/share/canaima-bienvenido-gnome/canaima-bienvenido.py
	;;
esac

exit 0
