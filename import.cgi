#!/usr/bin/python

import os, ldap, ldif, sys, smtplib, cgi, cgitb, uuid, re
filename = str(uuid.uuid4())
textfile = '/export/home/idm_import/' + filename + '.tmp'
counter = '/export/home/idm_import/counter.txt' 
with open(counter, "rb") as rp:
        requestid = rp.readline() 


env = dict()
env['path'] = '/bin:/usr/bin:/usr/local/bin'

try:
        key1 = os.environ['SSL_CLIENT_S_DN_CN']
except KeyError:
        print("Location:https://xxx.xxx.xxx.xxx/idm_import/cert_error.html")
        print #end reponse
searchfilter = key1.split('.')[-1]
if searchfilter == '1404909556':
        print("Location:https://xxx.xxx.xxx.xxx/idm_import/user_account.html")
        print #end reponse

l = ldap.initialize('ldap://xxx.xxx.xxx.xxx:389')
ldap.set_option(ldap.OPT_REFERRALS, 0)
binddn = "xxxxxxxxxxxxxxxx"
pw = "xxxxxxxxxxxxxxx"
basedn = "xxxxxxxxxxxxxxxxxxxxxxx"
searchFilter = "(&(sAMAccountName="+searchfilter+"*))"
searchAttribute = ["mail","displayName"]
searchScope = ldap.SCOPE_SUBTREE
try:
    l.protocol_version = ldap.VERSION3
    l.simple_bind_s(binddn, pw) 
except ldap.INVALID_CREDENTIALS:
        print("Location:https://xxx.xxx.xxx.xxx/idm_import/ad_login_error.html")
        print #end reponse
except ldap.LDAPError, e:
        print("Location:https://xxx.xxx.xxx.xxx/idm_import/ad_error.html")
        print #end reponse
try:    
    ldap_result_id = l.search(basedn, searchScope, searchFilter, searchAttribute)
    result_set = []
    while 1:
        result_type, result_data = l.result(ldap_result_id, 0)
        if (result_data == []):
            break
        else:
            if result_type == ldap.RES_SEARCH_ENTRY:
                result_set.append(result_data)
    a = result_set
    mail_addr = a[0][0][1]['mail'][0]
    display_name = display_name = a[0][0][1]['displayName'][0]
except ldap.LDAPError, e:
        print("Location:https://xxx.xxx.xxx.xxx/idm_import/result_error.html")
        print #end reponse
l.unbind_s()

form = cgi.FieldStorage()

subject = [form.getvalue('subject')]

tonums = [form.getvalue('TONUM' + str(x)) for x in range(10) if form.getvalue('TONUM' + str(x)) and form.getvalue('REV' + str(x)) or form.getvalue('FRAME' + str(x) != 'Choose one below')]
z = []
for b in tonums:
        if b is None:
                z.append('<br />')
        else:
                besc = cgi.escape(b, True)
                besc = b.decode('string_escape')
                z.append(besc)
tonums = z

revs = [form.getvalue('REV' + str(x)) for x in range(10) if form.getvalue('TONUM' + str(x)) and form.getvalue('REV' + str(x)) or form.getvalue('FRAME' + str(x) != 'Choose one below')]
c = []
for d in revs:
        if d is None:
                c.append('<br />')
        else:
                desc = cgi.escape(d, True)
                desc = d.decode('string_escape')
                c.append(desc)
revs = c

urgents = [form.getvalue('URGENT' + str(x)) for x in range(10) if form.getvalue('TONUM' + str(x)) and form.getvalue('REV' + str(x)) or form.getvalue('FRAME' + str(x) != 'Choose one below')]
y = []
for w in urgents:
        if w is None:
                y.append('<br />')
        else:
                y.append(w)
urgents = y

secures = [form.getvalue('CLASS' + str(x)) for x in range(10) if form.getvalue('TONUM' + str(x)) and form.getvalue('REV' + str(x)) or form.getvalue('FRAME' + str(x) != 'Choose one below')]
g = []
for h in secures:
        if h is None:
                g.append('<br />')
        else:
                g.append(h)
secures = g


frames = [form.getvalue('FRAME' + str(x)) for x in range(10) if form.getvalue('TONUM' + str(x)) and form.getvalue('REV' + str(x)) or form.getvalue('FRAME' + str(x) != 'Choose one below')]
i = []
for j in frames:
        if j is None:
                i.append('<br />')
        else:
                i.append(j)

frames = i

news = [form.getvalue('NEW' + str(x)) for x in range(10) if form.getvalue('TONUM' + str(x)) and form.getvalue('REV' + str(x)) or form.getvalue('FRAME' + str(x) != 'Choose one below')]
k = []
for l in news:
        if l is None:
                k.append('<br />')
        else:
                k.append(l)
news = k


comments = [form.getvalue('COMMENTS' + str(x)) for x in range(10) if form.getvalue('TONUM' + str(x)) and form.getvalue('REV' + str(x)) or form.getvalue('FRAME' + str(x) != 'Choose one below')]
m = []
for n in comments:
        if n is None:
                m.append('<br />')
        else:
                nesc = cgi.escape(n, True)
                nesc = n.decode('string_escape')
                m.append(nesc)
comments = m

if subject[0] == 'Choose one below' or not tonums or not revs:
        print("Location:https://xxx.xxx.xxx.xxx/idm_import/form_error.html")
        print #end reponse

elif any(q == 'Choose one below' for q in frames):
        print("Location:https://xxx.xxx.xxx.xxx/idm_import/form_error.html")
        print #end reponse

elif any(len(r) > 50 for r in tonums):
        print("Location:https://xxx.xxx.xxx.xxx/idm_import/len_error.html")
        print #end reponse

elif any(len(t) > 25 for t in revs):
        print("Location:https://xxx.xxx.xxx.xxx/idm_import/len_error.html")
        print #end reponse

elif any(len(u) > 150 for u in comments):
        print("Location:https://xxx.xxx.xxx.xxx/idm_import/len_error.html")
        print #end reponse

else:

        f = open(textfile, "w")
        f.write("<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Transitional//EN' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd'><html><head><meta charset='utf-8'><title>Import Request</title></head><body style='font-family: Arial, Helvetica, sans-serif;'><h3>Import Request</h3>")
        f.write("<p>A request for import has been submitted to the WR-IDM support team with the following information. This is an automatically generated email, please do not reply. To request a status update or cancel a request an email may be sent to AFLCMC.PDSS.WR-IDMContentaImport@us.af.mil.</p><table cols='7' border='0' cellspacing='0' cellpadding='5' style='font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;'><tr style='border: 1px solid black;'><td style='background-color: black; color: white;'>Request ID: " + requestid + "</td><td style='background-color: black; color: white;' colspan='6'>Group: " + subject[0] + "</td></tr><tr style='border: 1px solid black;'><td style='background-color: black; color: white;'>TO NUMBER</td><td style='background-color: black; color: white;'>REVISION</td><td style='background-color: black; color: white;'>URGENT</td><td style='background-color: black; color: white;'>CLASSIFIED</td><td style='background-color: black; color: white;'>IMPORT TYPE</td><td style='background-color: black; color: white; word-wrap:break-word;'>NEW IMPORT</td><td style='background-color: black; color: white;'>COMMENTS</td></tr>" + "\n")
        for tonum, rev, urgent, secure, frame, new, comment in zip(tonums, revs, urgents, secures, frames, news, comments):
                if tonum == ' ':
                        continue
                f.write("<tr border='1' style='border: 1px solid black; background-color: white;'><td border='0' style='border-top: 1px solid black; border-right: 1px solid black; border-bottom: 1px solid black; border-left: 1px solid black;'><span>%s</span></td><td border='0' style='border-top: 1px solid black; border-right: 1px solid black; border-bottom: 1px solid black; border-left: 1px solid black;'><span>%s</span></td><td border='0' style='border-top: 1px solid black; border-right: 1px solid black; border-bottom: 1px solid black; border-left: 1px solid black;'><span>%s</span></td><td border='0' style='border-top: 1px solid black; border-right: 1px solid black; border-bottom: 1px solid black; border-left: 1px solid black;'><span>%s</span></td><td border='0' style='border-top: 1px solid black; border-right: 1px solid black; border-bottom: 1px solid black; border-left: 1px solid black;'><span>%s</span></td><td border='0' style='border-top: 1px solid black; border-right: 1px solid black; border-bottom: 1px solid black; border-left: 1px solid black;'><span>%s</span></td><td border='0'  style='border-top: 1px solid black; border-right: 1px solid black; border-bottom: 1px solid black; border-left: 1px solid black; word-wrap:break-word;'><span>%s</span></td></tr>" % (tonum, rev, urgent, secure, frame, new, comment) + "\n")
        f.write("<tr border='0' style='border: 1px solid black;'><td style='background-color: black; color: black;' colspan='7'><br /></td></tr></table></body></html>")

        f.close()

        fromaddr = 'no-reply@addr.ess'
        ccaddr = 'cc@addr.ess'
        toaddr = mail_addr
        
        from email.MIMEText import MIMEText
        fp = open(textfile, 'rb')
        msg = MIMEText(fp.read(), 'html')
        fp.close()
        subj = 'Request ID:' + requestid + ' IDM IMPORT {}'.format(subject[0])
        msg [ 'Subject' ] = subj
        msg [ 'From' ] = fromaddr
        msg [ 'To' ] = toaddr
        msg [ 'CC' ] = ccaddr

        s = smtplib.SMTP('localhost')
        s.sendmail(fromaddr, [toaddr,ccaddr], msg.as_string())
        s.quit()

        os.remove(textfile)
        with open(counter, "r+") as ip:
                value = int(ip.read())
                ip.seek(0)
                ip.write(str(value + 1))

        print("Location:https://xxx.xxx.xxx.xxx/idm_import/success.html")
        print #end response
