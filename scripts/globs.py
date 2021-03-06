class Global_vars:
    """ Global variable holder """
    ACL_MEMBER_FILE = "/etc/openvpn/scripts/acl_members"
    ACL_RULES_PATH = "/etc/openvpn/scripts/acl_rules/"
    USER_SESSION_PATH = "/tmp/openvpn-sessions/"
    DEBUG = False
    USER_ACL = ""


class Action_Enum:
    """ Enum to hold the three states an action can be
    from the variables passed in argv[1] """
    ADD = "add"
    UPDATE = "update"
    DELETE = "delete"


# struct like placeholder for
# all openvpn variables we get when script is called
class Openvpn_incoming_var:
    """ Placeholder for the three variables argv[1-3]
    that are passed down from OpenVPN hook """
    action = ""
    ip = ""
    user = ""
