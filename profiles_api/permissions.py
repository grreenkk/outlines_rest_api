from rest_framework import permissions

#This used to rstrict users can only change or update their profiles not another user's profile
class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:#This checks that the http method is a safe method like HTTP GET
            return True

        return obj.id == request.user.id#This ensures that the object change has the same id as the users id, if it does this will return true
        # but if its not it will report false



class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""
    def has_oject_permission(self, request, view, obj):
        """Check the user is trying to update their own status"""
        if request.method in permission.SFAE_METHODS:
            return True

        return obj.user_profile.id == request.user.id#This ensures that the user making the request, if the user profile id is the same with the
        #request id updating the object, then it will return true and allow the user to update the object
