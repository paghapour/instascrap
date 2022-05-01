import profile
import instaloader


class instagram:

    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context , 'pooriaaghapour')
    #print(profile.followers)
    #print(profile.followees)
    followers=(profile.followers)
    followees=(profile.followees)
