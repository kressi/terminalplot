#!/bin/env bash
set -e
set -u
set -o pipefail

maj_min_prefix=v${1}.
version=$(git tag --sort=-version:refname --list "${maj_min_prefix}*" | head -n 1)

if [ -z "${version}" ]; then
  next_patch=0
else
  next_patch=$(( ${version#${maj_min_prefix}} + 1 ))
fi

echo "${maj_min_prefix}${next_patch}"
