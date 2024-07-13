# path to .ttf file that should be converted
input_file=$1

# get rid of the extension
name=$(echo "$1" | cut -f 1 -d '.')

# settings for pyftsubset
# Basic Latin, Latin-1 Supplement, Double Quotation Marks, €, „, “, “, EN Dash, EM Dash, Minus, EM Space, EN Space
unicodes="U+0020-007F,U+0080-00FF,U+201E,U+201C,U+20AC,U+201E,U+201C,U+201D,U+2013,U+2014,U+2212,U+2002,U+2003"
layout_features="tnum,ss01,ss02,ss03,ss04,ss05,ss06,ss07,ss08,ss09,ss10,ss11,ss12,ss13,ss14,ss15"
flavor="woff2"

echo "Converting ${input_file} to ${name}.woff2"

# run the command
pyftsubset ${input_file} --unicodes=${unicodes} --layout_features=${layout_features} --flavor=${flavor} --output-file=${name}.woff2