#!/usr/bin/env zsh

EXTRA_PARSE=""

while getopts k:e: flag
do
    case "${flag}" in
        k) api_key=${OPTARG};;
        e) endpoint=${OPTARG};;
    esac
done

curl -sH "Authorization: Bearer ${api_key}" "${endpoint}" | grep "County" | awk -F'|' '/{{Countyrow/ {for (i=1; i<=NF; i++) if ($i ~ /^Name=/) {sub(/^Name=/, "", $i); print $i}}' | sed -E 's/^[[:space:]]+//; s#/n##g'
