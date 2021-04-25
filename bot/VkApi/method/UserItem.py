class UserItem:

    member_id, invited_by, join_date, is_admin, is_owner = None, None, None, False, False

    def __init__(self, data):
        self.member_id = data['member_id']
        self.join_date = data['join_date']
        try:
            self.invited_by = data['invited_by']
        except:
            pass
        try:
            self.is_admin = data['is_admin']
        except:
            pass
        try:
            self.is_owner = data['is_admin']
        except:
            pass
