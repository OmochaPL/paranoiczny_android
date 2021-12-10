#program wybiera 3 wycinki, dzięki którym można wyodrębnicć i wyświetlić  fragmenty listy

paranoid_android = "Marvin, paranoiczny android"
letters = list(paranoid_android)

for char in letters[:6]:
    print('\t', char)
for char in letters[-7:]:
    print('\t'*2, char)
for char in letters[8:19]:
    print('\t'*3, char)
    
    
