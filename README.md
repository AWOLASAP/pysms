# pysms
Open Source python interpreter that allows code to be ran off a host computer and outputs via text.

# Operating Systems
Currently this only works with Macos and maybe linux distrubutions(needs to be tested), as it uses bash to function.

# Future improvements
Currently working on getting the type of error to be outputed instead of just telling the user there is an error.

# HOW TO USE
1. Download code and make sure you have python installed with packages flask and twilio.
2. Get a free twilio account at www.twilio.com and set up a phone number.
3. Run the python script and host it (ngrok works fine)
4. Click on your number to get to the configure section and under messaging in the "message in" section where it says webhook put the website url with /sms added to the end of it.

