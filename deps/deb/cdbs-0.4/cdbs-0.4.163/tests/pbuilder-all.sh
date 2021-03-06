#!/bin/bash
# -*- mode: sh; coding: utf-8 -*-
# Try to build all CDBS-using packages
# Copyright © 2003 Colin Walters <walters@debian.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

set -e

progname=$(basename "$0")

usage () {
    echo "Usage:"
    echo " --buildir DIR	Build packages in directory DIR"
    echo " --printonly		Print CDBS-using packages and exit"
    echo " --sourceonly		Download source for CDBS-using packages and exit"
    echo " --packages		Build only these packages"
}

while [ $# != 0 ]; do
	case "$1" in
	--builddir)	builddir=$2; shift;;
	--printonly)	printonly=yes;;
	--sourceonly)	sourceonly=yes;;
	--packages)	allpkgs=$2; shift;;
	*) echo >&2 "$progname: unknown option or argument $1"; usage; exit 2;;
	esac
	shift
done

if test -z "$allpkgs"; then
  allpkgs=$(build-rdeps --quiet cdbs)
fi

echo "$allpkgs"

if test -n "$printonly"; then
  exit 0
fi

if test -z "$builddir"; then
  builddir=$(mktemp -d /tmp/cdbstestXXXXXXXX)
fi    
mkdir -p "$builddir"
printf "Builddir is %s\n" "$builddir"

cd "$builddir"
for pkg in $allpkgs; do
    test -z "$sourceonly" || printf "building \"%s\"" "$pkg"
    apt-get source "$pkg"
    if test -z "$sourceonly"; then
	(
		set -e
		cd "$pkg"-*
		pdebuild
	)
    fi
done
