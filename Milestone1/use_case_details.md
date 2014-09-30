Django Fett: Use Cases
===================
**********************
##UC01: View Landing Page

**Goal:** User views Django Fett home page.

**Primary Actors:** Visitor, User, Admin

**Precondition:** Django Fett web server is running and configured correctly.

**Main Flow:**

1. User requests to view landing page via web browser.
2. Web server responds with landing page data.
3. The default landing page is displayed in user's browser.

**Alternative Flows:**

1. Web server cannot find landing page resources (aka 404).

**Post Conditions:** User's browser is displaying the Django Fett home page. The web page is ready to accept the next request.

##UC02: Register for Web Site

**Goal:** A visitor to the website has an account created.

**Primary Actors:** Visitors

**Precondition:** Website is operational.

**Main Flow:**

1. User clicks 'Register' button on web site.
2. Web server responds with landing page data.
3. User registration form is displayed on visitor's browser.
4. Visitor enters their information in the form.
5. Visitor presses 'Register' button.
6. Visitor is redirected to Log In page.

**Alternative Flows:**

1. Web server cannot find page resources (aka 404)
2. User enters invalid information.
3. User enters already-used username or email address.

**Post Conditions: ** Row added to Django Fett user database with user's details. User's browser is displaying Log In page.

##UC03: Log In

**Goal: ** User is logged into website.

**Primary Actors: ** User

**Precondition: ** Website is operational. User has an account.

**Main Flow:**

1. User clicks 'Log In' button on website.
2. Web server responds with log in page data.
3. Log In form is displayed in user's web browser.
4. User enters their log in credentials.
5. User presses 'Log In' button.
6. User is redirected to Landing Page.

**Alternative Flows:**

1. 404
2. Credentials are invalid.

**Post Conditions:** User is logged into web page.

##UC04: Reset Password

**Goal: ** User's password is reset.

**Primary Actors: ** User

**Precondition: ** Website is operational. User has an account.

**Main Flow:**

1. On the 'Log In' page, user presses 'Forgot Password' link.
2. User is presented with a text field to enter username.
3. User enters their username and presses 'Submit' button.
4. User's secret question is presented along with a text field for their answer.
5. User enters answer to question.
6. User enters a new password.
7. User presses 'Submit'
8. User is redirected to log in page.

**Alternative Flows:**

1. 404
2. Username is not valid.
3. Response to secret question is not valid.
4. New password is not valid.

**Post Conditions:** User's password is updated on user database. User's browser is displaying log in page.

##UC05: View Game List

**Goal: ** Display a list of games on the website.

**Primary Actors: ** User, Visitor, Admin

**Precondition:** Website is operational.

**Main Flow:**

1. User clicks 'Games' on the navigation menu.
2. A list of games is displayed

**Alternative Flows:**

1. 404
2. Retrieved 0 games (database returned zero rows)

**Post Conditions: ** User's browser is displaying game list page.

##UC06: Post Review

**Goal: ** A user adds a new game review to the website.

**Primary Actors:** User

**Precondition: ** Website is operational. User has an account. User is viewing a 'game detail' page.

**Main Flow:**

1. 
  1. User presses 'Post Review' button on game detail page.
  2. User is presented with the 'post review' form to fill out.
  3. User enters their review (fills out form).
  4. User presses 'Submit' button.
  5. User is redirected to their newly added review page.

**Alternative Flows:**

1. Review form field validation failed.
2. 404.
3. Unable to reach database.

**Post Conditions: ** Review is added to website database. User's browser is displaying new review.

##UC07: Read Review

**Goal: ** Display a review page.

**Primary Actors:** Visitor, User, Admin

**Preconditions: ** User is viewing a game detail page.

**Main Flow:**

1. User presses a link to a review.
2. The review selected is displayed in the user's web browser.

**Alternative Flows:**

1. Invalid Review (Review has been deleted).
2. 404.

**Post Conditions: ** User's browser is displaying a game review.

##UC08: Search For Game

**Goal: ** A list of games matching an entered query is displayed on the user's browser.

**Primary Actors: ** Visitor, User, Admin

**Preconditions: ** User is on a page with the website's search bar available in the header. ****

**Main Flow:**

1. User enters their search query in the search text field.
2. User presses return key on keyboard or presses 'Search' button.
3. User is presented with a list of games which match their search query.

**Alternative Flows:**

1. Search found zero matches.
2. Invalid search query.
3. 404.

**Post Conditions: ** User's browser is displaying a filtered list of games.

##UC09: Like/Dislike Review

**Goal: ** A review's 'like' or 'dislike' count is altered.

**Primary Actors: ** User

**Preconditions: ** User is viewing a game review page.

**Main Flow: **

1. User presses one of two icons on the review page indicating that they 'like' or 'dislike' the review they are viewing.
2. The number of likes and dislikes is updated in the user's browser.
3. The review's like or dislike count is altered appropriately in the database.

**Alternative Flows:**

1. 404
2. Cannot reach database

**Post Conditions: ** A review's like/dislike count is altered on database.

##UC10: Edit Review

**Goal: ** Edit a review.

**Primary Actors: ** User, Admin

**Preconditions: ** Actor is the author of the review or an Administrator. Actor is viewing a game review page.

**Main Flow:**

1. The user presses the 'Edit Review' button.
2. User is presented with the edit review page.
3. Fields are automatically populated with current review data.
4. User edits the review's fields.
5. User presses 'Submit' button.
6. User is redirected to the game review page which is now displaying the updated version.

**Alternative Flows:**

1. User is not the author of the review or is not an admin.
2. Review fields invalid.
3. 404.

**Post Conditions: ** A review's row on the database has its fields altered. User is viewing the updated review page.

##UC11: View Profile

**Goal: ** View a user's profile page.

**Primary Actors: ** Visitor, User, Admin

**Preconditions: ** User in on a page in which usernames are displayed (e.g. Game Review, Comments, etc.)

**Main Flow:**

1. Actor clicks on a username for a user.
2. Selected user's profile page is displayed on page.

**Alternative Flows:**

1. User does not exist.
2. User has been deleted.
3. 404.

**Post Conditions:** Actor's web browser is displaying a profile page.

##UC12: Edit User/Profile

**Goal: ** Edit a user's profile.

**Primary Actors: ** User, Admin

**Preconditions: ** User is viewing their own profile page.

**Main Flow:**

1. User presses 'edit profile' button.
2. User is presented the edit profile page.
3. Fields are automatically populated with appropriate data.
4. User updates their profile fields.
5. User presses 'Submit' button.
6. User is redirected back to their own profile page.

**Alternative Flows:**

1. User is trying to edit another user's profile.
2. Actor is not an administrator.
3. Invalid profile form data.
4. 404.

**Post Conditions: ** User's profile database entry is updated.

##UC13: Post Comment on Game

**Goal: ** Post a comment about a game.

**Primary Actors: ** User

**Preconditions: ** User is viewing a game detail page.

**Main Flow:**

1. At the bottom of the game detail page, a user enters a comment in the text box labeled 'Comment'
2. User presses 'Submit' next to comment box.
3. User's browser is refreshed and page is scrolled down to comments section.

**Alternative Flows:**

1. Comment field validation failed.
2. 404.

**Post Conditions: ** A row is added to the comments table in website database.

##UC14: Flag Inappropriate Content

**Goal: ** A piece of content on the web page is flagged as inappropriate.

**Primary Actors: ** User, Admin

**Preconditions: ** User is on a Game Review page, a User Profile page, or a Game Details page viewing comments.

**Main Flow:**

1. User presses an icon labeled 'Report Content' located next to user-generated content.
2. Website generates a row in a 'flagged content' table on the database.
3. The icon state changes indicating the actions was performed.

**Alternative Flows:**

1. Cannot reach database.

**Post Conditions: ** A new entry is added to the database with details about the content. (URL to content, time of report, reporting user, offending user, etc.)

##UC15: Review Flagged Content

**Goal: ** View a list of content that has been reported by users.

**Primary Actors: ** Admin

**Preconditions: ** Admin is viewing the administrator's portal.

**Main Flow:**

1. An admin presses on the 'Review Flagged Content' link.
2. A list of items is retrieved and displayed to the user.

**Alternative Flows:**

1. Actor does not have administrative rights on website.
2. Zero items retrieved.

**Post Conditions: ** Admin's browser is displaying the list of requested items.

##UC16: Disable/Delete User

**Goal: ** Disable/Delete a user account from the website.

**Primary Actors: ** Admin

**Preconditions: ** Admin is viewing a user's profile page.

**Main Flow:**

1. An admin presses a 'delete user' link/button on a user's profile page.
2. A confirmation box appears to confirm the requested action to be performed.
3. Actor presses button in confirmation box confirming the action should be performed.
4. The user's entry in the users table has its status field set to 'deleted/disabled'.
5. Admin's web browser is redirected to administrator's portal page.

**Alternative Flows:**

1. Actor is not an administrator.
2. Actor does not grant confirmation.
3. Cannot reach database.

**Post Conditions: ** A user's status is set to deleted/disabled in the database.

##UC17: Delete Review

**Goal: ** Remove a review from the website.

**Primary Actors: ** User, Admin

**Preconditions: ** User is viewing a review they are the author of or the actor is an administrator.

**Main Flow:**

1. User presses 'edit review' button.
2. User is presented the edit review page.
3. Fields are automatically populated with appropriate data.
4. User presses 'delete review' button.
5. A confirmation box appears to confirm the requested action to be performed.
6. Actor presses button in confirmation box confirming the action should be performed.
7. The review's entry in the reviews table has its status field set to 'deleted/hidden.'
8. User's web browser is redirected to another location on the website (Home Landing Page?).

**Alternative Flows:**

1. User is not the author of the review.
2. Actor is not an administrator.
3. Cannot reach database.
4. 404.

**Post Conditions: ** The selected review's database entry 'status' field is set to 'deleted/hidden.'

##UC18: Delete Comment

**Goal: ** Remove a comment from the website.

**Primary Actors: ** Admin

**Preconditions: ** Actor is an administrator. Actor is viewing comments on a game-detail page.

**Main Flow:**

1. Admin presses 'delete comment' icon/link next to the comment they would like to delete.
2. A confirmation box appears to confirm the requested action to be performed.
3. Actor presses button in confirmation box confirming the action should be performed.
4. The comment's entry in the comments table has its status field set to 'deleted/hidden.'
5. User's web browser is refreshed.

**Alternative Flows:**

1. Actor is not an administrator.
2. Cannot reach database.
3. 404.

**Post Conditions: ** The selected comment's database entry 'status' field is set to 'deleted/hidden.'