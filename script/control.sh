#!/usr/bin/bash
# Script by Robson Dobzinski
# 2024-03-12
if [[ -n $1 ]]; then
  if ([ -n $2 ] && [ -n $3 ]); then
    PASSPHRASE=$2
    FILE=$3
    case $1 in
      'in')
        /usr/bin/gpg2 -c --batch --quiet --passphrase "$PASSPHRASE" --output "$FILE.gpg" --symmetric "$FILE"
        #/usr/bin/sleep 1
        if [[ -e "$FILE.gpg" ]]; then
          /usr/bin/rm -f "$FILE"
          exit 0
        else
          exit 5
        fi
      ;;
      'out')
        /usr/bin/gpg2 -d --batch --quiet --passphrase "$PASSPHRASE" --output "${FILE:0:-4}" --decrypt "$FILE"
        #/usr/bin/sleep 1
        if [[ -e "${FILE:0:-4}" ]]; then
          /usr/bin/rm -f "$FILE"
          exit 0
        else
          exit 4
        fi
      ;;
      *)
        echo 'Please, inform the param: "in" to crypto file or "out" to decrypt gpg file...'
        exit 3
    esac
  else
    exit 2
  fi
else
  exit 1
fi
