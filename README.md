# About
Simple Steam profile checker bot for [Telegram messenger](https://telegram.org/) checks [Steam community](http://steamcommunity.com/) profiles including VAC, trade, etc. statuses.

This bot can also check users via third-party services:
 * [TEAM-FORTRESS.SU](https://check.team-fortress.su/) anti-scam service;
 * [STEAMREP.COM](https://steamrep.com/) anti-scam service.

# License
GNU General Public License version 3. You can find it here: [COPYING](COPYING). External libraries can use another licenses, compatible with GNU GPLv3.

# Requirements
 * Python 2.7 or Python 3.x;
 * python-pytelegrambotapi;
 * python-minidom;
 * python-requests.

# Running bot without installation
This bot can work without installation. Just clone repository, enter API tokens and run it:
 1. Clone this repository:
 ```
 git clone https://github.com/xvitaly/stmbot.git
 ```
 2. Get API tokens from [@BotFather](https://t.me/BotFather) and [TEAM-FORTRESS.SU forum](http://forum.team-fortress.su/threads/5115/), open `stmbot/settings.py` file in any text editor and set them.
 3. Run it using Python 3.x:
 ```
 cd stmbot
 /usr/bin/python3 stmbot/scripts/runbot.py
 ```
 4. Or run it using Python 2.7:
 ```
 cd stmbot
 /usr/bin/python2 stmbot/scripts/runbot.py
 ```

# Installing bot
You can also install bot:
 1. Clone this repository:
 ```
 git clone https://github.com/xvitaly/stmbot.git
 ```
 2. Get API tokens from [@BotFather](https://t.me/BotFather) and [TEAM-FORTRESS.SU forum](http://forum.team-fortress.su/threads/5115/), open `stmbot/settings.py` file in any text editor and set them.
 3. Install bot using Python 3:
 ```
 cd stmbot
 sudo /usr/bin/python3 setup.py install
 ```
 4. Install bot using Python 2.7:
 ```
 cd stmbot
 sudo /usr/bin/python2 setup.py install
 ```
 5. Run installed bot:
 ```bash
 /usr/bin/stmbot
 ```

# Building RPM package for Fedora
 1. Clone this repository:
 ```
 git clone https://github.com/xvitaly/stmbot.git
 ```
 2. Install mock, spectool and rpmbuild:
 ```
 sudo dnf install rpm-build rpmdevtools mock
 ```

 Add yourself to `mock` group (you must run this only for the first time after installing mock):
 ```
 sudo usermod -a -G mock $(whoami)
 ```
 You need to relogin to your system after doing this or run:
 ```
 newgrp mock
 ```
 3. Create RPM build base directories:
 ```
 rpmdev-setuptree
 ```
 4. Download sources:
 ```
 cd stmbot
 spectool -g -R stmbot.spec
 ```
 5. Generate SRPM package for mock:
 ```
 cd stmbot
 rpmbuild -bs stmbot.spec
 ```
 6. Start mock build sequence:
 ```
 mock -r fedora-$(rpm -E %fedora)-$(uname -m) --rebuild ~/rpmbuild/SRPMS/stmbot*.src.rpm
 ```
 7. Wait for a while and then install result without debug subpackages:
 ```
 sudo dnf install /var/lib/mock/*/result/python3-stmbot*.noarch.rpm --exclude="*debug*"
 ```
 8. Remove temporary files from `~/rpmbuild`, `/var/cache/mock`, `/var/lib/mock` directories.

# Systemd service
If bot was installed from RPM package, it can be controlled by systemd.

Start bot:
```
sudo systemctl start stmbot.service
```

Stop bot:
```
sudo systemctl stop stmbot.service
```

Restart bot:
```
sudo systemctl restart stmbot.service
```

Enable bot autostart on system boot:
```
sudo systemctl enable stmbot.service
```

Disable bot autostart on system boot:
```
sudo systemctl disable stmbot.service
```
