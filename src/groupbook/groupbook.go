package groupbook
import (
	"google.golang.org/grpc/codes"
)
func IsUserInGroup(userid string)(string, error){
	groups := map[string]string{
		"alice": "permissionedgroup"
		"bob": "unperssionedgroup"
		"carol": "unperssionedgroup"
	}
	for key, element:= range group {
		if userid == key {
			return element, nil
		}
	}

	return nil, status.Errorf(codes.NotFound, "no user_id with ID %s", userid)

}

    userid := in.GetUserId() 
	groupid,err := IsUserInGroup(userid)
	if err!=nil{
		ctx := metadata.AppendToOutgoingContext(ctx, "groupid", groupid)
	}
	else{
		return nil, status.Errorf(codes.Internal, "failed to find the group id for userid: %+v", userid)
	}