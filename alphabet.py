alphabet = {'!': 'n', ' ': 'r', '#': 'e', '%': 'a', '$': 'h', '&': 'b', '*': 'o', '-': 'd', '/': 's', ';': ' ', ':': 't', '=': 'i', '?': 'w', '@': 'j', ']': 'm', '_': 'c', 'a': 'f', '`': 'x', 'b': 'k', 'e': 'y', 'd': 'l', 'f': '/', 'o': 'v', 'n': '.', 'p': ':', 'r': 'g', 'w': 'q', 'x': 'p', 'z': 'u', '|': 'z'}

wtf = "@z/:;=!;_%/#;e*z;$%o#;-#_=-#-;:*;: %!/d%:#;:$=/;]#//%r#;&e;$%!-,;=;%];%--=!r;=!;d*:/;*a; %!-*];?* -/;%!-;/#!:#!_#/;:*;]%b#;:$=/;]* #;-=aa=_zd:n;&d%$;&d%$;&d%$n; */#/;% #; #-,;o=*d#:/;% #;&dz#,;=;d=b#;_$*_*d%:#/;&z:;!*:;:$#;*!#/;a *];e*zn;*b%e;=;:$=!b;=;$%o#;-=/_*z %r#-;%!e;]%!z%d;: %!/d%:=*!n;!*?;a* ;:$#; #%d;]#//%r#p;$#dd*;:#%],;_*!r %:zd%:=*!/;*!;-#_=x$# =!r;:$=/;]#//%r#n;$*?#o# ,;?#;% #;!*:;wz=:#;-*!#;e#:n;e*z;]z/:;r*;*!:*;]=]=_$#!226@r=:$z&n=*;%!-;a=!-;:$#;/#_ #:;]#//%r#n;*!_#;e*z;a=!-;:$#;/#_ #:;]#//%r#,;#!:# ;=:;:*;:$#;_*?;x *]x:"

result = " "


for char in wtf:
    if char in alphabet.keys():
        result += alphabet[char]
    else:
        result += char
print (result)
