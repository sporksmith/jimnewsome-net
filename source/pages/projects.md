title: projects
date: 2012-08-09 21:04

## Creative Coding

### Guinea Pig Guinea Pig 

![Guinea Pig Guinea Pig](/images/gpgp.png)

Guinea Pig Guinea Pig is an HTML5 game made for the
[2013 Global Game Jam](http://globalgamejam.org/2013/guinea-pig-guinea-pig).
You play a (further) miniaturized, super-powered, Guinea Pig.
Your job is to weaken (with your eye-lasers, of course) and collect
the germs infecting the patient's arteries, while contending with
the rhythmic blood flow.

Made with Brian Bogovich and [Lara Schenk](http://notlaura.com/).
Soundtrack "Bang That Accordian" by [Bonnie Bogovich](http://www.blackcatbonifide.com/).

[Play it now!](/projects/gpgp/)

### Dance Ave

![Dance Ave](/images/dance-ave.jpg)

[Dance Ave](https://github.com/sporksmith/dance_ave/)
 is a physical game where players try to reach all of several stations positioned around an area.
Players may only move between stations by dancing with passers-by.
The telephony back-end comes in at the stations, where players dial a special code
with their cell phone. Doing so gives the player credit for reaching that station, tells them
how many stations they have left to visit, and then plays the song for that station.
Players use that song to groove over to the next station.

[Related blog posts](/blog/categories/danceave/)

### EepEepMotion

![Monkey Labeling](/images/monkey-labeling.jpg)

EepEepMotion is a tool for *opportunistic stop motion*; given a set of
photographs with some common object (e.g., a stuffed monkey) in them,
it lets the user create an animation using individual photos as
animation frames. To achieve this, the user labels where the target
object is in each photo using EepEepMotion, creates an animation with
a place-holder object using the standard Blender tools, exports the
animation using an included Blender plugin, and uses EepEepMotion
again to render the animation.

This tool was developed to create the
[Travels of Code Monkey](#travels-of-code-monkey) video. With a little
work it could be generalized and made more user-friendly.

 * [Travels of Code Monkey (video)](http://www.youtube.com/watch?v=qhV4mSn1jrY)
 * [Source code](https://github.com/sporksmith/EepEepMotion)
 * [Development journal](http://sporksmith.wordpress.com/travels-of-code-monkey/)

Technologies:

 * [Processing](http://processing.org/)
 * [Blender](http://www.blender.org/)

### Piranha Tank (work in progress)

![Piranha Tank](/images/piranha-tank.png)

Piranha Tank is a tablet/smart-phone toy in which a swarm of hungry
piranhas pursues and munches on the user's finger. I'm building it with
Haxe and NME, allowing it to be deployed across many platforms.

Current builds:

 * [Flash](/projects/piranha-tank/piranha-tank.swf): Play in your browser
 * [Android](/projects/piranha-tank/piranha-tank-debug.apk): Install on your
   Android device ("Unknown sources" must be enabled)

Technologies:

 * [Haxe](http://haxe.org/)
 * [NME](http://www.haxenme.org/)
 * [HaxePunk](http://haxepunk.com/)

### Creator

![Creator Snake](/images/creator-snake.png)

Creator was made in 48 hours for the 2012
[Global Game Jam](http://globalgamejam.org/), tying for second
place. I was involved in the game design and implementation. This
included creating a custom audio manager to handle synchronized and
spatially positioned musical loops.

> Part music mix box, part Nibbler, and part 'just a fun tech
> toy'. Devour your own tail to create new planets. Planets grow and
> evolve and can be consumed again. Each planet grows musically, and
> all planets combined make a lush soundtrack. Make your own universe,
> losing part of yourself every time and devour planets to get your
> tail back to start the cycle anew.

 * [Project page](http://globalgamejam.org/2012/creator/): Credits,
   source code, etc.
 * [Source](/projects/creator/Creator_GGJ12.zip)
 * [Play!](/projects/creator/creator-MKBBJN-v2.swf)

Technologies:

 * ActionScript

### Doc Brown mind-reading helmet

![Sleeptalkers helmet](/images/sleeptalkers-helmet.jpg)

I helped create a replica of
Doc Brown's [mind-reading helmet](images/doc-brown-thinking-cap-back-to-the-future.jpg),
originally for a group Halloween costume. I designed and integrated
the pulsing LED system, (with pulse rate controllable by a
potentiometer), using an Arduino.

* Used as "time projection helmet" in the short film: [Sleeptalkers](http://www.youtube.com/watch?v=1FhZdwLL6iI&t=1m).

Technologies:

 * C
 * [Arduino](http://www.arduino.cc/)
 * [FoamCore](http://en.wikipedia.org/wiki/Foamcore)

## Security research software

### XMHF, TrustVisor, TEE-SDK, TEE-Cred

My recent academic work uses trusted computing and virtualization to
create isolated, trustworthy execution environments. While trusted
computing is often perceived as restricting what the *user* can do
(e.g., DRM), our work focuses on restricting what *malware* can do
(e.g., protecting a password database from malware in TEE-Cred), or on
restricting what remote servers can do (e.g., forcing the server to
prove that it doesn't store or leak your plaintext password).

I contributed heavily to the TrustVisor hypervisor. I also created the
TEE-SDK---development tools for using Trusted Execution
Environments---and TEE-Cred---a password manager that protects its
database from malware.

 * [Project page](http://xmhf.org)

Technologies:

 * C
 * x86 assembly
 
### TaintCheck

TaintCheck is a plugin for [Valgrind](http://valgrind.org/) that
performs dataflow analysis (taint analysis) to track how untrusted
data is propagated and used in a running program binary. This
technique has a number of applications, including detecting many types
of control-flow-hijacking exploits.

The source code is available on request. However, it is no longer
maintained, and does not work with recent versions of Valgrind. You
might be interested in
[TEMU](http://bitblaze.cs.berkeley.edu/temu.html) instead, which
performs whole-system taint analysis in QEMU.

Technologies:

 * C
 * Valgrind

### Vine

Vine is a tool for static analysis of x86 assembly. I was involved
in its design and implementation.

* [Vine project](http://bitblaze.cs.berkeley.edu/vine.html)

Technologies:

 * C
 * x86 assembly

### Polygraph

Polygraph is a set of tools for generating signatures from a few
examples of exploits or worms in a network trace. In particular, it
was designed to work for *polymorphic* worms, which use code
obfuscation and encryption to make such signature generation
difficult.

Technologies:

 * Python


## Videos

### Travels of Code Monkey

![Code monkey](/images/code-monkey.jpg)

I created this video using my tool [EeeEepMotion](#eepeepmotion).

 * [Travels of Code Monkey](http://www.youtube.com/watch?v=qhV4mSn1jrY)

### FriendStat

![FriendStat](/images/friendstat.jpg)

FriendStat was an entry and audience-choice award winner in the 2011
Pittsburgh 48 Hour Film Festival. I was on the writing team, and
played 'Gas mask in black'.

 * [FriendStat](http://www.youtube.com/watch?v=gt2-7ZuFwSU) on YouTube

### Re: Firm Adness

![Re: Firm Adness](/images/re-firm-adness.jpg)

Re: Firm Adness was an entry and audience-choice award winner in the
2012 Pittsburgh 48 Hour Film Festival. I was on the writing team, and
played 'wholesome Dad'.

 * [Re: Firm Adness](http://www.youtube.com/watch?v=2u_C828d3aM) on YouTube

### I Feel Fantastic

![I Feel Fantastic](/images/fantastic-whee.jpg)

This is a music video created for Jonathan Coulton's song
[I Feel Fantastic](http://www.jonathancoulton.com/wiki/I_Feel_Fantastic). I
starred and co-directed.

 * [I Feel Fantastic](http://www.youtube.com/watch?v=zidiWe9yq88) on YouTube

## Stage

 * [Pittsburgh Savoyards](http://www.pittsburghsavoyards.org/)
   * Pirates of Penzance 3/2012: ensemble
   * Yeomen of the Guard 10/2012: ensemble
 * [Parallax Second Players](http://www.parsec-sff.org/confluence/play.html)
   * [SupermAnnie](https://www.facebook.com/events/409836555719502/) 7/2012: General Zod (also created the logo, and Zod costume)
 * [Evening in Quarantine: The Zombie Opera](http://www.thezombieopera.com/)
   10/2010: running soldier
