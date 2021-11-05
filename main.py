#!/usr/bin/env python
# -*- coding: utf-8 -*-

words = raw_input(">: ")
words_list = words.split(" ")
emoji_dict = {
    ":)": "😃",
    ":(": "☹️",

}
output_str = "";
for word  in words_list:
    output_str += emoji_dict.get(word,word)+" "
print (output_str)
