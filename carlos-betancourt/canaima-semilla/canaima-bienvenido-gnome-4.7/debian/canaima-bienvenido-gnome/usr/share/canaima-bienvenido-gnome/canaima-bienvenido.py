#!/usr/bin/python
# -*- encoding: utf-8 -*-
from user import home
import gtk
import webkit
import os
import sys
import subprocess

sys.path.append('/usr/share/canaima-bienvenido-gnome')

class Config:
    """
    Config class
    """
   
    AUTOSTART_ENABLED = False
    NO_AUTOSTART_FILE = os.getenv('HOME') + '/.canaima-bienvenido-noautostart'
    DEV = os.path.dirname(os.path.realpath(__file__)) != '/usr/share/canaima-bienvenido-gnome'

    @staticmethod
    def getDesktopSession():
        """
        Get the Desktop session.. mate or gnome.
        """

        if subprocess.Popen(['pidof', 'mate-session'], stdout=subprocess.PIPE).communicate()[0]:
            return "mate"
        elif subprocess.Popen(['pidof', 'gnome-session'], stdout=subprocess.PIPE).communicate()[0]:
            return "shell"
        elif subprocess.Popen(['pidof', 'gnome-shell'], stdout=subprocess.PIPE).communicate()[0]:
            return "shell"
        elif subprocess.Popen(['pidof', 'x-session-manager'], stdout=subprocess.PIPE).communicate()[0]:
            if os.path.exists("/etc/alternatives/x-session-manager"):
                session = os.readlink("/etc/alternatives/x-session-manager").split("/")[3]
                if session == "gnome-session":
                    return "shell"
                elif session == "mate-session":
                    return "mate"
                else:
                    return "other"  # Running other desktop..
            else:
                return "other"  # dont have alternatives
        else:
            return "other"  # not exist x-session-manager process

    @staticmethod
    def load():
        """
        Load configuration
        """
        Config.AUTOSTART_ENABLED = Config.read_autostart_enabled()

    @staticmethod
    def save():
        """
        Save configuration
        """
        if Config.AUTOSTART_ENABLED:
            if os.path.exists(Config.NO_AUTOSTART_FILE):
                os.unlink(Config.NO_AUTOSTART_FILE)
        else:
            open(Config.NO_AUTOSTART_FILE, "w").close()

    @staticmethod
    def read_autostart_enabled():
        """
        Check autostart file
        """
        return not os.path.exists(Config.NO_AUTOSTART_FILE)


class BulletsBrowser(webkit.WebView):
    """
    Class for show Bullets
    """

    #Check env dev
    if Config.DEV:
        
        app_dir = os.getcwd() + "/"
	
        
    else:
        app_dir = "/usr/share/canaima-bienvenido-gnome/"

    #get Session gnome or mate
    RunningDesktop = Config.getDesktopSession()
    from data.shell.bullets_list import bullets_list
    bullet_close_number = 0
    bullet_close_active = False
    answer_active = False
    bullets_list = bullets_list
    bullets_dir = app_dir + 'data/' + RunningDesktop + '/'
   


    def __init__(self, start_page):
        """
        Widget for browsing the bullets.
        """
        webkit.WebView.__init__(self)
        self.get_property("settings").set_property(
            "enable-default-context-menu", False)
        self.connect('navigation-policy-decision-requested',
            self._on_navigate_decision)

        self.__build_page(0)  # First time


    def __build_page(self, bullet):
        """
        Builds the page
        """
        if bullet >= self.bullet_close_number or (bullet == len(self.bullets_list) - 1):  # Activate close button?
            self.bullet_close_active = True
        header = open(self.app_dir + 'data/header.html', 'r').read()
        header_content = header.replace('{{ variant }}', str(self.bullets_list[bullet]['variant']))
        header_content = header_content.replace('{{ animation }}', self.bullets_list[bullet]['animation']['class'])


        bullet_content = open(self.bullets_dir + str(self.bullets_list[bullet]['file']), 'r').read()
        bullet_content = bullet_content.replace('{{ prev_bullet_link }}',
                self.__build_prev_bullet_link(bullet))
        bullet_content = bullet_content.replace('{{ prev_bullet_link }}',
                self.__build_prev_bullet_link(bullet))
        bullet_content = bullet_content.replace('{{ next_bullet_link }}',
                self.__build_next_bullet_link(bullet))
        bullet_content = bullet_content.replace('{{ close_app_button }}',
                self.__build_close_button(bullet))
        bullet_content = bullet_content.replace('{{ autostart_checkbox }}',
                self.__build_show_next_startup())
        bullet_content = bullet_content.replace('{{ animation_class }}',
                self.bullets_list[bullet]['animation']['class'])
        footer_content = open(self.app_dir + 'data/footer.html', 'r').read()
        content = header_content + bullet_content + footer_content
        self.load_html_string(content, base_uri='file://' + self.app_dir)	

    def __build_prev_bullet_link(self, current_bullet):
	
        """
        Prev bullet link
        """
        if int(current_bullet) == 0:
            return '<div class="action bullet-navigation inactive" id="prev-bullet"><span>Anterior</span></div>'
        return '<div class="action bullet-navigation" id="prev-bullet"><a href="[bullet]?%s">Anterior</a></div>' % str(int(current_bullet) - 1)

    def __build_next_bullet_link(self, current_bullet):
        """
        Next bullet link
        """
        if int(current_bullet) == len(self.bullets_list) - 1:
            return '<div class="action bullet-navigation inactive" id="next-bullet"><span>Siguiente</span></div>'
        return '<div class="action bullet-navigation" id="next-bullet"><a href="[bullet]?%s">Siguiente</a></div>' % str(int(current_bullet) + 1)
        
       

    def __build_close_button(self, current_bullet):
        """
        Close bullet button
        """
        if current_bullet <= self.bullet_close_number and not \
                self.bullet_close_active:
            return '<div class="action inactive" id="close-app"><span>CERRAR</span></div>'
        return '<div class="action" id="close-app"><a href="#" onclick="finalize();">CERRAR</a></div>'

    def __build_show_next_startup(self):
        """
        Show next time
        """
        if Config.AUTOSTART_ENABLED:
            return '<input type="checkbox" checked="checked" id="chkAutoStart" />'
        return '<input type="checkbox" id="chkAutoStart" />'

    def _on_navigate_decision(self, view, frame, req, action, decision):
        """
        Decision navigate
        """
        import re
        parts = re.split("\[([a-z]+)\]", req.get_uri())[1:]

        if len(parts) == 2:
            if parts[0] == 'exec':
                # Launch external commands
                command = parts[1].split("%20")
                subprocess.Popen(command, bufsize=0, executable=None,
                        stdin=None, stdout=None, stderr=None, preexec_fn=None,
                        close_fds=False, shell=False, cwd=None, env=None,
                        universal_newlines=False, startupinfo=None,
                        creationflags=0)
                return True
            elif parts[0] == 'app':
                if parts[1] == 'portal':
                    os.system("sensible-browser http://canaima.softwarelibre.gob.ve/ -new-tab")
                    return True
                if parts[1] == 'wiki':
                    os.system("sensible-browser http://wiki.canaima.softwarelibre.gob.ve/wiki/Portada -new-tab")
                    return True
		if parts[1] == 'trac':
                    os.system("sensible-browser http://trac.canaima.softwarelibre.gob.ve/canaima/ -new-tab")
                    return True
                # Close app
                if parts[1] == 'finalize':
                    exit_app()
                    return True
                # Autostart
                elif parts[1] == "set-autostart-off":
                    os.system("mkdir -p " + home + "/.config/canaima-bienvenido-gnome/")
                    os.system("echo 'MOSTRAR=0' > " + home + "/.config/canaima-bienvenido-gnome/gui.conf")
                    return True
                elif parts[1] == "set-autostart-on":
                    os.system("mkdir -p " + home + "/.config/canaima-bienvenido-gnome/")
                    os.system("echo 'MOSTRAR=1' > " + home + "/.config/canaima-bienvenido-gnome/gui.conf")
                    return True
                elif parts[1] == "set-answer-active-on":
                    os.system("mkdir -p " + home + "/.config/canaima-bienvenido-gnome/")
                    os.system("echo 'MOSTRAR=0' > " + home + "/.config/canaima-bienvenido-gnome/gui.conf")
		    return True
                elif parts[1] == "set-answer-active-off":
                    os.system("mkdir -p " + home + "/.config/canaima-bienvenido-gnome/")
                    os.system("echo 'MOSTRAR=1' > " + home + "/.config/canaima-bienvenido-gnome/gui.conf")
		    return True
            # Bullets navigation
            elif parts[0] == 'bullet':
                params = parts[1].split("?", 1)
                self.__build_page(int(params[1]))  # Load page
                return True

            # Documentation
            elif parts[0] == 'doc':
                doc_page = parts[1]
                subprocess.Popen(["yelp", "file://" + doc_page])
                return True
        return False

def es_modo_live():
	'Verifica si el entorno de ejecucion es un LiveCD'
	return os.path.isdir("/lib/live/mount/medium")


def build_app_window(start_page):
    """
    Build application window.
    """
    logo='/usr/share/icons/Gnamon/places/scalable/canaima-logo.svg'
    sw = gtk.ScrolledWindow()
    bullet_browser = BulletsBrowser(start_page)
    sw.add(bullet_browser)
    Win = gtk.Window(gtk.WINDOW_TOPLEVEL)
    Win.set_icon_from_file(logo)
    Win.add(sw)
    Win.set_resizable(False)
    bullet_browser.set_size_request(740, 535)
    Win.set_default_size(740, 535)
    Win.set_title("Primeros pasos en Canaima")
    Win.set_position(gtk.WIN_POS_CENTER)
    #Win.set_deletable(True)
    Win.connect("destroy", gtk.main_quit)
    return Win


def exit_app():
    """
    Exit for this apps, saving the changes.
    """
    Config.save()
    sys.exit()

if __name__ == '__main__':
	Config.load()
	if '--autostart' in sys.argv and not Config.AUTOSTART_ENABLED:
		sys.exit()
	PATH = "file://" + BulletsBrowser.bullets_dir
	WIN = build_app_window(PATH + "/pages/bullets.html")
	WIN.show_all()
	if not es_modo_live():
		gtk.main()
		
