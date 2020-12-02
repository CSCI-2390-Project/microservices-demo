package groupbook
import (
	"google.golang.org/grpc/codes"
)
func IsUserInGroup(userid string)(string, error){
	groups := map[string]string{
		"alice": "permissionedgroup"
		"bob": "notperssionedgroup"
		"carol": "notperssionedgroup"
	}
	for i := 0; i < len(groups); i++ {
		if group[userid]!= nil {
			return group[userid], nil
		}
	}

	return nil, status.Errorf(codes.NotFound, "no user_id with ID %s", userid)

}