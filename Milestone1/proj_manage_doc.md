<!--- Project Management Document, by Sean Soderman -->


#Project Management Document for team Django Fett

##I. Task definition
The goals of our website are to provide a modern game review website where users can
review and converse about games. This large goal is composed of many smaller tasks, including
the implementation of:


* A system for storing pictures and plaintext documents
* A comments system for communication
* A moderation system that detects questionable content or flagged posts,
* The ability to search for content
* A user rating system similar to StackOverflow's that will allow users to rate reviews.
* A poll system that will allow system administrators to ask the userbase daily "fun" questions
about various gaming related topics.
* And a modern UI that will make the website pleasant to use.

##II. Risks

Since we aren't doing this for a company there are no real monetary risks. However, figurative risks
might include:

###Company risks:
* A low amount of profit due to the "free" nature of the site
* Copyright issues with sites who may use similar styles for their sites
* A small consumer/user base
* Low ad revenue


###User risks:
* Security issues arising from user account information being compromised
* Difficulty using the site due to a physical disability
* Loss of repuation due to making a fool of oneself online

###How we will minimize these risks:
We'll partner up with Amazon and other online retailers and offer users deals from their
sites with links. This will generate revenue that will offset any loss of ad revenue.

We will also use a unique style for our site's design that will set it apart from similar sites
such as GameFAQS or Gamespot. This will prevent any copyright issues.

The reputation system, as well as the comments section for games, will make the website
fun to use and encourage people without accounts to sign up.

As for the user risks, we will use cutting edge hashing algorithms to securely store all user's
passwords in our database. We will also use a screen reader for the site to accomodate those with
blindness. We will also warn users before they post something stupid or inappropriate, and no
two users will be allowed to have the same username, so nobody will be able to ruin someone
else's reputation by posing as them.

##III. Evaluation criteria and methods
###We plan to run a user study to evaluate usability.

##IV. Implementation

### I (Sean) will do:
* Design of the rudimentary text editor for the review writer
* Developing a form fill in system for users to write comments
* Design of the user account system
* Implementation of the poll system

###Kurt will handle:
* Designing a post flagging system for users
* Implementing the admin tools to review and act upon flagged posts/content (i.e., remove them)
* The database that will handle storage of flagged posts

###Vincent will make:
* The system for rating users' contributions
* A way to gauge a user's "reputation", which will be improved with more upvotes
* A reward system that will dole out "badges" based on a user's helpfulness to the site

###Josh will generate:
*  The metaphorical coat of paint (CSS) for the website that will give it its modern look 
* The search bar which will allow users to find any game listed on the site
* A game rating system that will tie in to a user's review

###Dylan will develop:
*  The database for storing text and pictures for reviews and games
*  The layout of the home page
*  Information pertaining to game data (i.e, the company who made the game, when the game was made)
*  The screen reader for the website that will accomodate those with vision disabilities


##V. Training
Sometimes, a feature of a website is not immediately apparent to the user. To avoid as much
confusion as possible, a FAQ page will be supplied on the main navigation bar of the
website. An email account will be  created for the sole purpose of processing help request mail
from users.

Sean, Kurt, and Vincent will be responsible for the development of this FAQ and system.

##VI. Maintenance
To keep the website in usable shape, it is important that moderators take down offensive
posts that could jeopardize the user-friendliness of the site. It is also important that
developers maintain strong password hashing algorithms so that, even if the database
of passwords is compromised, it would be difficult for hackers to discern even simple
passwords. A bi-monthly message to all users recommending that they change or strengthen
their passwords could also ensure a minimum of password cracking.

##VII. Future needs
A forum would be absolutely essential to the growth of the website community wise. If forums for each
game could be implemented that would spur tons of site traffic and conversation, which would do
very well for the site's ad revenue and other means of revenue (links to other sites). Also, a
friend system and private messaging system would also prove to be quite useful and, similar to
forums, would spur more conversation and use of the site.
