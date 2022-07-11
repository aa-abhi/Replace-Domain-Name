def replace_domain(email,old_domain,new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index]+ "@" + new_domain
        return new_email
    return email

email= "abhi07@att.com"
old_domain = "att.com"
new_domain = "ac.in"
print(replace_domain(email,old_domain,new_domain))
