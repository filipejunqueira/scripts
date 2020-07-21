urlencode() {
    # urlencode <string>
    old_lc_collate=$LC_COLLATE
    LC_COLLATE=C

    local length="${#1}"
    for (( i = 0; i < length; i++ )); do
        local c="${1:i:1}"
        case $c in
            [a-zA-Z0-9.~_-]) printf "$c" ;;
            *) printf '%%%02X' "'$c" ;;
        esac
    done

    LC_COLLATE=$old_lc_collate
}

readarray -t list <doi-list.txt

for doi in "${list[@]}"
do
    echo "Download for doi: $(urlencode $doi)"
    link=$(curl -s -L 'https://sci-hub.tw/' --compressed \
        -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0' \
        -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' \
        -H 'Accept-Language: en-US,en;q=0.5' \
        -H 'Content-Type: application/x-www-form-urlencoded' \
        -H 'Origin: https://sci-hub.tw' \
        -H 'DNT: 1' \
        -H 'Connection: keep-alive' \
        -H 'Referer: https://sci-hub.tw/' \
        -H 'Cookie: __ddg1=SFEVzNPdQpdmIWBwzsBq; session=45c4aaad919298b2eb754b6dd84ceb2d; refresh=1588795770.5886; __ddg2=6iYsE2844PoxLmj7' \
        -H 'Upgrade-Insecure-Requests: 1' \
        -H 'Pragma: no-cache' \
        -H 'Cache-Control: no-cache' \
        -H 'TE: Trailers' \
        --data "sci-hub-plugin-check=&request=$(urlencode $doi)". | grep -oP  "(?<=//).+(?=#)")

    echo "Found link: $link"
    article=$(getbib $doi | grep -oP '\@article\{\K[^,]+')
    month=$(getbib $doi | grep -oP 'month = \{\K[^}]+')
    curl -s -L $link --output $article$month.pdf
done

