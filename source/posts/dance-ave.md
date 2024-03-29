title: Dance Ave
date: 2013-07-06 14:47

I got an interesting request a few months ago--to implement the telephony back-end
for a real life dancing game to be played at the
2013 [Three Rivers Arts Festival](http://www.3riversartsfest.org/).

![Dance Ave](/images/dance-ave.jpg)

[Dance Ave](http://www.cityofplay.org/traf/)
 is a physical game where players try to reach all of several stations positioned around an area.
Players may only move between stations by dancing with passers-by.
The telephony back-end comes in at the stations, where players dial a special code
with their cell phone. Doing so gives the player credit for reaching that station, tells them
how many stations they have left to visit, and then plays the song for that station.
Players use that song to groove over to the next station.

I ended up implementing the back-end with the [Django](https://www.djangoproject.com/) web framework,
and using the [Tropo](https://www.tropo.com/home.jsp) programmable telephony service.
The more mainstream option for telephony of course would have been [Twilio](http://www.twilio.com/).
I ended up using Tropo because initially we were also going to make an SMS-based game,
and Tropo has cheaper rates for SMS.
Still, Tropo was fairly pleasant to use. One nice feature in particular is that until you move your app
from "debug mode" to "production mode", all services are free. So, you can feel free
to blast the service with requests during development and testing without worrying about racking
up a big bill.

Unfortunately the player scores were inadvertently reset both times the game was played.
After reviewing the logs again, I found a [usability issue](https://github.com/sporksmith/dance_ave/issues/1)
with the administrative dashboard page that was most likely the cause.
Long story short--from now on I'll remember to use the [Post-Redirect-Get](https://en.wikipedia.org/wiki/Post/Redirect/Get)
pattern to avoid accidental re-`POST`s.

Luckily the score for Dance Ave is mostly immaterial, and folks still 
[had fun playing it](https://www.facebook.com/media/set/?set=a.10151753193669892.1073741833.555979891&type=1&l=21b6c3dff1).
The code is now available [on GitHub](https://github.com/sporksmith/dance_ave).
