# Subproccess and Powershell

## Important Notes
* **It would probably make more sense to just create a Powershell script for this** - but I wanted to test this out with Python. 
* I havent actully tested this script with an AD server. It is possible that it may run into issues since the command is typically run from Powershell as an Administrator. I will have to look into that at a later time if this is ever used.<br>
*(in testing I just used the "echo" command to confirm the logic worked)*

# What is this:
This script can be used to add a single AD user to a bulk set of AD security groups.

The script expects a text file called ```ADGROUPS.TXT``` as an input. The script then reads each line and adds the user to that AD security group.

If it runs into an error it stops and asks if you want to continue. If you say "no", the program stops.

# How to use this:
* Populate the ```ADGROUPS.TXT``` file with the security groups that you want the AD user added to (1 per line).
* To run the script:<br> ```python bulk-add-ad-user-to-sg.py --adname {ad name} --adserver {ad server}```
* Example: <br>
```python bulk-add-ad-user-to-sg.py --adname Jdoe --adserver domain.co```



# Some of the related Python Documentation:
* Python arguments: https://docs.python.org/3/library/argparse.html
* Subproccess module:  https://docs.python.org/3/library/subprocess.html