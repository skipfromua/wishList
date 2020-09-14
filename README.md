# wishList
Hi this is my test task for Star.
You can manage your wishlist by get, post, put or delete requests. 

But only authenticated user can manage it. You can sign up and use login + password or authenticate by google.

Main page will offer you to add some object from others wishlists to one of yours.

1. If you need to create a new wishlist, you need to send post request for 
https://wishlist-manager-test.herokuapp.com/api/v1/wishlist/ {'wishlistName':'SOME_NAME', 'wishlistOwnerID':'OWNER_ID', 'isSharedToOthers':'True or False'}

2. If you need to see your and shared wishlists, you need to send get request for
https://wishlist-manager-test.herokuapp.com/api/v1/wishlist/

3. If you need to update a new wishlist, you need to send put request for 
https://wishlist-manager-test.herokuapp.com/api/v1/wishlist/<id>

4. If you need to delete your and shared wishlists, you need to send delete request for
https://wishlist-manager-test.herokuapp.com/api/v1/wishlist/<id>

5. If you need to create a new wishObject, you need to send post request for 
https://wishlist-manager-test.herokuapp.com/api/v1/wishlist/<wishlist_id>/wishObjects/
{'objectName':'SOME_NAME', 'objectDescription':'SOME DESCRIPTION', 'reasonToHave':'WHY DO YOU NEED IT', 'objectLocation':'WHERE YOU CAN GET IT', 'requirementsToDo':'WHAT DO YOU NEED FOR IT', 'wishlistId':'ID OF WISHLIST'}

6. If you need to see wishObjects in current wishlist, you need to send get request for
https://wishlist-manager-test.herokuapp.com/api/v1/wishlist/<wishlist_id>/wishObjects/

7. If you need to update wishObjects in current wishlist, you need to send put request for 
https://wishlist-manager-test.herokuapp.com/api/v1/wishlist/<wishlist_id>/wishObjects/<id>

8. If you need to delete wishObjects in current wishlist, you need to send delete request for
https://wishlist-manager-test.herokuapp.com/api/v1/wishlist/<wishlist_id>/wishObjects/<id>
