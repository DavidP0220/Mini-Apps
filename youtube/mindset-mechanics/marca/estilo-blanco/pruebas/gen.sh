#!/bin/bash
gen(){ # $1=archivo $2=prompt $3=seed $4=model
  Q=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$2")
  for n in 1 2 3 4 5 6; do
    c=$(curl -sS -m 150 -o "$1" -w "%{http_code}" "https://image.pollinations.ai/prompt/$Q?width=1024&height=1024&nologo=true&seed=$3&model=$4")
    [ "$c" = "200" ] && { echo "$1 OK ($(stat -c %s $1)b)"; return; }
    node -e "const t=Date.now();while(Date.now()-t<10000){}"
  done
  echo "$1 FALLO"
}
