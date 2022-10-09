print('Tale of Two Bridges')
n = input("Traveler's Name?:")
print('Welcome', n)
print('Our story begins at the head of a trail in the mystical land of Telligrade')
print(n, 'you have been met with a decison, to cross the bridge to the right or to the left')
print('which do you choose traveler?')
r = input('Right or Left?')
x = str('Right')
y = str('Left')
if r == x:
    exit('you died due to a perolius fall!')
else:
    print('you found a tresure chest!')
    print(n, 'inside you found two weapons a dark dagger and a shining sword')
    z = input('Dagger or Sword?')
    d = str('Dagger')
    s = str('Sword')
    if z == d:
        exit('The dagger was cursed and you perished!')
    else:
        print('The sword shines with the light of a thousand suns!')
        print('You Win!')
