#Requirements Document


##1.Functional

**A list of models that will need to be implemented.**

* A model for comments being posted

* A profile model that the user can customize.
 Their names and passwords will be unique
 and unmodifiable from admins. They may 
 carry a sort of reputation/rating, with
 statistics on the number of reviews they have 
 made, along with a avatar picture. A repository for the
 reviews that they have made will be provided.

* A moderated reviews/comments section with the ability for users 
 to flag for inappropriate content and have them reviewed by a moderator.

* A search model that allows searches for reviews or profiles.

* A home page model that displays the most reviewed/latest released 
 games, along with a poll section.

* A article model that allows the writer to include 
 images, link videos, and access varying fonts for emphasis.

* The poll model will keep count of the number of votes it has,
 as well as a closing period that the maker can specify.
 A poll can be scheduled to be released at a certain time, and
 only a trusted number of people have permission to release a poll.

* Templates to help make the website look appealing.

##2.Information

* This being a simple review website, the most that's needed as input 
  from a user would be an image, whether it's for their avatar or their 
  review.
  Besides that there will be incremental integer values for reputation, 
  number of articles made, a counter for votes in a poll, among other 
  things.
  
* Users will be able to flag content as inappropriate and have it reviewed
  by a site moderator. Upon finding content inappropriate the moderator 
  will remove the post and flag the user's account and punitive action 
  will be taken.
  
* The search functionality will be a text box which will search the review
  content and return relevant results to the user.
  
* There will be a home page which will have different tabs/menus that will
  allow the user to access the most viewed content, newest content, and 
  other popular features.

* The model for a profile would contain fields for the photo being 
  uploaded, some integer fields like their reputation value, a comment 
  that they have posted that was well-received, and a field for the number 
  of reviews that they have posted
  
* The article model has a many-to-one relationship with the profile model.
  Meaning that a profile model can have multiple article models, each 
  holding a field of the user, a field that will limit the amount of words
  to around 5kb.
  
* There will be a field for a image being uploaded, and it has to be limited
  to a predetermined size. 
  There will also be a link field, and a video field, which will hold 
  lists of links and videos that the writer of the article puts up. 
  Finally, any registered user who reads the article may give the article 
  a thumbs-up or thumbs-down. If the ratio to thumbs-ups and thumbs-downs 
  are more in favor of thumbs-downs, the comment will be hidden.
  
* Comments also has a one-to-many relation to the profile model. There 
  will be a white box at the end of a article, where the user can enter 
  text and submit as a comment. The posted comment will have a date that 
  it was made, along with the name of the user who posted it, and 
  thumbs-up/thumbs-down counters. If the difference between thumbs-up and 
  thumbs is at a certain threshold the comment will be hidden.
      
##3.Physical
      
* The site will need to be hosted. No other resources will be needed in
* order for it to function.
  
* This site will not support mobile devices.

##4.Inputs/Outputs
      
###Inputs:

* a. Reviewers can hyperlink other website pages.
     This takes a word that will be highlighted blue
     and a link that will be alongside it.

* b. Reviewers can embed videos and photos in their posts as well as
     adding text.

* c. Reviewers can click the thumbs-up/thumbs-down icon to up or 
    down vote a post.
      
###Outputs:
      
* a. The site will display the posts that the user requests.

* c. If there is an embedded video then it will be displayed to the 
     user.

* b. The thumb-up/thumb-down will be highlighted when it is selected
     by the user.
	
##5.Constraints
      
* The only constraints that we can foresee will be based on the time 
       allocated to complete the project.
       
