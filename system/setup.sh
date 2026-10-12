#!/usr/bin/env bash

#
# Setup Script
#

if [ $# -lt 1 ]; then
    echo "Usage: $0 SERVER [PORT] [BIND ADDRESS]" >&2
    exit 1
fi

s_SERVER_NAME=$1
s_PORT=${2:-80}
s_BIND=${3:-*}

set -e

cd "$(dirname "$0")"

# Checks
if ! command -V httpd >/dev/null; then
    echo -n "Error: Apache not found! " 1>&2
    echo "Please install apache."
    exit 1
fi

if ! command -V make >/dev/null; then
    echo -n "Error: Make not found! " 1>&2
    echo "Please install make."
    exit 1
fi

if ![[command -V python3 >/dev/null || command -V python3.14 >/dev/null]];  then
    echo "Error: Python not found!" 1>&2
    exit 1
fi

if ! [[ "$(python3 --version)" =~ Python 3\.14\..*]]; then
    echo "Error: Wrong Python Version (Expected 3.14.X, got '$(echo $(python3 --version))')" 1>&2
    exit 1
fi


# Dir Setup
mkdir -p /etc/httpd/sites-enabled
mkdir -p /etc/httpd/sites-available
mkdir -p /var/www/$s_SERVER_ALIAS/html
cat > /etc/httpd/sites-available/$s_SERVER_ALIAS.horseworld.ca.conf <<EOL
<VirtualHost $s_BIND:$s_PORT>
    ServerName $s_SERVER_ALIAS.horseworld.ca
    ServerAlias $s_SERVER_ALIAS
    DocumentRoot /var/www/$s_SERVER_ALIAS/html
    ErrorLog /var/log/httpd/$s_SERVER_ALIAS/error.log
    CustomLog /var/log/httpd/$s_SERVER_ALIAS/requests.log combined
</VirtualHost>
EOL
ln -s /etc/httpd/sites-available/blog.horseworld.ca.conf /etc/httpd/sites-enabled/blog.horseworld.ca.conf

mkdir -p /var/log/httpd/$s_SERVER_ALIAS
touch /var/log/httpd/$s_SERVER_ALIAS/error.log
touch /var/log/httpd/$s_SERVER_ALIAS/requests.log


# System Files
if ! [[ -e /etc/systemd/system/pelican.service ]]; then
    echo -n "Creating pelican.service..."
    cat "$(dirname "$0")/pelican.service" > /etc/systemd/system/pelican.service
    systemctl daemon-reload
    systemctl enable pelican
    if [[ -e /etc/httpd/conf/httpd.conf ]]; then
        echo "Adding configurations to Apache..."
        echo "IncludeOptional sites-enabled/*.conf" >> /etc/httpd/conf/httpd.conf
    fi
fi

# Environment
if ! [[ -d "$(dirname "$0")/.venv" ]]; then
    python3.14 -m venv .venv
    source .venv/bin/activate
    python -m pip install --no-cache-dir -r requirements.txt
fi

echo "Success - Setup Finished!"

exit 0