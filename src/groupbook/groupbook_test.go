package groupbook

import (
	"testing"
)

func TestIsUserInGroup(t *testing.T) {
	userids := ["alice","bob","carol"]
	groupids := ["permissionedgroup","unpermissionedgroup","unpermissionedgroup"]
	for i :=0:i<len(userids); i++ {
		GroupId, err := IsUserInGroup(userids[i])
		if err != nil {
			t.Errorf("Not able to find the group id for %+v", userids[i])
		}
		if GroupId != groupids[i] {
			t.Errorf("the group id is wrong, expected %+v, but find %+v", groupids[i],GroupId)
		}
	}
}
