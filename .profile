export QT_QPA_PLATFORMTHEME="qt5ct"
export EDITOR=/usr/bin/emacs
export GTK2_RC_FILES="$HOME/.gtkrc-2.0"
# fix "xdg-open fork-bomb" export your preferred browser from here
export BROWSER=/usr/bin/qutebrowser

export JAVA_HOME=/opt/jdk-17.0.6+10/bin
export PATH=$PATH:/opt/jdk-17.0.6+10/bin:/opt/Discord:/opt/i3-layout-manager

export OPENAI_API_KEY=`pass openai`
export AWS_ACCESS_KEY_ID=`pass aws/access-key-id`
export AWS_SECRET_ACCESS_KEY=`pass aws/secret-access-key`
export REGION_NAME=eu-central-1

export PYSTRAY_BACKEND=gtk


# Added by Toolbox App
export PATH="$PATH:/home/rowan/.local/share/JetBrains/Toolbox/scripts"
export PATH="$PATH:/home/rowan/opt/JetBrains Rider-2021.3.4/bin"
