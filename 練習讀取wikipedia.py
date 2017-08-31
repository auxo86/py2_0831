#  encoding=utf-8

import wikipedia

print wikipedia.summary('jetbrain')
print wikipedia.search('C++')
taipei = wikipedia.page("Taipei")
print taipei.title, taipei.url
print taipei.content
print taipei.links[0]


wikipedia.set_lang('zh-tw')
print wikipedia.summary('Taipei', sentences=4)
