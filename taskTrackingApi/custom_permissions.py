from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission, BasePermissionMetaclass
from rest_framework.exceptions import PermissionDenied


''' create a customise permission for and admin access '''


class AdminCanAccess(BasePermission):
    message = "you cannot access , you need to be an admin"

    ''' 
    it will allow to create a data if current user is and admin, 
    if user is not an admin they can't post access this view's section
    '''

    def has_permission(self, request, view):
        if request.user.user_role == "Admin" or request.user.is_staff == True:
            pass
        else:
            raise PermissionDenied(detail=self.message)
        return super().has_permission(request, view)



