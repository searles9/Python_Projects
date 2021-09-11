import subprocess 
import argparse
#-----------------
# COMMAND LINE ARGUMENTS
parser = argparse.ArgumentParser(description='Grant Bulk AD Security Group Access')
parser.add_argument('--adname', dest='adname', type=str, help='AD username of the individual who needs access to the security groups')
parser.add_argument('--adserver', dest='adserver', type=str, help='AD server')
args = parser.parse_args()
#-----------------
# VARIABLES
adserver = args.adserver
aduser = args.adname
#-----------------
def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed
#-----------------   

if __name__ == "__main__":
    adgroupfile = open("ADGROUPS.txt", "r") 
    for adgroup in adgroupfile:
        adgroup = adgroup.strip() # removing line endings
        the_command = "Add-ADGroupMember -Identity {group} -Members {user} -Server {server}".format(group = adgroup, user = aduser, server = adserver)
        command_result = run(the_command)
        if command_result.returncode != 0:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("An error occured: {error}".format(error = command_result.stderr))
            print("!!!!!!!!!!!!!!!!!!!!!!!!!")
            keepgoing = input("The command did not execute successfully.There was a problem adding {user} to {group} Would you like to continue? Enter Yes or No:  ".format(user = aduser, group = adgroup))
            if keepgoing.lower()[0] == 'y':
                continue
            else:
                adgroupfile.close()
                break
            print("-------------------------")
        else:
            print("{user} has been added to {group}".format(user = aduser, group = adgroup))
            print("-------------------------")
    adgroupfile.close()